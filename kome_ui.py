from module.controller import Controller
from module.kome.ui import UI
from sys import exit

def clean_path(path : str):
    return path.replace('"', '')

def main(*args):

    src_video = None
    dest_video = None
    track_no = None
    sub_script = None
    is_complete_clean = None
    is_remove_source = None

    print("Choose action:")
    print("1. Shift subtitle in video to another video")
    print("2. Shift subtitle in video to another video based on external subtitle")
    print("3. Retime subtitle based on external subtitle")
    print("4. Clean subtitle only")

    match input():
        case "1":
            src_video, dest_video, track_no = UI.prompt_shift_subtitle()
        case "2":
            src_video, dest_video, sub_script = UI.prompt_shift_subtitle_external()
        case "3":
            src_video, sub_script = UI.prompt_retime_subtitle()
        case "4":
            sub_script = UI.prompt_clean_subtitle()
        case _:
            print("Invalid selection!")
            exit(1)

    print("Complete sub cleaning mode? (y/n)")
    is_complete_clean = input()

    if ((is_complete_clean != 'y') and (is_complete_clean != 'Y')):
        is_complete_clean = False

    if (src_video):
        print("Remove source file? (y/n)")
        is_remove_source = input()

        if ((is_remove_source != 'y') and (is_remove_source != 'Y')):
            is_remove_source = False

    if (not sub_script) and (not src_video) and (not dest_video):
        print("Please input source/destination video or subtitle script")
        exit(1)
    
    if (src_video and dest_video):
        src_video = clean_path(src_video)
        dest_video = clean_path(dest_video)
    
    if (sub_script):
        sub_script = clean_path(sub_script)

    controller = Controller()
    controller.start(src_video, dest_video, 
                    sub_script, track_no, 
                    is_complete_clean, is_remove_source)
        
    input("Press any key to exit.")

if __name__ == "__main__":
    main()