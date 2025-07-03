import os
import SteamManager

class FileOrganizer:

    def __init__(self):
        self.steam = SteamManager.SteamManager()
        self.path = self.steam.get_screenshots_path()
        self.files = os.listdir(self.path)
        self.games_ids = dict()
        self.types = ['png', 'jpg', 'jpeg']

    def run(self) -> None:
        print("\nWelcome to the Steam Screenshot Organizer!")
        print("This program will organize your screenshots into folders based on the game they belong to.")
        print("It will only organize PNG, JPG, and JPEG files.")
        print("If you have any other file types, they will remain untouched.\n")

        print("Would you like to continue using the user information above? (Y/N): ")
        user_input = input()
        if user_input.lower() == 'y':
            self.organize()
        elif user_input.lower() == 'n':
            print("Would you like to enter a custom path to your screenshots directory? (Y/N): ")
            user_input = input()
            if user_input.lower() == 'y':
                print("Enter custom path to screenshots directory: ")
                custom_screenshots_path = input()
                if os.path.exists(custom_screenshots_path):
                    self.path = custom_screenshots_path
                    self.files = os.listdir(self.path)
                    self.organize()
                else:
                    print("Invalid path provided, exiting program.")
                    exit(1)
            else:
                print("Exiting program.")
                exit(0)

    def organize(self) -> None:
        if not any(file.endswith(tuple(self.types)) for file in self.files):
            print("No PNG, JPG, or JPEG files found to organize.")
            exit(1)

        for file in self.files:
            if file.endswith(tuple(self.types)):
                folder_name = self.create_folders(file)
                if folder_name != "": self.move_file(file, folder_name)
            else:
                print(f"Skipping file: {file} (not a PNG, JPG, or JPEG)")

    def create_folders(self, file : str) -> str:
        game_id = file.split('_')[0]
        if not game_id.isdigit():
            print(f"Skipping file {file} (does not start with a valid game ID)")
            return ""

        if game_id not in self.games_ids:
            game_name = self.steam.get_game_name(game_id)
            self.games_ids[game_id] = game_name
        else:
            game_name = self.games_ids[game_id]

        folder_path = os.path.join(self.path, game_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {game_name}")

        return game_name

    def move_file(self, file : str, folder_name : str) -> None:
        source = os.path.join(self.path, file)
        destination = os.path.join(self.path, folder_name, file)
        if not os.path.exists(destination):
            os.rename(source, destination)
        else:
            print(f"File {file} already exists in {folder_name}, skipping move.")
