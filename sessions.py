import os

# default directories
LOCAL_DIRECTORY_WINDOWS = "C:\\Users\\%USERNAME%\\Downloads"  # local folder for the windows download
REMOTE_DIRECTORY = "/home/serveur/downloads"  # remote folder for download/upload

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
    """Upload a file from Windows to the Linux server."""
    file_name = os.path.basename(local_path)
    remote_path = os.path.join(REMOTE_DIRECTORY, file_name)
    
    # Commande SCP pour l'upload
    os.system(f'scp {local_path} user@server_ip:{remote_path}')
    print(f"File {file_name} uploaded to {remote_path} on the server.")

def download_file(file_name):
    """downloads a file from the Linux server to the Windows 'Download' folder."""
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
        print("\n--- Session Menu. ---")
        print("1. Créer une session")
        print("2. Lister les sessions")
        print("3. Attacher à une session")
        print("4. Terminer une session")
        print("7. Help (Commandes utiles)")
        print("8. Quitter")
        
        choice = input("Choice : ")
        
        if choice == '1':
            session_name = input("Session name : ")
            create_session(session_name)
        elif choice == '2':
            list_sessions()
        elif choice == '3':
            session_name = input("Name of the session to attach : ")
            attach_session(session_name)
        elif choice == '4':
            session_name = input("Name of the session to end : ")
            kill_session(session_name)
        elif choice == '5':
            file_path = input("Full path to the file to upload (from Windows): ")
            upload_file(file_path)
        elif choice == '6':
            file_name = input("Name of the file to download (from the server) : ")
            download_file(file_name)
        elif choice == '7':
            show_help()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please retry.")

if __name__ == "__main__":
    menu()
