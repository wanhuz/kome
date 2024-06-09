import unittest
from module.finder import Finder


class FinderTest(unittest.TestCase):

    def test_get_episode_match_number(self):
        search_results = ['Subarashii Sekai ni Shukufuku o！ 3 - 07 「この成り上がり冒険者にも安息を！」 (AT-X 1280x720 x264 AAC).mkv', 
                          '[SubsPlease] Subarashii sekai - 07 (720p) [17584023].mkv']
        
        valid_result = 'Subarashii Sekai ni Shukufuku o！ 3 - 07 「この成り上がり冒険者にも安息を！」 (AT-X 1280x720 x264 AAC).mkv'
        series_name = 'Subarashii Sekai ni Shukufuku o！ 3'

        ext = '.mkv'
        episode_number = '07'

        for result in search_results:
            episode_found = Finder.get_episode(series_name, result, ext, episode_number)
            break

        self.assertEqual(valid_result, episode_found)

    def test_match_episode_number(self):
        valid_episode_name = "[SubsPlease] Subarashii sekai - 06 (720p) [17584023]"
        episode_number = "06"

        self.assertTrue(Finder.match_episode_number(episode_number, valid_episode_name))

    def test_extract_episode_number(self):
        valid_episode_name = "[SubsPlease] Subarashii sekai - 06 (720p) [17584023].mkv"
        episode_number = "06"

        extracted_ep_number = Finder.extract_episode_number(valid_episode_name)

        self.assertEqual(episode_number, extracted_ep_number)

    def test_extract_episode_number_with_season(self):
        valid_episode_name = "Hibike！ Euphonium 3 - 07"
        episode_number = "07"

        extracted_ep_number = Finder.extract_episode_number(valid_episode_name)

        self.assertEqual(episode_number, extracted_ep_number)

    def test_valid_match_extension(self):
        valid_episode_name_ext = "[SubsPlease] Subarashii sekai - 06 (720p) [17584023].mkv"
        ext = ".mkv"

        self.assertTrue(Finder.match_extension(valid_episode_name_ext, ext))

    def test_invalid_match_extension(self):
        invalid_episode_name_ext = "[SubsPlease] Subarashii sekai - 06 (720p) [17584023].mkv.sushi"
        ext = ".mkv"

        self.assertFalse(Finder.match_extension(invalid_episode_name_ext, ext))