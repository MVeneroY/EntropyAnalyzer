#! /usr/bin/python3
# populate_csv.py

import sys
import subprocess
from typing import List
from os import listdir
from os.path import isfile, join, getsize
import csv

# fields = ['file_name', 'file_size', 'entropy', 'packed']
total_items = []

def main(directories: List[int]):

    for directory in directories:
        if 'unpacked' in directory: getData(directory, False)
        else:                       getData(directory, True)

    writeToCSV()

def getData(directory: str, packed: bool = False):

    # get file name
    files = [file for file in listdir(directory) if isfile(join(directory, file))]
    paths = [join(directory, file) for file in files]
    
    # get file size
    sizes = [getsize(path) for path in paths]

    # get entropy (TODO: get output from entropy calls)
    command_path = '../target/entropy'
    entropies = []
    try:
        for path in paths:
            entropy = float(
                subprocess.run(
                    [command_path, path],
                    timeout=5,
                    check=True,
                    capture_output=True
                ).stdout
            )
            entropies.append(entropy)

    except FileNotFoundError as e:
        print(f"Process failed because executable was not found. Make sure you provide a working file path\n{e}.")
    except subprocess.CalledProcessError as e:
        print(f"Process failed, return code was not successful."
              f"Returned {e.returncode}\n{e}")
    except subprocess.TimeoutExpired as e:
        print(f"Process timed out.\n{e}")

    for (file, size, entropy) in zip(files, sizes, entropies):
        total_items.append({'file_name': file, 
                            'file_size': size,
                            'entropy': entropy,
                            'packed': packed
                            })

def writeToCSV():
    print(len(total_items))
    with open('../samples/data.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=total_items[0].keys())
        writer.writeheader()
        writer.writerows(total_items)

if __name__ == '__main__':

    args = sys.argv.copy()
    args.pop(0)
    main(args)