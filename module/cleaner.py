import pysubs2
import re

SFX_SYMBOL = [
    '｟',
    '｠',
    '《',
    '》',
    '((',
    '))',
    '♬～',
    '♪~',
    '~♪',
    '➡',
    '⚞',
    '⚟',
    '＜',
    '＞',
    '≫',
    '≪',
    '🔊',
    '📻',
    '📱',
    '📼',
    '📺',
    '♬'
]

SFX_EFFECT_SUSPECT = [
    '声',
    '音'
]

DIALOGUE_SYMBOL = '：';

SOUND_EFFECT_REGEX = '\（(.*?)\）'
ROMAJI_REGEX = '\((.*?)\)'

class Cleaner:

    def __new__(cls):
        raise TypeError("This is a static class and cannot be instantiated.")
    
    @staticmethod
    def clean_misc_symbol(subs):
        for line in subs:
            for symbol in SFX_SYMBOL:
                line.text = line.text.replace(symbol, '')
        return subs

    @staticmethod
    def clean_sound_effects(subs):
        for line in subs:
            line.text = re.sub(SOUND_EFFECT_REGEX, '', line.text)
        return subs
    
    def clean_romaji(subs):
        for line in subs:
            line.text = re.sub(ROMAJI_REGEX, '', line.text)
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
        clean_style.outline = 0.7
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
    
    @staticmethod
    def clean_sfx_suspect(subs):
        for line in subs:
            for symbol in SFX_EFFECT_SUSPECT:
                if (symbol in line.text):
                    print('Remove this line? (y/n)')
                    print(line.text)
                    is_line_removed = input()

                    if ((is_line_removed == 'y') or (is_line_removed == 'Y')):
                        line_removed = line.text
                        line.text = ''
                        print(line_removed + " removed.")
                    else:
                        print(line.text + " skipped.")
        return subs


    @staticmethod
    def clean_speaker(subs):
        for line in subs:
            if (DIALOGUE_SYMBOL in line.text):
                speaker_removed = line.text.split(DIALOGUE_SYMBOL, 1)[1]
                speaker_removed = speaker_removed.strip()

                line.text = speaker_removed

        return subs
    
