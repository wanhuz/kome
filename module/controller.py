from module.cleaner import Cleaner
from module.sub import Sub
from module.sushi_api import Sushi_API as Sushi


class Controller:

    def __init__(self):
        pass
    
    def start(self, src_videopath, dest_videopath, subs_script):
        shifted_subpath = Sushi.shift_subtitle(src_videopath, dest_videopath, subs_script)
        subtitle = Sub.load(shifted_subpath)
        
        new_subtitle = Cleaner.clean_subtitle_for_deaf(subtitle)
        new_subtitle = Cleaner.strip_whitespace(new_subtitle)
        new_subtitle = Cleaner.clean_misc(new_subtitle)
        new_subtitle = Cleaner.clean_style(new_subtitle)

        Sub.export(new_subtitle, shifted_subpath)
        Sub.cleanup(shifted_subpath)

