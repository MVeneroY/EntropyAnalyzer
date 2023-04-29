#! /usr/bin/python3
# random_stream.py
# generate a stream of random values [0-255]

import sys
import random
from typing import List

def main(length: int, outFilePath: str, verbose: bool = False):
    stream = randomStream(length)
    if verbose: print([hex(x) for x in stream])

    stream = bytearray(stream)

    outFile = open(outFilePath, 'wb')
    outFile.write(stream)
    outFile.close()

def randomStream(length: int) -> List[int]:
    stream = []
    for i in range(length):
        stream.append(random.randint(0, 0xFF - 1)) 

    return stream

if __name__ == '__main__':
    # print(f"Arguments count: {len(sys.argv)}")
    length = int(sys.argv[1])
    outFilePath = sys.argv[2]
    verbose = '-v' in sys.argv

    main(length, outFilePath, verbose)