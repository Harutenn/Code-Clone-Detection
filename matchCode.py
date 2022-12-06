from matchLine import lineDistance
import numpy as np
from DTW import dp

def readText(fname):
    with open(fname, 'r') as f1:
        x = f1.readlines()
    # remove space and line switch at both side of the strings:
    x = list(map(lambda a: a.strip(), x))
    # remove empty string
    x = list(filter(lambda x: len(x) > 0, x))

    return np.array(x)
# uses a two-step DTW algorithm
def codeDistance(x, y):
    N = x.shape[0]
    M = y.shape[0]
    dist_mat = np.zeros((N, M))
    for i in range(N):
        for j in range(M):
            _,dist_mat[i, j] = dist(x[i], y[j])
    p, cost_mat = dp(dist_mat)
    return p, cost_mat[N - 1, M - 1]/max(N,M)

# formatting the inputs and storing into np
def dist(a, b):
    aa = a.split()
    aa = np.array(aa)
    bb = b.split()
    bb = np.array(bb)
    return lineDistance(aa, bb)

if __name__ == '__main__':
    x = readText('SourceCode.py')
    y = readText('Example.py')
    print("Matching Word(s):",end=' ')
    p, d = codeDistance(x, y)
    print()
    print('Overall Percent Similar:{:3.0f}%'.format((1-d)*100))

