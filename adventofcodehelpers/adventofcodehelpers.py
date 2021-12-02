def readFile(file):
    with open(file, "r") as f:
        return [x.strip() for x in f.readlines()]