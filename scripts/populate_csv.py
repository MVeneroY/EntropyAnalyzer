#! /usr/local/bin/python3

import sys
import subprocess
from typing import List

total_items = []

def main(directories: List[int]):
    print(directories)

    for directory in directories:
        if 'unpacked' in directory: getData(directory, False)
        else:                       getData(directory, True)

def getData(directory: str, packed: bool = False):
    # get file name
    files = []

    # get file size

    # get entropy (TODO: get output from entropy calls)
    executable_path = '../target/entropy'
    try:
        for file in files:
            subprocess.run(
                [executable_path, file],
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




    # push {$name, $size, $entropy, $packed} to total_items 

if __name__ == '__main__':
    print("hey", sys.argv)
    main(sys.argv[1:])