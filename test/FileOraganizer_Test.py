import unittest
import os
from FileOrganizer import FileOrganizer

class TestFileOrganizer(unittest.TestCase):

    def setUp(self):
        self.organizer = FileOrganizer()
        self.number_of_files = len(self.organizer.files)

    def test_organize_files(self):
        initial_files = self.organizer.files.copy()
        self.organizer.organize()
        # Check if the number of files remains the same
        self.assertEqual(len(self.organizer.files), self.number_of_files)
        # Check if files have been moved to their respective folders
        for file in initial_files:
            folder_name = file.split('_')[0]
            folder_path = os.path.join(self.organizer.path, folder_name)
            if file.endswith(tuple(self.organizer.types)):
                self.assertTrue(os.path.exists(folder_path), f"Folder {folder_name} was not created.")
                self.assertTrue(os.path.exists(os.path.join(folder_path, file)), f"File {file} was not moved to {folder_name}.")
            else:
                self.assertFalse(os.path.exists(os.path.join(folder_path, file)), f"File {file} should not be in {folder_name}.")

    def tearDown(self):
        # Move the files back to the original directory for cleanup
        for file in self.organizer.files:
            folder_name = file.split('_')[0]
            folder_path = os.path.join(self.organizer.path, folder_name)
            if os.path.exists(os.path.join(folder_path, file)):
                os.rename(os.path.join(folder_path, file), os.path.join(self.organizer.path, file))

        # Remove the created folders
        directories = os.listdir(self.organizer.path)
        for directory in directories:
            dir_path = os.path.join(self.organizer.path, directory)
            if os.path.isdir(dir_path):
                os.rmdir(dir_path)