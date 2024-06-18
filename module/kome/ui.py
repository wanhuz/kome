

class UI:
    @staticmethod
    def prompt_shift_subtitle():
        print("Input source file destination: ")
        src_video = input()

        print("Input target file destination: ")
        dest_video = input()
        
        print("Input track no to be used: (Blank for no track number)")
        track_no = input()
        if (track_no):
            track_no = int(track_no)

        return src_video, dest_video, track_no

    @staticmethod
    def prompt_shift_subtitle_external():
        print("Input source file destination: ")
        src_video = input()

        print("Input target file destination: ")
        dest_video = input()
        
        print("Input external script file destination: ")
        sub_script = input()

        return src_video, dest_video, sub_script

    @staticmethod
    def prompt_retime_subtitle():
        print("Input source file destination: ")
        src_video = input()
        
        print("Input external script file destination: ")
        sub_script = input()

        return src_video, sub_script

    @staticmethod
    def prompt_clean_subtitle():
        print("Input external script file destination: ")
        sub_script = input()

        return sub_script