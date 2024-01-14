import unittest
from pysubs2 import SSAFile
from module.cleaner import Cleaner

class CleanerTest(unittest.TestCase):
    
    def test_clean_misc_symbol(self):
        raw_misc_symbol = """
        1
        00:00:01,101 --> 00:00:04,071
        ｟そういうものだよ みんなとの冒険だって➡
        """

        cleaned_misc_symbol = """
        1
        00:00:01,101 --> 00:00:04,071
        そういうものだよ みんなとの冒険だって
        """

        cleaned_subs = SSAFile.from_string(cleaned_misc_symbol)
        cleaned_subs = cleaned_subs[0].text

        subs = SSAFile.from_string(raw_misc_symbol)
        subs = Cleaner.clean_misc_symbol(subs)
        subs = subs[0].text

        self.assertEqual(subs, cleaned_subs)
    
    def test_clean_sound_effects(self):
        raw_sound_effect = """
        1
        00:00:01,101 --> 00:00:04,071
        （アイゼン）フリーレン（ドアを閉める音）
        魂の眠る地を探して
        """
        
        cleaned_sound_effect = """
        1
        00:00:01,101 --> 00:00:04,071
        フリーレン
        魂の眠る地を探して
        """

        cleaned_subs = SSAFile.from_string(cleaned_sound_effect)
        cleaned_subs = cleaned_subs[0].text

        subs = SSAFile.from_string(raw_sound_effect)
        subs = Cleaner.clean_sound_effects(subs)
        subs = subs[0].text

        self.assertEqual(subs, cleaned_subs)


    def test_strip_whitespace(self):
        whitespace = """
        1
        00:00:01,101 --> 00:00:04,071
        　フリーレン
        魂の眠る地を探して
        """
        
        cleaned_whitespace = """
        1
        00:00:01,101 --> 00:00:04,071
        フリーレン
        魂の眠る地を探して
        """

        cleaned_subs = SSAFile.from_string(cleaned_whitespace)
        cleaned_subs = cleaned_subs[0].text
        
        subs = SSAFile.from_string(whitespace)
        subs = Cleaner.strip_whitespace(subs)
        subs = subs[0].text

        self.assertEqual(subs, cleaned_subs)

    def test_apply_clean_style(self):
        style_name = 'CleanStyle'

        sub = """
        1
        00:00:01,101 --> 00:00:04,071
        フリーレン
        魂の眠る地を探して
        """

        subs = SSAFile.from_string(sub)
        styled_subs = Cleaner.clean_style(subs)
        styled_subs_style = styled_subs[0].style

        self.assertEqual(styled_subs_style, style_name)


    def test_clean_romaji(self):
        raw_romaji = """
        1
        00:00:01,101 --> 00:00:04,071
        齢(よわい)12歳にして最強クラスの狩竜人
        """
        
        cleaned_romaji = """
        1
        00:00:01,101 --> 00:00:04,071
        齢12歳にして最強クラスの狩竜人
        """

        cleaned_subs = SSAFile.from_string(cleaned_romaji)
        cleaned_subs = cleaned_subs[0].text

        subs = SSAFile.from_string(raw_romaji)
        subs = Cleaner.clean_romaji(subs)
        subs = subs[0].text

        self.assertEqual(subs, cleaned_subs)

    def test_clean_speaker(self):
        line_with_speaker = "綾小路：すべては南雲のわな。"
        valid_line_without_speaker = "すべては南雲のわな。"

        self.assertEqual(Cleaner.clean_speaker(line_with_speaker), valid_line_without_speaker)