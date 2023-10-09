import sys
from module.controller import Controller

def main(*args):

    if (len(sys.argv) < 1):
        print('Invalid commands! Run with --help to view all commands')
        return
    
    args = sys.argv[1:]

    if (len(args) == 3):
        src_video = args[0]
        dest_video = args[1]
        sub_script = args[2]
        controller = Controller()

        controller.start(src_video, dest_video, sub_script)
    else:
        print('Invalid commands! Run with --help to view all commands')

if __name__ == "__main__":
    main()