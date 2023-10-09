import unittest
from module.sushi_api import Sushi_API
import os

class Sushi_APITest(unittest.TestCase):

    def test_get_sushi_generated_subs(self):
        valid_video_path = 'test.mkv'
        valid_sushi_sub = 'test.mkv.sushi.ass'

        with open(valid_sushi_sub, 'w'):
            self.assertEqual(Sushi_API.get_sushi_generated_subs(valid_video_path), valid_sushi_sub)

        os.remove(valid_sushi_sub)