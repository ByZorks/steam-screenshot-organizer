import os

class FileOrganizer:

    def __init__(self):
        self.path = "D:\\Images\\Steam - Copy\\"
        self.files = os.listdir(self.path)
        self.types = ['png', 'jpg', 'jpeg']

    def organize(self):
        for file in self.files:
            if file.endswith(tuple(self.types)):
                folder_name = self.create_folders(file)
                self.move_file(file, folder_name)
            else:
                print(f"Skipping file: {file} (not a PNG, JPG, or JPEG)")

    def create_folders(self, file):
        folder_name = file.split('_')[0]
        folder_path = os.path.join(self.path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_name}")

        return folder_name

    def move_file(self, file, folder_name):
        source = os.path.join(self.path, file)
        destination = os.path.join(self.path, folder_name, file)
        if not os.path.exists(destination):
            os.rename(source, destination)
        else:
            print(f"File {file} already exists in {folder_name}, skipping move.")
