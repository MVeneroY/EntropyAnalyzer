#! /usr/local/bin/python3
# populate_csv.py

import sys
import subprocess
from typing import List
from os import listdir
from os.path import isfile, join, getsize

total_items = []

def main(directories: List[int]):

    for directory in directories:
        if 'unpacked' in directory: getData(directory, False)
        else:                       getData(directory, True)

def getData(directory: str, packed: bool = False):

    # get file name
    files = [file for file in listdir(directory) if isfile(join(directory, file))]
    paths = [join(directory, file) for file in files]
    
    # get file size
    sizes = [getsize(path) for path in paths]

    # get entropy (TODO: get output from entropy calls)
    command_path = '../target/entropy'
    try:
        for path in paths:
            subprocess.run(
                [command_path, path],
                timeout=5,
                check=True
            )
    except FileNotFoundError as e:
        print(f"Process failed because executable was not found. Make sure you provide a working file path\n{e}.")
    except subprocess.CalledProcessError as e:
        print(f"Process failed, return code was not successful."
              f"Returned {e.returncode}\n{e}")
    except subprocess.TimeoutExpired as e:
        print(f"Process timed out.\n{e}")

    for (file, size) in zip(files, sizes):
        print(f"file: {file}\tsize: {size}")

    # push {$name, $size, $entropy, $packed} to total_items 

if __name__ == '__main__':

    args = sys.argv.copy()
    args.pop(0)
    main(args)