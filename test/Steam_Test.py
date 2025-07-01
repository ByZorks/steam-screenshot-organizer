import unittest

from Steam import Steam

class TestSteam(unittest.TestCase):

    def setUp(self):
        self.steam = Steam()

    def test_get_user_id(self):
        user_id_to_find = 445561282
        self.steam.get_user_id()
        self.assertEqual(user_id_to_find, self.steam.id)

    def test_get_screenshots_path(self):
        screenshots_path_to_find = "D:\\Images\\Steam"
        screenshot_path = self.steam.get_screenshots_path()
        self.assertEqual(screenshots_path_to_find, screenshot_path)