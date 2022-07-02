def read_file(filename):
    with open(filename) as f:
        cols, rows = [int(x) for x in next(f).split()] # read first line
        array = []
        for line in f: # read rest of lines
            array.append([int(x) for x in line.split()])
    return cols, rows, array