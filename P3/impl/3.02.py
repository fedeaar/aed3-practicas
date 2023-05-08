import numpy as np

def puentes(A, n):
    R = [0] * n
    S = [0] * n
    F = [0] * n
    B = []    
    t = 0

    def phi(v, p):
        nonlocal t
        t = t + 1
        R[v] = 1
        S[v] = t
        bmin = np.inf 
        for w in A[v]:
            if w == p: # padre
                continue
            if R[w] == 1:
                if S[w] < S[v]: # back-edge
                    x = S[w]
                else: # "forward-edge"
                    continue
            else: # hijo
                x = phi(w, v)
            if x > S[v]:
                B.append((v, w))
            if x < bmin:
                bmin = x 
        t = t + 1
        F[v] = t
        return bmin

    for i in range(n):
        if R[i] == 0:
            phi(i, -1)

    B.sort()
    return B


if __name__ == "__main__":
    A = [
        [1],
        [0, 2, 7],
        [1, 3, 8],
        [2, 4, 9],
        [3, 5, 6],
        [4],
        [4],
        [1, 10],
        [2, 9],
        [3, 8, 10],
        [7, 9, 11, 12],
        [10, 13],
        [10],
        [11, 14, 16],
        [13, 15, 16],
        [14],
        [13, 14, 17],
        [16, 18],
        [17, 19, 20],
        [18],
        [18, 21, 22],
        [20],
        [20]
    ]
    print(puentes(A, len(A)))
