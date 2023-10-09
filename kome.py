import argparse
from module.controller import Controller

def create_parser():
    parser = argparse.ArgumentParser(description='Convert Japanese subtitle into English Video')

    parser.add_argument('src', metavar='src', type=str, help='Input source video')
    parser.add_argument('dest', metavar='dest', type=str, help='Input destination video')
    
    parser.add_argument('-script', metavar='script', type=str, help='Input subtitle script to use instead of source track')
    parser.add_argument('-track', metavar='track', type=int, help='Input subtitle track to use for source video')

    return parser

def main(*args):
    
    parser = create_parser()
    args = parser.parse_args()

    src_video = args.src
    dest_video = args.dest

    sub_script = args.script
    track_no = args.track

    controller = Controller()
    controller.start(src_video, dest_video, 
                     sub_script, track_no)

if __name__ == "__main__":
    main()