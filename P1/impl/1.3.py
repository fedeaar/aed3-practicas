import numpy as np


# ej. 1.3; M es simétrica
def maximizar(M, k):
    n = M.shape[0]
    A = [0]*n   # contiene la solucion parcial actual
    a = 0       # suma los elementos de A
    m = 0       # s(A)
    B = [0]*n   # contiene la mejor solucion candidata hasta ahora
    b = 0       # s(B)

    def _maximizar(m, a, j):
        nonlocal M, A, B, b, n, k
        if a == k:
            if m > b: # si la solucion actual es mejor
                b = m
                B = A.copy()
            return m
        elif j == n:
            return m
        else:
            # a + {0}
            s0 = _maximizar(m, a, j + 1)
            # a + {1}
            A[j] = 1
            for i in range(j + 1): # sumo la nueva columna 
                m += A[i] * M[i, j]
            s1 = _maximizar(m, a + 1, j + 1)
            A[j] = 0
            return max(s0, s1)

    _maximizar(m, a, 0)
    return B


# tests
if __name__ == "__main__":

    k = 3
    M = np.array(
       [[0, 10, 10, 1], 
        [10, 0,  5, 2], 
        [10, 5,  0, 15], 
        [1,  2,  15, 0]]
    )
    print(maximizar(M, k))
