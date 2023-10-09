from module.cleaner import Cleaner
from module.sub import Sub
from module.sushi_api import Sushi_API as Sushi


class Controller:

    def __init__(self):
        pass
    
    def start(self, src_video, dest_video, subs_script="", track_no=0):
        
        temp_subtitle = Sushi.shift_subtitle(src_video, dest_video, subs_script, track_no)

        subtitle = Sub.load(temp_subtitle)
        
        new_subtitle = Cleaner.clean_subtitle_for_deaf(subtitle)
        new_subtitle = Cleaner.strip_whitespace(new_subtitle)
        new_subtitle = Cleaner.clean_empty_line(new_subtitle)
        new_subtitle = Cleaner.clean_style(new_subtitle)

        Sub.export(new_subtitle, temp_subtitle)
        Sub.cleanup(temp_subtitle)

