# Sometimes we forget, in our personal scripts and programs, that we shouldn't put curses in a public project. This module is to read a file, find any and all curses, and if it finds any, prints the number of times it occurs.
import re
from pathlib import Path

# TODO: find way to integrate this with git precommit hooks so it runs whenever try to do a commit

def soap(file):
    # Check if it's a directory
    if Path(file).is_dir():
        raise IsADirectoryError
    # assume it doesn't have any swears
    bool_flag = True
    with open(file) as f:
        # Check each line of file, index is used to indicate which line it's on (add one since iterator starts at 0)
        for index, line in enumerate(f):
            # if there is a match
            if re.search('fu+ck', line):
                print(f'Cleanup crew on line {index + 1}')
                bool_flag = False
    return bool_flag

            
# example code
if __name__ == '__main__':
    print(soap('ascii.py'))