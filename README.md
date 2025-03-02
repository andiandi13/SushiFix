### ENGLISH


# Method to Fix Sushi-Converted Subtitles

This method fix subtitles lines extending to previous and next scenes. It's an issue that happen often when using [Sushi](https://github.com/tp7/Sushi) to resync subtitles.

It can also be used for any subtitle files having this issue (if you consider it being an issue)

## Rules Applied
```
If a subtitle line starts on an exact keyframe, it is shifted by +2 frames.
If a subtitle line starts 1 frame before a keyframe, it is shifted by +3 frames.
If a subtitle line starts 1 frame after a keyframe, it is shifted by +1 frame.
If a subtitle line ends on an exact keyframe, it is shifted by -3 frames.
If a subtitle line ends 1 frame after a keyframe, it is shifted by -4 frames.
If a subtitle line ends 2 frames after a keyframe, it is shifted by -5 frames.
If a subtitle line ends 1 frame before a keyframe, it is shifted by -2 frames.
If a subtitle line ends 2 frames before a keyframe, it is shifted by -1 frame.
```

To comply with subtitle conventions:
- A subtitle line will always start with a 2-frame gap after a scene change.
- A subtitle line will always end with a 2-frame gap before a scene change.

## Prerequisites

- Install [Python](https://www.python.org/)
- Install the Python script "VideoTimestamps" by moi15moi: https://github.com/moi15moi/VideoTimestamps
- Install [FFmpeg](https://www.ffmpeg.org/) and add it to the [PATH](https://phoenixnap.com/kb/ffmpeg-windows) environment variable.
- Install [pysubs2](https://pypi.org/project/pysubs2/) (optional)

## 1- Convert .ass Subtitles to .sub

Use SubtitleEdit (https://github.com/SubtitleEdit/subtitleedit/releases), which correctly converts subtitles to .sub format (frame-based instead of timecode-based). Some other software or scripts may produce incorrect frames.

- Open SubtitleEdit
- Go to Tools > Batch Convert
- Drag and drop all files to be converted
- In Format, select "MicroDVD (.sub)"
- Click "Convert" to start the conversion

**Note:** Converting to .sub will remove all ASS tags and certain formatting.

**If you use raw ASS subtitles without formatting and only need to correct timecodes, this will not be an issue.**

**If your ASS subtitles have formatting, follow Step 5 to transfer the corrected timecodes to your original ASS files.**

## 2- Generate .txt Keyframe Files from Videos

- Place `Extract_keyframes.sh` in the folder containing the videos synchronized with the subtitles.
- Run the `Extract_keyframes.sh` script.
- Wait for all .txt files to be generated (this process takes some time).

## 3- Rename .txt Files

Keyframe .txt files must have the same name as their corresponding .sub subtitle files.
For example, if `001.txt` contains the keyframes for a video, the subtitle file for this video must be named `001.sub`.

Tools like [Ant Renamer](https://www.antp.be/software/renamer/en) can help automate batch renaming.

## 4- Fix SUB Files

- Place the `Fix-SUB.py` script in the same folder as the SUB subtitle files to be corrected.
- Also place all corresponding .txt keyframe files in the same folder.
- Run the .py script to generate corrected SUB files with the `_fixed` suffix.

Example:
```
📂Folder
 ┣ 📜Subtitle01.sub
 ┣ 📜Subtitle01.txt
 ┣ 📜Subtitle02.sub
 ┗ 📜Subtitle02.txt
```

## 5- Convert Fixed SUB Files to ASS

- Place the corrected .sub files and the `Convert sub to ass.py` script in the same folder.
- Run the `Convert sub to ass.py` script.
- The .sub files will be converted to .ass format.

**Note:**
- Text and formatting conversion is handled by FFmpeg.
- Frame-to-timecode conversion is handled by the `VideoTimestamps` script by moi15moi.
- This ensures that timecodes precisely match source frames, which is often incorrectly handled by other software (including FFmpeg).

## 6- (Optional) Copy Timecodes from Corrected ASS Subtitles to Original ASS Files

This step requires `pysubs2` installation.

In the same folder:

- Place the `Copy_timecodes_to_source.py` script.
- Place your original ASS subtitles and rename them as `source_name.ass`.
- Place the corrected ASS subtitles (from Step 5) and rename them as `destination_name.ass`.
- Run the .py script.

New `.ass` files with the `_final` suffix will be created, containing the original subtitles with corrected timecodes from the destination files.

Example file structure:


```
📂Folder
 ┣ 📜Subtitle01_source.ass
 ┣ 📜Subtitle01_destination.ass
 ┣ 📜Subtitle02_source.ass
 ┗ 📜Subtitle02_destination.ass
```

### FRANÇAIS

Cette méthode corrige les lignes de sous-titres qui débordent sur les scènes précédentes et suivantes.
C'est un problème qui survient souvent lors de l'utilisation de [Sushi](https://github.com/tp7/Sushi) pour resynchroniser les sous-titres.  

Elle peut également être utilisée pour tout fichier de sous-titres présentant ce problème (si vous considérez que c'en est un).


Les règles suivantes sont appliquées :
```
Si une ligne de sous-titres commence sur une keyframe exacte, elle est décalée de +2 frames.
Si une ligne de sous-titres commence sur 1 frame avant une keyframe, elle est décalée de +3 frames.
Si une ligne de sous-titres commence sur 1 frame après une keyframe, elle est décalée de +1 frame.
Si une ligne de sous-titres termine sur une keyframe exacte, elle est décalée de -3 frames.
Si une ligne de sous-titres termine sur 1 frame après une keyframe, elle est décalée de -4 frames.
Si une ligne de sous-titres termine sur 2 frames après une keyframe, elle est décalée de -5 frames.
Si une ligne de sous-titres termine sur 1 frame avant une keyframe, elle est décalée de -2 frames.
Si une ligne de sous-titres termine sur 2 frames avant une keyframe, elle est décalée de -1 frame.
```

Ainsi pour respecter les conventions de sous-titrage : 
une ligne de sous-titre commencera toujours en laissant un espace de 2 frames après le changement de scène
une ligne de sous-titre finira toujours en laissant un espace de 2 frames avant le changement de scène

## Pré-requis

- Installer [Python](https://www.python.org/)
- Installer le script python "VideoTimestamps" par moi15moi https://github.com/moi15moi/VideoTimestamps
- Installer [FFmpeg](https://www.ffmpeg.org/) et l'ajouter à la variable d'environnement [PATH](https://phoenixnap.com/kb/ffmpeg-windows)
- Installer [pysubs2](https://pypi.org/project/pysubs2/) (optionnel)


## 1- Convertir les sous-titres .ass en .sub


Il faut utiliser SubtitleEdit (https://github.com/SubtitleEdit/subtitleedit/releases), qui converti correctement les sous-titres en .sub (format basé sur des frames et non des timecodes). Certains autres logiciels ou scripts sortent des frames incorrectes.

- Ouvrir SubtitleEdit
- Tools > Batch Convert
- Glisser-déposer tous les fichier à convertir
- Dans Format, choisir "MicroDVD (.sub)".
- Cliquer sur "Convert" pour démarrer la conversion


**Note : La conversion en .sub supprimera toutes les balises ASS ainsi que certains formatages.**

**Si vous utilisez des sous-titres ASS bruts sans formatage et que vous souhaitez seulement corriger les timecodes, cela ne posera aucun problème**

**Si vous utilisez des sous-titres ASS avec formatage, suivez aussi l'étape 5 pour transferer les timecodes corrigés vers vos fichiers ASS sources**

## 2- Créer les fichiers .txt keyframes à partir des vidéos

- Placer Extract_keyframes.sh dans le dossier des vidéos sur lesquelles sont synchronisés les sous-titres)
- Lancer le fichier Extract_keyframes.sh
- Attendre que tous les fichiers .txt se génèrent (c'est assez long)

## 3- Renommer les fichiers .txt

Les fichiers keyframes en .txt doivent avoir le même nom que leurs fichiers .sub correspondant
Si le fichier 001.txt correspond aux keyframe d'une video, alors le fichier sous-titres .sub de cette vidéo devra être nommé 001.sub

Plusieurs logiciels permettent d'automatiser le renommage de plusieurs fichiers, comme [Ant Renamer](https://www.antp.be/software/renamer/fr)

## 3- Corriger les fichiers SUB

- Placer le fichier Fix-SUB.py dans le même dossier que les sous-titres SUB a corriger
- Placer dans le même dossier tous les fichiers .txt des keyframes des videos
- Executer le fichier .py pour générer des version corrigées des SUB enregistrées avec le suffixe _fixed

Exemple :

  
    📂Folder
     ┣ 📜Subtitle01.sub
     ┣ 📜Subtitle01.txt
     ┣ 📜Subtitle02.sub
     ┗ 📜Subtitle02.txt



## 4- Convertir les SUB corrigés en ASS

- Placer les fichiers .sub corrigées et le fichier "Convert sub to ass.py" dans le même dossier
- Executer le script "Convert sub to ass.py"
- Les fichiers .sub seront convertis en .ass

Note : La partie de la conversion du texte et du formattage est gérée par ffmpeg, et la partie de conversion des frames en timecodes est gérée par le script VideoTimestamps par moi15moi.
Ainsi les timecodes correspondent précisement aux frames sources, ce qui est habituellemnt mal géré par les autres logiciels (FFmpeg inclus)

## 5- (Optionnel) Copier les timecodes des sous-titres ASS dans les fichiers sources

Cette étape requiert l'installation de pysubs2.

Dans le même dossier : 

- Placer le fichier "Copy_timecodes_to_source.py"
- Placer vos sous-titres ASS d'origine et les renommer "nom_source.ass"
- Places les sous-titres ASS corrigés (à l'étape 4) et les renommer "nom_destination.ass"
- Executer le script .py

Des fichiers .ass avec le suffixe _final seront crées, ils correspondront aux fichiers sources avec les timecodes des fichiers destination

Exemple de structure des fichiers :

  
    📂Folder
     ┣ 📜Subtitle01_source.ass
     ┣ 📜Subtitle01_destination.ass
     ┣ 📜Subtitle02_source.ass
     ┗ 📜Subtitle02_destination.ass

  
