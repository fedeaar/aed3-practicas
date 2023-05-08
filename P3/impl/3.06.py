import numpy as np

def min_v(A, n, s, f):
    E = []
    R = [0] * n; R[0] = 1  # recorridos
    N = [0] * n            # nivel
    Q = [s]                # cola
    while len(Q) > 0:
        v = Q.pop(0)
        m = np.inf; a = (-1, -1)
        for w in A[v]:
            if R[w] == 0:
                R[w] = 1
                N[w] = N[v] + 1
                Q.append(w)
            else:
                p = f(v, w)
                if N[w] + 1 == N[v] and p < m:
                    m = p; a = (v, w)
        if m < np.inf:
            E.append(a)
    return E


if __name__ == "__main__":
    A = [
        [1, 3, 8],
        [0, 2, 3, 4],
        [1, 3, 6, 7],
        [0, 1, 2, 4],
        [1, 3, 5],
        [4],
        [2, 7, 8],
        [2, 6],
        [0, 6]
    ]
    pesos = {
        (0, 1): 5,
        (0, 3): 7,
        (0, 8): 8,
        (1, 2): 10,
        (1, 3): 9,
        (1, 4): 12,
        (2, 3): 20,
        (2, 6): 9, 
        (2, 7): 10,
        (3, 4): 7,
        (4, 5): 3,
        (6, 7): 4,
        (6, 8): 3
    }
    def f(v, w): return pesos[(v, w)] if v < w else pesos[(w, v)]
    print(min_v(A, len(A), 0, f))
