import numpy as np


# ej. 1.4
def permutar(M):
    n = M.shape[0]
    I = [0]*n   # indicadores de los elementos contemplados en A
    A = [0]*n   # la permutación parcial que se está considerando
    a = 0       # suma parcial de la funcion objetivo
    B = [0]*n   # la mejor permutación hasta ahora
    b = np.inf  # el valor de la permutacion

    def _permutar(a, j):
        nonlocal I, A, B, b, n
        if j == n:
             # ultima suma de la fn objetivo
            a += M[A[n-1], A[0]]   
            if b > a:
                b = a
                B = A.copy()
        else:
            # el primer caso afuera para evitar un if en el loop
            if I[0] == 0:
                # probamos con el elemento
                I[0] = 1
                A[j] = 0
                _permutar(a, j + 1)
                # liberamos
                I[0] = 0
            for i in range(1, n):
                if I[i] == 0:
                    I[i] = 1
                    A[j] = i
                    # se suma la seleccion a la fn objetivo
                    _permutar(a + M[A[i - 1], A[i]], j + 1) 
                    I[i] = 0
            
    _permutar(0, 0)
    return B


# tests
if __name__ == "__main__":
    M = np.array([
        [0, 1, 10, 10],
        [10, 0, 3, 15],
        [21, 17, 0, 2],
        [3, 22, 30, 0]
    ])
    print(permutar(M))
