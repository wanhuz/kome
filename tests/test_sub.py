import unittest
from module.sub import Sub

class SubTest(unittest.TestCase):

    def test_is_valid_subtitle_valid(self):
        valid_subtitle_file = '[SubsPlease] Sousou no Frieren - 05 (720p) [9EA9D3FF].mkv.ja.ass'
        
        self.assertTrue(Sub.is_valid_subtitle(valid_subtitle_file))

    def test_is_valid_subtitle_invalid(self):
        invalid_subtitle_file = '[SubsPlease] Sousou no Frieren - 05 (720p) [9EA9D3FF].mkv'

        self.assertFalse(Sub.is_valid_subtitle(invalid_subtitle_file))
        
    def test_generate_output_filename_kome(self):
        sushi_sub = '[SubsPlease] Sousou no Frieren - 05 (720p) [9EA9D3FF].sushi.ass'
        kome_sub = '[SubsPlease] Sousou no Frieren - 05 (720p) [9EA9D3FF].kome.ass'

        self.assertEqual(Sub.generate_output_filename(sushi_sub), kome_sub)