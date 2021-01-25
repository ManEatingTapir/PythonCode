# Sometimes we forget, in our personal scripts and programs, that we shouldn't put curses in a public project. This module is to read a file, find any and all curses, and if it finds any, prints the number of times it occurs.
import re
from pathlib import Path

def soap(file):
    """Uses regex to parse a file for any expletives. Returns a list of strings with the line each occurence is on."""
    # Check if it's a directory
    if Path(file).is_dir():
        raise IsADirectoryError
    # list to hold any output
    output = []
    with open(file) as f:
        # Check each line of file, index is used to indicate which line it's on (add one since iterator starts at 0)
        for index, line in enumerate(f):
            # TODO: make it parse for other swears. Keep some sort of list of patterns?
            if re.search('fu+ck', line):
                output.append(f'Cleanup crew on line {index + 1} in {file}')
    return output

# example code
if __name__ == '__main__':
    print(soap('ascii.py'))