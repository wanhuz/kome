import argparse
from module.controller import Controller

def clean_path(path : str):
    return path.replace('"', '')

def main(*args):

    print("Input source file destination: ")
    src_video = input()

    print("Input target file destination: ")
    dest_video = input()
    
    print("Input track no to be used: (Blank for no track number)")
    track_no = input()

    if (not track_no):
        print("Input external script file destination: (Blank for no external script) ")
        sub_script = input()
    else:
        sub_script = ""

    print("Complete sub cleaning mode? (y/n)")
    isCompleteClean = input()

    if ((isCompleteClean != 'y') and (isCompleteClean != 'Y')):
        isCompleteClean = False
    
    src_video = clean_path(src_video)
    dest_video = clean_path(dest_video)
    track_no = int(track_no)
    sub_script = clean_path(sub_script)

    try:
        controller = Controller()
        controller.start(src_video, dest_video, 
                        sub_script, track_no,
                        isCompleteClean)
    except Exception as ex:
        print(ex)
        
    print("Press any key to exit.")
    input()


if __name__ == "__main__":
    main()