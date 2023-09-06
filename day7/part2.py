import sys
sys.path.append('..') # to be able to import files from parent directory
from utils import read_txt_file, strip

class Folder:
    all_lines = ""
    
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.child_dir = []
        self.count_size_smaller_threshold = 0
    
    def update_size(self, start_index):
        THRESHOLD = 100000
        
        # skip the lines starting with $
        current_index = start_index
        while Folder.all_lines[current_index].startswith("$"):
            current_index += 1
        start_relevant = current_index
        
        # find until when does it end
        while current_index < len(Folder.all_lines) and not Folder.all_lines[current_index].startswith("$"):
            current_index += 1
        end_relevant = current_index
        
        relevant = Folder.all_lines[start_relevant:end_relevant]
        dirs_name = []
        direct_files_size = 0
        
        # do a first pass
        for line in relevant:
            if line.startswith("dir"):
                dirs_name.append(line[4:])
            else:
                direct_files_size += int(line.split(" ")[0])

        total_size = direct_files_size
        for dir_name in dirs_name:
            self.child_dir.append(Folder(dir_name))
            current_index = self.child_dir[-1].update_size(current_index)
            total_size += self.child_dir[-1].size
            self.count_size_smaller_threshold += self.child_dir[-1].count_size_smaller_threshold
        
        self.size = total_size
        if total_size <= THRESHOLD:
            self.count_size_smaller_threshold += total_size
            
        return current_index

def find_smallest_bigger_size(current_folder, minimum_size = 8381165):
    if current_folder.size < minimum_size:
        return float('inf')

    smallest_val = current_folder.size
    for child in current_folder.child_dir:
        smallest_val = min(smallest_val, find_smallest_bigger_size(child))
    return smallest_val



if __name__ == "__main__":
    lines = read_txt_file("input")
    lines = list(map(strip, lines))
    Folder.all_lines = lines
    root = Folder("/")
    root.update_size(0)
    
    print("Answer : ", find_smallest_bigger_size(root))
    
    
    