from module.cleaner import Cleaner
from module.sub import Sub
from module.sushi_api import Sushi_API as Sushi


class Controller:

    def __init__(self):
        pass
    
    def start(self, src_video, dest_video, subs_script="", track_no=0):
        
        Sushi.shift_subtitle(src_video, dest_video, subs_script, track_no)
        temp_subtitle = Sushi.get_sushi_generated_subs()

        subtitle = Sub.load(temp_subtitle)
        
        new_subtitle = Cleaner.clean_misc_symbol(subtitle)
        new_subtitle = Cleaner.clean_sound_effects(new_subtitle)
        new_subtitle = Cleaner.strip_whitespace(new_subtitle)
        new_subtitle = Cleaner.clean_empty_line(new_subtitle)
        new_subtitle = Cleaner.clean_style(new_subtitle)

        new_subtitle_path = Sub.generate_output_filename(temp_subtitle)
        Sub.export(new_subtitle, new_subtitle_path)
        Sub.cleanup(temp_subtitle)

