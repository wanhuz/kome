from ffsubsync import ffsubsync as ffs
import os

class FFS_API:

    @staticmethod
    def generate_output_filename(path):
        filename, ext = os.path.splitext(path)
        ffs_ext = '.ffs' + ext
        output_path = path.replace(ext, ffs_ext)
        return output_path

    @staticmethod
    def create_args(src_path, dest_path, output_path):
        parser = ffs.make_parser()
        args = parser.parse_args()

        src_path = src_path.replace('"', '')
        dest_path = dest_path.replace('"', '')

        args.reference = src_path
        args.srtin = [dest_path]
        args.srtout = output_path

        return args

    @staticmethod
    def retime_subtitle(src_path, script_path, output_path):
        ffs_args = FFS_API.create_args(src_path, script_path, output_path)

        ffs.run(ffs_args)
