#! /usr/bin/python3
# generate a stream of random values [0-255]

import sys
import random

def randomStream(length: int) -> list[int]:
    stream = []
    for i in range(length):
        stream.append(random.randint(0, 0xFF - 1)) 

    return stream

if __name__ == '__main__':
    # print(f"Arguments count: {len(sys.argv)}")
    length = int(sys.argv[1])
    outFilePath = sys.argv[2]

    stream = randomStream(length)
    if '-v' in sys.argv: print([hex(x) for x in stream])
    stream = bytearray(stream)
    # print(stream)

    outFile = open(outFilePath, 'wb')
    outFile.write(stream)
    outFile.close()