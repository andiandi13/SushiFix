Ceci est une méthode pour corriger les débordements des sous-titres convertis par sushi sur les scènes suivantes et précédentes

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

  
