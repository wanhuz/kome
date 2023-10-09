import pysubs2
import re

SOUND_EFFECT_SYMBOL = [
    '｟',
    '｠',
    '《',
    '》',
    '((',
    '))',
    '♬～',
    '➡',
    '⚞',
    '⚟',
    '≫',
    '≪'
]

SOUND_EFFECT_REGEX = '\（(.*?)\）'

class Cleaner:

    def __new__(cls):
        raise TypeError("This is a static class and cannot be instantiated.")
    
    @staticmethod
    def clean_misc_symbol(subs):
        for line in subs:
            for symbol in SOUND_EFFECT_SYMBOL:
                line.text = line.text.replace(symbol, '')
        return subs

    @staticmethod
    def clean_sound_effects(subs):
        for line in subs:
            line.text = re.sub(SOUND_EFFECT_REGEX, '', line.text)
        return subs

    @staticmethod
    def strip_whitespace(subs):
        for line in subs:
            line.text = line.text.strip()

        return subs

    @staticmethod
    def clean_style(subs):
        clean_style = subs.styles['Default'].copy()
        clean_style.fontname = "Arial Unicode MS"
        clean_style.outline = 0.5
        clean_style.fontsize = 20
        clean_style.marginv = 25
        clean_style.shadow = 0

        subs.styles['CleanStyle'] = clean_style

        for sub in subs:
            sub.style = "CleanStyle"

        return subs
    
    @staticmethod
    def clean_empty_line(subs):
        subs.remove_miscellaneous_events()
        return subs


