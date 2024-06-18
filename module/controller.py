from module.cleaner import Cleaner
from module.sub import Sub
from module.sushi_api import Sushi_API as Sushi
from module.ffs_api import FFS_API as FFS
from os import remove


class Controller:

    def __init__(self):
        pass
    
    def start(self, src_video, dest_video, subs_script="", track_no=0, isCompleteClean=False, isRemoveSource=False):
        
        if (src_video and dest_video and subs_script):
            Sushi.shift_subtitle(src_video, dest_video, subs_script, track_no)
            temp_subtitle = Sushi.get_sushi_generated_subs(dest_video)
            cleanup = True
        elif (src_video and dest_video):
            Sushi.shift_subtitle(src_video, dest_video, None, track_no)
            temp_subtitle = Sushi.get_sushi_generated_subs(dest_video)
            cleanup = True
        elif (src_video and subs_script):
            output_path = FFS.generate_output_filename(subs_script)
            FFS.retime_subtitle(src_video, subs_script, output_path)
            temp_subtitle = output_path
            cleanup = True
        elif (subs_script):
            temp_subtitle = subs_script
            cleanup = False

        subtitle = Sub.load(temp_subtitle)
        
        new_subtitle = Cleaner.clean_misc_symbol(subtitle)
        new_subtitle = Cleaner.clean_sound_effects(new_subtitle)

        if (isCompleteClean):
            new_subtitle = Cleaner.clean_sfx_suspect(new_subtitle)
            
        new_subtitle = Cleaner.clean_speaker(new_subtitle)
        new_subtitle = Cleaner.clean_romaji(new_subtitle)
        new_subtitle = Cleaner.strip_whitespace(new_subtitle)
        new_subtitle = Cleaner.clean_empty_line(new_subtitle)
        new_subtitle = Cleaner.clean_style(new_subtitle)

        new_subtitle_path = Sub.generate_output_filename(temp_subtitle)
        Sub.export(new_subtitle, new_subtitle_path)
        
        if (cleanup):
            Sub.cleanup(temp_subtitle)

        if (isRemoveSource):
            remove(src_video)