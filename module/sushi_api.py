from sushi import __main__ as Sushi
import os
import re

class Sushi_API:

    @staticmethod
    def create_args(src_path, dest_path, script_path, track_no):
        sushi_args = [
            "--src", src_path, 
             "--dst", dest_path
        ]

        # Prioritize external script over internal subtitle track
        if (script_path):
            sushi_args.extend(["--script", script_path])
        elif (track_no):
            sushi_args.extend(["--src-script", str(track_no)])

        return sushi_args

    @staticmethod
    def get_sushi_generated_subs():
        for file in os.listdir('.'):
            if ('sushi' in file):
                return file
        
        raise Exception('Generated file not found')

    @staticmethod
    def shift_subtitle(src_path, dest_path, script_path, track_no):
        
        sushi_args = Sushi_API.create_args(src_path, dest_path, script_path, track_no)

        Sushi.parse_args_and_run(sushi_args)

        temp_filename = Sushi_API.get_sushi_generated_subs()
        return temp_filename
