import pysubs2
import os

class Sub:

    def __new__(cls):
        raise TypeError("This is a static class and cannot be instantiated.")
    
    @staticmethod
    def valid_subtitle_extensions():
        return (
            'ass',
            'srt',
        )
    
    @staticmethod
    def is_valid_subtitle(sub_filepath : str):

        if (sub_filepath.endswith(Sub.valid_subtitle_extensions())):
            return True
        return False
    
    @staticmethod
    def generate_output_filename(destpath):
        new_destpath = destpath.replace('.sushi', '.kome')
        for exts in Sub.valid_subtitle_extensions():
            new_destpath = new_destpath.replace(exts, 'ass') # SRT cannot hold style

        return new_destpath
    
    @staticmethod
    def load(sub_path):
        return pysubs2.load(sub_path, encoding="utf-8")

    @staticmethod
    def export(subs, destpath : str):
        subs.save(destpath)

    @staticmethod
    def cleanup(tempfile):
        os.remove(tempfile)