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

Installer [Python](https://www.python.org/) : 

## 1- Convertir les sous-titres .ass en .sub

Il faut utiliser SubtitleEdit (https://github.com/SubtitleEdit/subtitleedit/releases), qui converti correctement les sous-titres en .sub (format basé sur des frames et non des timecodes). Certains autres logiciels ou scripts sortent des frames incorrectes.

- Ouvrir SubtitleEdit
- Tools > Batch Convert
- Glisser-déposer tous les fichier à convertir
- Dans Format, choisir "MicroDVD (.sub)".
- Cliquer sur "Convert" pour démarrer la conversion

## 2- Créer les fichiers .txt keyframes à partir des vidéos

- Placer Extract_keyframes.sh dans le dossier des vidéos de destination (sur lesquelles synchroniser les sous-titres)
- Lancer le fichier .sh
- Attendre que chaque fichier .txt se génère (c'est assez long)

## 3- Corriger les fichiers SUB

- Placer le fichier Fix-SUB.py dans le même dossier que les sous-titres SUB a corriger
- Placer dans le même dossier tous les fichiers .txt des keyframes des videos
- Executer le fichier .py pour générer des version corrigées des SUB enregistrées avec le suffixe _fixed

## 4- Convertir les SUB corrigés en ASS

- Placer les fichiers .sub corrigées et le fichier "Convert sub to ass.py" dans le même dossier
- Executer le script "Convert sub to ass.py"
- Les fichiers .sub seront convertis en .ass

Note : La partie de la conversion du texte et du formattage est gérée par ffmpeg, et la partie de conversion des frames en timecodes est gérée par le script VideoTimestamps par moi15moi.
