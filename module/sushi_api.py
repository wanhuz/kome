from sushi import __main__ as Sushi
import os

class Sushi_API:

    @staticmethod
    def get_sushi_generated_subs(dest_video):
        dest_videopath = os.path.dirname(dest_video)

        if (dest_videopath):
            dest_videopath = dest_videopath + '/'
            path_to_find = dest_videopath + '/'
        else:
            path_to_find = '.'

        
        for file in os.listdir(path_to_find):
            if (('sushi' in file) and (path_to_find != '.')):
                return dest_videopath + file
            elif ('sushi' in file):
                return file
        
        raise Exception('Generated sushi file not found')

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
    def shift_subtitle(src_path, dest_path, script_path, track_no):
        sushi_args = Sushi_API.create_args(src_path, dest_path, script_path, track_no)

        Sushi.parse_args_and_run(sushi_args)
