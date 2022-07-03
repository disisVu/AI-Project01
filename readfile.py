import os, sys

def read_file(filename):
    with open(os.path.join(sys.path[0], filename), "r") as f:
        cols, rows = [int(x) for x in next(f).split()] # read first line
        array = []
        for line in f: # read rest of lines
            array.append([int(x) for x in line.split()])
    return cols, rows, array

# References: https://stackoverflow.com/questions/6583573/how-to-read-numbers-from-file-in-python