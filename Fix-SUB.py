import os
import re

def load_keyframes(txt_path):
    """Charge les keyframes depuis un fichier .txt."""
    with open(txt_path, 'r', encoding='utf-8') as file:
        keyframes = [int(line.strip()) for line in file if line.strip()]
    return keyframes

def adjust_frame(frame, keyframes):
    """Ajuste une frame (frame1 ou frame2) en fonction des règles."""
    for keyframe in keyframes:
        if frame == keyframe:
            return frame - 3  # Règle 1
        elif frame == keyframe + 1:
            return frame - 4  # Règle 2
        elif frame == keyframe + 2:
            return frame - 5  # Règle 3
        elif frame == keyframe - 1:
            return frame - 2  # Règle 4
        elif frame == keyframe - 2:
            return frame - 1  # Règle 8
    return frame  # Si aucune règle ne s'applique, retourne la frame inchangée

def adjust_start_frame(frame1, keyframes):
    """Ajuste frame1 en fonction des règles spécifiques."""
    for keyframe in keyframes:
        if frame1 == keyframe - 1:
            return frame1 + 3  # Règle 5
        elif frame1 == keyframe:
            return frame1 + 2  # Règle 6
        elif frame1 == keyframe + 1:
            return frame1 + 1  # Règle 7
    return frame1  # Si aucune règle ne s'applique, retourne la frame inchangée

def process_sub_file(sub_path, keyframes):
    """Traite un fichier .sub et applique les modifications."""
    # Ouvrir le fichier en détectant l'encodage (UTF-8 BOM ou standard)
    with open(sub_path, 'r', encoding='utf-8-sig') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        # Supprimer le BOM si présent (utf-8-sig le gère automatiquement)
        line = line.lstrip('\ufeff')
        
        # Utilisation d'une expression régulière pour extraire frame1, frame2 et le reste
        match = re.match(r'\{(\d+)\}\{(\d+)\}(.*)', line.strip())
        if match:
            frame1 = int(match.group(1))
            frame2 = int(match.group(2))
            rest = match.group(3)

            # Appliquer les règles pour frame1 et frame2
            frame1 = adjust_start_frame(frame1, keyframes)
            frame2 = adjust_frame(frame2, keyframes)

            # Reconstruire la ligne modifiée
            new_line = f"{{{frame1}}}{{{frame2}}}{rest}\n"
            new_lines.append(new_line)
        else:
            # Si la ligne ne correspond pas au format, la laisser inchangée
            new_lines.append(line)

    # Sauvegarder le fichier modifié
    new_sub_path = sub_path.replace('.sub', '_fixed.sub')
    with open(new_sub_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

def process_current_folder():
    """Parcourt le dossier courant et traite tous les fichiers .sub et .txt correspondants."""
    folder_path = os.getcwd()  # Dossier courant
    for filename in os.listdir(folder_path):
        if filename.endswith('.sub'):
            sub_path = os.path.join(folder_path, filename)
            txt_path = os.path.join(folder_path, filename.replace('.sub', '.txt'))

            if os.path.exists(txt_path):
                keyframes = load_keyframes(txt_path)
                process_sub_file(sub_path, keyframes)
                print(f"Fichier traité : {filename} -> {filename.replace('.sub', '_fixed.sub')}")
            else:
                print(f"Fichier .txt manquant pour : {filename}")

# Exécuter le script
process_current_folder()