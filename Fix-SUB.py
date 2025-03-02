import os

def process_files():
    current_directory = os.getcwd()
    log_filename = "log.txt"

    # Parcourir tous les fichiers dans le répertoire
    for filename in os.listdir(current_directory):
        if filename.endswith(".sub"):  # Vérifier si c'est un fichier .sub
            base_filename = filename[:-4]  # Retirer l'extension .sub

            txt_filename = f"{base_filename}.txt"  # Le fichier .txt associé
            keyframes_filename = base_filename  # Le fichier keyframes sans suffixe

            # Vérifier si le fichier .txt existe
            txt_exists = os.path.exists(txt_filename)
            # Vérifier si le fichier de keyframes existe (le même nom que le fichier .sub)
            keyframes_exists = os.path.exists(keyframes_filename)

            # Si les deux fichiers existent
            if txt_exists and keyframes_exists:
                log_message = f"Traitement du fichier {filename} avec {txt_filename} et {keyframes_filename}...\n"
                print(log_message)
                with open(log_filename, 'a', encoding='utf-8-sig') as log_file:
                    log_file.write(log_message)  # Écrire dans le fichier log
                process_sub_file(filename, txt_filename, keyframes_filename, log_filename)
            else:
                # Si l'un des fichiers est manquant, logguer un message d'erreur
                missing_files = []
                if not txt_exists:
                    missing_files.append(txt_filename)
                if not keyframes_exists:
                    missing_files.append(keyframes_filename)
                log_message = f"Fichier(s) manquant(s): {', '.join(missing_files)}. Passage au suivant.\n"
                print(log_message)
                with open(log_filename, 'a', encoding='utf-8-sig') as log_file:
                    log_file.write(log_message)  # Enregistrer dans le fichier log

def process_sub_file(sub_filename, txt_filename, keyframes_filename, log_filename):
    # Implémentation de ta logique de traitement ici
    pass

# Appel à la fonction principale
process_files()
