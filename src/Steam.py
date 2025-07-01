import os
import time
import requests

class Steam:
    def __init__(self):
        self.id = -1

    def get_user_id(self):
        parent_directory = "C:\\Program Files (x86)\\Steam\\userdata"
        directories = os.listdir(parent_directory)
        for directory in directories:
            if directory.isdigit():
                self.id = int(directory)
                print(f"Found user ID: {self.id}")
                break
        else:
            raise ValueError("No valid user ID found in userdata directory.")

    def get_screenshots_path(self):
        if self.id == -1:
            self.get_user_id()

        config_path = f"C:\\Program Files (x86)\\Steam\\userdata\\{self.id}\\config\\localconfig.vdf"
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found at {config_path}")

        with open(config_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if line.find("InGameOverlayScreenshotSaveUncompressed") != -1:
                    is_enabled = line.split('"')[3]
                    if is_enabled == "0":
                        print("In-game uncompressed screenshot saving is disabled, exiting program.")
                        exit(2)
                if line.find("InGameOverlayScreenshotSaveUncompressedPath") != -1:
                    path = line.split('"')[3]
                    print(f"Found screenshot path: {path}")
                    return path.replace("\\\\", "\\")

            return "No screenshots path found in config file."

    def get_game_name(self, app_id):
        url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                if str(app_id) in data and 'data' in data[str(app_id)]:
                    game_name = data[str(app_id)]['data'].get('name', 'Unknown Game')
                    unauthorized_char = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
                    for char in unauthorized_char:
                        game_name = game_name.replace(char, ' ')
                    return game_name

                else:
                    return 'Game not found'
            elif response.status_code == 429:
                print(f"Rate limit exceeded")
                time.sleep(1)
                return self.get_game_name(app_id)
            else:
                print(f"Application ID {app_id} not found. Status code: {response.status_code}")
                return 'Unknown Game - fetch failed'
        except Exception as e:
            print(f"An error occurred while fetching game name: {e}")
            return 'Error fetching game name'
