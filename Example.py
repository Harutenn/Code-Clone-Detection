def readText(fname):
    aa= a.split()
    aa= np.array(aa)
    bb= b.split()
    bb= np.array(bb)
    return lineDistance(aa, bb)