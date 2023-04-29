#! /usr/local/bin/python3

import sys
from typing import List

total_items = []

def main(directories: List[int]):
    print(directories)

    for directory in directories:
        if 'unpacked' in directory: getData(directory, False)
        else:                       getData(directory, True)

def getData(directory: str, packed: bool = False):
    # get file name
    # get file size
    # get entropy
    
    # push {$name, $size, $entropy, $packed} to total_items 
    pass 

if __name__ == '__main__':
    print("hey", sys.argv)
    main(sys.argv[1:])