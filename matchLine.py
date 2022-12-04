from DTW import dp
import numpy as np
# second DTW layer to check the words in the lines
def lineDistance(x, y):
    N = x.shape[0]
    M = y.shape[0]
    dist_mat = np.zeros((N, M))
    def dist(a, b):
        return 0 if a==b else 1
    for i in range(N):
        for j in range(M):
            # dist_mat[i, j] = abs(x[i] - y[j])
            dist_mat[i, j] = dist(x[i], y[j])
    p, cost_mat = dp(dist_mat)
    # printing the matching words
    for pair in p:
        if x[pair[0]]==y[pair[1]]:
            print(y[pair[1]],end=', ')
    return p, cost_mat[N - 1, M - 1]/max(N,M)
