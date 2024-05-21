import os

class Finder:

    @staticmethod
    def find(name, path) -> list:
        search_results = []

        for root, dirs, files in os.walk(path):
            for file in files:
                if (name in file):
                    search_results.append(os.path.join(root, file))
                
        return search_results
    
    @staticmethod
    def get_episode(series_name, filename, ext, ep_number) -> str:
        if (series_name in filename) and (ext in filename) and (Finder.match_episode_number(ep_number, filename)):
            return filename
        
        return ""
    
    @staticmethod
    def match_episode_number(ep_number, filename):
        if ep_number in filename.split(" "):
            return True
        return False
    
    @staticmethod
    def extract_episode_number(filename):
        filename = filename.split(" ")
        
        for name in filename:
            if (name.isnumeric()):
                return name
        
        return None