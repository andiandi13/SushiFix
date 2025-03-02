#!/bin/bash

# Parcourir tous les fichiers vidéo dans le dossier courant
for video in *.{mp4,mkv,avi,flv,wmv,mov,webm}; do
    # Vérifier si des fichiers existent (évite les erreurs si aucun fichier trouvé)
    [ -e "$video" ] || continue

    # Nom du fichier de sortie (remplace l'extension par .txt)
    output="${video%.*}.txt"

    # Extraction des keyframes, soustraction de 1 et enregistrement
    ffprobe -select_streams v -show_frames \
    -show_entries frame=pict_type \
    -of csv "$video" | grep -n I | cut -d ':' -f 1 | awk '{print $1-1}' > "$output"

    echo "Keyframes ajustés de '$video' enregistrés dans '$output'"
done
