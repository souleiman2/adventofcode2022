def extract_is_file_and_size(line):
    relevant = line.split("(")[1].split(")")[0]
    if "dir" in relevant:
        return False, None
    return True, int(relevant.split("=")[1])

class Node:
    def __init__(self, is_leaf, lines):
        self.current_size = 0
        self.is_leaf = is_leaf
        self.child_dir = None if is_leaf else []
        self.update_current_size(lines)
    
    def get_is_leaf(self):
        return self.is_leaf
    
    def update_current_size(self, sub_lines):
        pass
