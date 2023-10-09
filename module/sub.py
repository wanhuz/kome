import pysubs2
import os

class Sub:

    def __new__(cls):
        raise TypeError("This is a static class and cannot be instantiated.")
    
    @staticmethod
    def valid_subtitle_extensions():
        valid_subtitle_extensions = (
            '.ass',
            '.srt'
        )

        return valid_subtitle_extensions
    
    @staticmethod
    def is_valid_subtitle(sub_filepath : str):

        if (sub_filepath.endswith(Sub.valid_subtitle_extensions())):
            return True
        return False

    @staticmethod
    def load(sub_path):
        return pysubs2.load(sub_path, encoding="utf-8")

    @staticmethod
    def export(subs, filepath : str):
        
        new_filepath = filepath.replace('.temp', '')
        for exts in Sub.valid_subtitle_extensions():
            new_filepath = new_filepath.replace(exts, '.ja.ass') # SRT cannot hold style

        subs.save(new_filepath)

    @staticmethod
    def cleanup(tempfile):
        os.remove(tempfile)