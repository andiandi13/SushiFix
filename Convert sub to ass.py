import os
import subprocess
import re
import math
from fractions import Fraction
from video_timestamps import FPSTimestamps, TimeType, RoundingMethod

# Définition du FPS constant
FPS = Fraction(24000, 1001)

# Création de l'instance de conversion de timestamps
timestamps = FPSTimestamps(RoundingMethod.FLOOR, Fraction(1000), FPS)

def format_ass_time(seconds: float) -> str:
    """Convertit un temps en format ASS h:mm:ss.xx en tronquant les centièmes"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    sec = seconds % 60
    centiseconds = math.floor(sec * 100) / 100  # Tronquer sans arrondir
    return f"{hours}:{minutes:02}:{centiseconds:05.2f}"

def convert_sub_to_ass(sub_file):
    """Utilise FFmpeg pour convertir un fichier .sub en .ass sans toucher aux timecodes."""
    ass_file = sub_file.replace(".sub", ".ffmpeg.ass")

    # Exécuter ffmpeg pour obtenir un premier fichier .ass (seulement pour le texte et le formatage)
    subprocess.run(["ffmpeg", "-y", "-i", sub_file, ass_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if not os.path.exists(ass_file):
        print(f"Erreur : impossible de convertir {sub_file} en ASS avec FFmpeg.")
        return None

    return ass_file

def process_ass_timecodes(original_ass, sub_file):
    """Remplace les timecodes FFmpeg par ceux recalculés avec video_timestamps."""
    new_ass_file = sub_file.replace(".sub", ".ass")
    
    with open(original_ass, "r", encoding="utf-8") as f:
        ass_lines = f.readlines()
    
    # Charger le fichier .sub original pour extraire les timecodes corrects
    with open(sub_file, "r", encoding="utf-8") as f:
        sub_lines = f.readlines()

    # Extraire les frames de début et de fin depuis le fichier .sub
    frame_times = []
    for line in sub_lines:
        match = re.match(r"\{(\d+)\}\{(\d+)\}(.*)", line)
        if match:
            start_frame, end_frame, text = int(match.group(1)), int(match.group(2)), match.group(3)
            start_time = format_ass_time(timestamps.frame_to_time(start_frame, TimeType.START))
            end_time = format_ass_time(timestamps.frame_to_time(end_frame, TimeType.END))
            frame_times.append((start_time, end_time, text))

    # Réécriture du fichier .ass avec les nouveaux timecodes
    new_ass_lines = []
    idx = 0  # Index pour parcourir frame_times
    for line in ass_lines:
        if line.startswith("Dialogue:"):
            if idx < len(frame_times):
                start_time, end_time, text = frame_times[idx]
                # Remplace uniquement les timecodes dans la ligne
                new_line = re.sub(r"Dialogue: \d+,\d+:\d+:\d+\.\d+,\d+:\d+:\d+\.\d+", 
                                  f"Dialogue: 0,{start_time},{end_time}", line)
                new_ass_lines.append(new_line)
                idx += 1
            else:
                new_ass_lines.append(line)  # Au cas où il y aurait un décalage
        else:
            new_ass_lines.append(line)

    # Écriture du nouveau fichier ASS avec les timecodes corrigés
    with open(new_ass_file, "w", encoding="utf-8") as f:
        f.writelines(new_ass_lines)

    # Supprimer le fichier intermédiaire FFmpeg
    os.remove(original_ass)

    print(f"✅ Conversion terminée : {new_ass_file}")

def main():
    """Parcourt tous les fichiers .sub du dossier et les convertit en .ass."""
    for file in os.listdir():
        if file.endswith(".sub"):
            print(f"📂 Traitement du fichier : {file}")
            ass_file = convert_sub_to_ass(file)
            if ass_file:
                process_ass_timecodes(ass_file, file)

if __name__ == "__main__":
    main()
