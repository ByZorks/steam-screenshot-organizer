import unittest

from Steam import Steam

class TestSteam(unittest.TestCase):

    def setUp(self):
        self.steam = Steam()

    def test_get_user_id(self):
        user_id_to_find = 123456789  # Replace with the actual user ID you expect
        self.steam.get_user_id()
        self.assertEqual(user_id_to_find, self.steam.id)

    def test_get_screenshots_path(self):
        screenshots_path_to_find = "D:\\Images\\Steam"
        screenshot_path = self.steam.get_screenshots_path()
        self.assertEqual(screenshots_path_to_find, screenshot_path)

    def test_get_game_name(self):
        app_id = 570
        expected_game_name = "Dota 2"
        game_name = self.steam.get_game_name(app_id)
        self.assertEqual(expected_game_name, game_name)