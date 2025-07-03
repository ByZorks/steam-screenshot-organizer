import unittest

from SteamManager import SteamManager

class TestSteam(unittest.TestCase):

    def setUp(self) -> None:
        self.steam = SteamManager()

    def test_get_screenshots_path(self) -> None:
        screenshots_path_to_find = "D:\\Images\\Steam"
        screenshot_path = self.steam.get_screenshots_path()
        self.assertEqual(screenshots_path_to_find, screenshot_path)

    def test_get_game_name(self) -> None:
        app_id = "570"
        expected_game_name = "Dota 2"
        game_name = self.steam.get_game_name(app_id)
        self.assertEqual(expected_game_name, game_name)