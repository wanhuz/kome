import unittest
from module.finder import Finder

class FinderTest(unittest.TestCase):

    def test_get_episode_match_number(self):
        search_results = ['[SubsPlease] Subarashii sekai - 06 (720p) [17584023].mkv', 
                          '[SubsPlease] Subarashii sekai - 07 (720p) [17584023].mkv']
        
        valid_result = '[SubsPlease] Subarashii sekai - 06 (720p) [17584023].mkv'
        series_name = 'Subarashii sekai'

        ext = '.mkv'
        episode_number = '06'

        for result in search_results:
            episode_found = Finder.get_episode(series_name, result, ext, episode_number)
            break

        self.assertEqual(valid_result, episode_found)

    def test_match_episode_number(self):
        valid_episode_name = "[SubsPlease] Subarashii sekai - 06 (720p) [17584023]"
        episode_number = "06"

        self.assertTrue(Finder.match_episode_number(episode_number, valid_episode_name))

    def test_extract_episode_number(self):
        valid_episode_name = "[SubsPlease] Subarashii sekai - 06 (720p) [17584023]"
        episode_number = "06"

        extracted_ep_number = Finder.extract_episode_number(valid_episode_name)

        self.assertEqual(episode_number, extracted_ep_number)