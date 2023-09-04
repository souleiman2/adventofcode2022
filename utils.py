def read_txt_file(filename):
    f = open(filename + ".txt", "r")
    return f.readlines()

def strip(line):
    return line.strip()
