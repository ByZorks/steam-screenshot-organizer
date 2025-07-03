import os
import time
import requests
import vdf

class SteamManager:
    def __init__(self):
        self.id = -1

    def get_most_recent_user_id(self) -> None:
        file = "C:\\Program Files (x86)\\Steam\\config\\loginusers.vdf"
        if not os.path.exists(file):
            raise FileNotFoundError(f"Login users file not found at {file}")

        with open(file, 'r', encoding='utf-8') as f:
            data = vdf.load(f)

            users = data.get('users', {})

            most_recent_user = None
            for steam_id, info in users.items():
                if info.get("MostRecent") == "1":
                    most_recent_user = {
                        "SteamID64": int(steam_id),
                        "AccountName": info.get("AccountName"),
                        "PersonaName": info.get("PersonaName"),
                    }
                    break

        if most_recent_user and self.verify_user_id(self.get_account_id(most_recent_user["SteamID64"])):
            account_id = self.get_account_id(int(most_recent_user["SteamID64"]))
            print(f"Most recent user ID: {account_id} ({most_recent_user['PersonaName']})")
            self.id = account_id
        else:
            raise ValueError("No most recent user found in loginusers.vdf file.")

    def verify_user_id(self, steam_3_account_id : int) -> bool:
        if not os.path.exists(f"C:\\Program Files (x86)\\Steam\\userdata\\{steam_3_account_id}"):
            raise FileNotFoundError(f"User ID {steam_3_account_id} does not exist in userdata directory.")
        else:
            print(f"User ID {steam_3_account_id} verified successfully.")

        return True

    def get_screenshots_path(self) -> str:
        if self.id == -1:
            self.get_most_recent_user_id()

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

    def get_game_name(self, app_id : str) -> str:
        url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                if app_id in data and 'data' in data[str(app_id)]:
                    game_name = data[app_id]['data'].get('name', 'Unknown Game')
                    unauthorized_char = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
                    for char in unauthorized_char:
                        game_name = game_name.replace(char, ' ')
                    return game_name

                else:
                    return 'Game not found'
            elif response.status_code == 429:
                print(f"Steam API Rate limit exceeded, retrying in 1 second...")
                time.sleep(1)
                return self.get_game_name(app_id)
            else:
                print(f"Application ID {app_id} not found. Status code: {response.status_code}")
                return 'Unknown Game - fetch failed'
        except Exception as e:
            print(f"An error occurred while fetching game name: {e}")
            return 'Error fetching game name'

    def get_account_id(self, steamid64: int) -> int:
        return steamid64 - 76561197960265728
