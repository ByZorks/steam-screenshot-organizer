import unittest

from SteamManager import SteamManager

class TestSteam(unittest.TestCase):
    """Unit tests for the SteamManager class."""

    def setUp(self) -> None:
        """Set up the test environment by initializing the SteamManager."""
        self.steam = SteamManager()

    def test_get_screenshots_path(self) -> None:
        """Test the retrieval of the screenshots path."""
        screenshots_path_to_find = "" # This should be set to the expected path for your environment
        screenshot_path = self.steam.get_screenshots_path()
        self.assertEqual(screenshots_path_to_find, screenshot_path)

    def test_get_game_name(self) -> None:
        """Test the retrieval of a game's name by its app ID."""
        app_id = "570"
        expected_game_name = "Dota 2"
        game_name = self.steam.get_game_name(app_id)
        self.assertEqual(expected_game_name, game_name)