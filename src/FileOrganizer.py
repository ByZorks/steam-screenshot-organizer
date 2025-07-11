import os
import time

import SteamManager

class FileOrganizer:
    """FileOrganizer class to organize Steam screenshots into game-specific folders."""

    steam: SteamManager.SteamManager
    path: str
    files: list[str]
    games_ids: dict[str, str]
    types: list[str]

    def __init__(self) -> None:
        self.steam = SteamManager.SteamManager()
        self.path = self.steam.get_screenshots_path()
        self.files = os.listdir(self.path)
        self.games_ids = dict()
        self.types = ['png', 'jpg', 'jpeg']

    def run(self) -> None:
        """Main entry point for the File Organizer program."""
        print("\nWelcome to the Steam Screenshot Organizer!")
        print("This program will organize your screenshots into folders based on the game they belong to.")
        print("It will only organize PNG, JPG, and JPEG files.")
        print("If you have any other file types, they will remain untouched.\n")

        print("Would you like to continue using the user information above? (Y/N): ")
        user_input = input()
        if user_input.lower() == 'y':
            self.organize()
            self.end_program("Organization complete! All screenshots have been organized into their respective game folders.")
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
                    self.end_program("Organization complete! All screenshots have been organized into their respective game folders.")
                else:
                    raise FileNotFoundError(f"The provided path does not exist: {custom_screenshots_path}")
            else:
                print("Exiting program in 10 seconds...")
                time.sleep(10)
                exit(0)

    def end_program(self, message: str) -> None:
        """Ends the program with a message."""
        print("\n" + message)
        print("Exiting program in 10 seconds...")
        time.sleep(10)
        exit(0)

    def organize(self) -> None:
        """Organizes the screenshots into folders based on the game they belong to."""
        if not any(file.endswith(tuple(self.types)) for file in self.files):
            raise ValueError("No PNG, JPG, or JPEG files found in the screenshots directory.")

        for file in self.files:
            if file.endswith(tuple(self.types)):
                folder_name = self.create_folders(file)
                if folder_name != "": self.move_file(file, folder_name)
            else:
                print(f"Skipping file: {file} (not a PNG, JPG, or JPEG)")

    def create_folders(self, file : str) -> str:
        """Creates a folder for the game based on the file name and returns the folder name."""
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
        """Moves the file to the corresponding game folder."""
        source = os.path.join(self.path, file)
        if not os.path.exists(source):
            print(f"Source file {file} does not exist, skipping move.") # Should not happen, but just in case
            return
        destination = os.path.join(self.path, folder_name, file)
        if not os.path.exists(destination):
            os.rename(source, destination)
        else:
            print(f"File {file} already exists in {folder_name}, skipping move.")
