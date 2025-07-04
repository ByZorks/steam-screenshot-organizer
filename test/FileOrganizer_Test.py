import unittest
import os
from FileOrganizer import FileOrganizer

class TestFileOrganizer(unittest.TestCase):
    """Unit tests for the FileOrganizer class."""

    def setUp(self) -> None:
        """Set up the test environment by initializing the FileOrganizer."""
        self.organizer = FileOrganizer()
        self.number_of_files = len(self.organizer.files)

    def test_organize_files(self) -> None:
        """Test the organization of files into game-specific folders."""
        initial_files = self.organizer.files.copy()
        # Ensure that valid files are present before organizing
        self.assertTrue(any(file.endswith(tuple(self.organizer.types)) for file in initial_files), "No valid files to organize.")

        self.organizer.organize()
        game_names = dict()
        # Check if the number of files remains the same
        self.assertEqual(len(self.organizer.files), self.number_of_files)
        # Check if files have been moved to their respective folders
        for file in initial_files:
            game_id = file.split('_')[0]
            if game_id not in game_names:
                game_names[game_id] = self.organizer.steam.get_game_name(int(game_id))
            game_name = game_names[game_id]
            folder_path = os.path.join(self.organizer.path, game_name)
            if file.endswith(tuple(self.organizer.types)):
                self.assertTrue(os.path.exists(folder_path), f"Folder {game_name} was not created.")
                self.assertTrue(os.path.exists(os.path.join(str(folder_path), str(file))), f"File {file} was not moved to {game_name} folder.")
            else:
                self.assertFalse(os.path.exists(os.path.join(str(folder_path), str(file))), f"File {file} should not be in {game_name} folder.")

    def tearDown(self) -> None:
        """Clean up the test environment by moving files back to the original directory."""
        try:
            directories = os.listdir(self.organizer.path)
            for directory in directories:
                dir_path = os.path.join(self.organizer.path, directory)
                if os.path.isdir(dir_path):
                    files_in_dir = os.listdir(dir_path)
                    for file in files_in_dir:
                        os.rename(os.path.join(dir_path, file), os.path.join(self.organizer.path, file))
                    os.rmdir(dir_path)
        except Exception as e:
            print(f"Error during cleanup: {e}")