from yaml import safe_load as yaml_safe_load
from module.finder import Finder
from module.controller import Controller

try:
    with open('kome_auto.yaml', 'r') as file:
        kome_auto = yaml_safe_load(file)
except IOError:
    exit('No kome_auto.yaml')
        
track = kome_auto['options']['track']
file_ext = kome_auto['options']['file_extension']
is_remove_source = kome_auto['options']['delete_after']
src_dir = kome_auto['options']['src_directory']
dest_dir = kome_auto['options']['dest_directory']

is_complete_clean = False
track_no = int(track)
sub_script = ""

for show in kome_auto['shows']:
    for src_show_name, dest_show_name in show.items():
        src_videos = Finder.find(src_show_name, src_dir)
        dest_videos = Finder.find(dest_show_name, dest_dir)
        
        if (not src_videos):
            print("Search not found for source: " + src_show_name)
            continue
        elif (not dest_videos):
            print("Search not found for destination: " + dest_show_name)
            continue

        for video in src_videos:
            src_video = video
            dest_video = ""
            episode_number = Finder.extract_episode_number(video)

            if (not episode_number):
                print("No episode number found for: " + src_video)
                break

            for video in dest_videos:
                if(Finder.get_episode(dest_show_name, video, file_ext, episode_number)):
                    dest_video = Finder.get_episode(dest_show_name, video, file_ext, episode_number)
                    break

            if (not dest_video):
                print("Destination video does not exist for: " + src_video)
                continue

            try:
                controller = Controller()
                controller.start(src_video, dest_video, 
                                sub_script, track_no, 
                                is_complete_clean, is_remove_source)
            except Exception as ex:
                print(ex)