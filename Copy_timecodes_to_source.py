import os
import pysubs2

def process_files(source_file, dest_file, output_file):
    try:
        # Chargement des fichiers ASS avec pysubs2
        sub_source = pysubs2.load(source_file, encoding="utf-8")
        sub_dest   = pysubs2.load(dest_file, encoding="utf-8")
    except Exception as e:
        print(f"Erreur lors du chargement de {source_file} ou {dest_file}: {e}")
        return

    # Vérifie que le nombre d'événements (lignes de dialogue) est identique
    if len(sub_source) != len(sub_dest):
        print(f"Nombre d'événements différent entre {source_file} et {dest_file}. Opération annulée.")
        return

    # Pour chaque événement, on remplace les timecodes par ceux du fichier destination
    for i, event in enumerate(sub_source):
        event.start = sub_dest[i].start
        event.end   = sub_dest[i].end

    try:
        # Sauvegarde dans un nouveau fichier avec le suffixe _final.ass
        sub_source.save(output_file, format="ass", encoding="utf-8-sig")
        print(f"Fichier généré : {output_file}")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement du fichier {output_file}: {e}")

def main():
    # Recherche de tous les fichiers .ass dans le dossier courant
    files = [f for f in os.listdir() if f.endswith(".ass")]
    # Dictionnaires indexés par le nom de base (avant le suffixe)
    source_files = {f.replace("_source.ass", ""): f for f in files if f.endswith("_source.ass")}
    dest_files   = {f.replace("_destination.ass", ""): f for f in files if f.endswith("_destination.ass")}

    # Pour chaque fichier dont le nom de base est identique dans source et destination
    for base, src in source_files.items():
        if base in dest_files:
            dest = dest_files[base]
            output = base + "_final.ass"
            process_files(src, dest, output)
        else:
            print(f"Pas de fichier destination correspondant pour : {src}")

if __name__ == "__main__":
    main()
