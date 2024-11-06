import os

# Répertoires par défaut
LOCAL_DIRECTORY_WINDOWS = "C:\\Users\\Gamme\\Downloads"  # Dossier local pour le download sur Windows
REMOTE_DIRECTORY = "/home/serveur/downloads"  # Dossier distant pour le download/upload

def create_session(session_name):
    os.system(f'tmux new-session -d -s {session_name}')
    print(f"Session '{session_name}' créée.")

def list_sessions():
    os.system('tmux ls')

def attach_session(session_name):
    os.system(f'tmux attach-session -t {session_name}')

def kill_session(session_name):
    os.system(f'tmux kill-session -t {session_name}')
    print(f"Session '{session_name}' terminée.")

def upload_file(local_path):
    """Upload un fichier depuis Windows vers le serveur Linux."""
    file_name = os.path.basename(local_path)
    remote_path = os.path.join(REMOTE_DIRECTORY, file_name)
    
    # Commande SCP pour l'upload
    os.system(f'scp {local_path} user@server_ip:{remote_path}')
    print(f"Fichier {file_name} uploadé vers {remote_path} sur le serveur.")

def download_file(file_name):
    """Télécharge un fichier depuis le serveur Linux vers le dossier 'Download' de Windows."""
    remote_path = os.path.join(REMOTE_DIRECTORY, file_name)
    local_path = os.path.join(LOCAL_DIRECTORY_WINDOWS, file_name)
    
    # Commande SCP pour le download
    os.system(f'scp user@server_ip:{remote_path} {local_path}')
    print(f"Fichier {file_name} téléchargé dans {local_path} sur Windows.")

def show_help():
    print("\n--- Commandes Utiles ---")
    print("1. Copier un fichier : `cp <source> <destination>`")
    print("   Ex : cp /home/simon/fichier.txt /home/simon/copie.txt")
    print("2. Coller un fichier : Le fichier est copié avec `cp`, pas besoin de commande spécifique.")
    print("3. Supprimer un fichier : `rm <fichier>`")
    print("   Ex : rm /home/simon/fichier.txt")
    print("4. Couper un fichier : `mv <source> <destination>`")
    print("   Ex : mv /home/simon/fichier.txt /home/simon/dossier/")
    print("-----------------------")

def menu():
    while True:
        print("\n--- Menu des Sessions ---")
        print("1. Créer une session")
        print("2. Lister les sessions")
        print("3. Attacher à une session")
        print("4. Terminer une session")
        print("7. Help (Commandes utiles)")
        print("8. Quitter")
        
        choice = input("Choix : ")
        
        if choice == '1':
            session_name = input("Nom de la session : ")
            create_session(session_name)
        elif choice == '2':
            list_sessions()
        elif choice == '3':
            session_name = input("Nom de la session à attacher : ")
            attach_session(session_name)
        elif choice == '4':
            session_name = input("Nom de la session à terminer : ")
            kill_session(session_name)
        elif choice == '5':
            file_path = input("Chemin complet du fichier à uploader (depuis Windows) : ")
            upload_file(file_path)
        elif choice == '6':
            file_name = input("Nom du fichier à télécharger (depuis le serveur) : ")
            download_file(file_name)
        elif choice == '7':
            show_help()
        elif choice == '8':
            break
        else:
            print("Choix invalide. Réessayez.")

if __name__ == "__main__":
    menu()
