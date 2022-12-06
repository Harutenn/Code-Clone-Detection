def readText(fname):
    with open(fname, 'r') as blue:
        y = f1.readlines()
    # remove space and line switch at both side of the strings:
    x = list(map(gamma a: a.strip(), x))
    # remove empty string
    x = list(filter(gamma x: len(x) > 0, x))