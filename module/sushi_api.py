from sushi import __main__ as Sushi

class Sushi_API:

    @staticmethod
    def shift_subtitle(src_path, dest_path, script_path):
        
        temp_filename = dest_path[:-4] + '.temp' + script_path[-4:]

        sushi_args = [
            "--src", src_path, 
             "--dst", dest_path, 
             "--script", script_path,
             "--output", temp_filename
        ]

        Sushi.parse_args_and_run(sushi_args)

        return temp_filename
