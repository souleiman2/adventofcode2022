def is_all_diff(substr):
    return len(list(set(substr))) == len(substr)

def find_start_pos(line):
    index = 0
    size_substr = 4
    while index < len(line) - size_substr + 1:
        if is_all_diff(line[index:index+size_substr]):
            return index + size_substr
        index += 1
