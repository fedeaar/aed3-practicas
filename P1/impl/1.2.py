import numpy as np
import time


# ej 1.2; idea 1, naive
def esmagico_1(M):
    n = M.shape[0]
    s = M[1, :].sum()
    res = True
    k = 0 
    while k < n and res:
        res &= s == M[k, :].sum()
        res &= s == M[:, k].sum()
        k += 1
    res &= s == np.trace(M)
    res &= s == np.trace(M[::-1])
    return res

def magico_1(n):
    M = np.zeros((n, n))    # solución parcial                 
    I = [0] * (n * n)       # indica que números ya están en el cuadrado
    
    def _magico(i, j):
        nonlocal M, I, n
        if j == n:
            if i == n - 1: 
                return esmagico_1(M)
            else:
                i += 1
                j = 0
        suma = 0
        for k in range(1, n*n + 1):
            if I[k - 1] == 0:
                I[k - 1] = 1    # descarto k para las proximas vueltas
                M[i, j] = k     # genero la proxima solucion parcial
                suma += _magico(i, j + 1) 
                I[k - 1] = 0    # libero k
        return suma      

    return _magico(0, 0)


# ej 1.2; idea 2, sumas precalculadas
def esmagico_2(S):
    res = True
    k = 0
    while k < len(S) and res:
        res = res and S[1] == S[k]
        k += 1
    return res

def magico_2(n):
    S = [0] * (2*n + 2) # mantiene las sumas parciales en el orden F, C, D
    I = [0] * (n * n)   # indica que números ya están en el cuadrado           
    
    def _magico(i, j):
        nonlocal S, I, n
        if j == n:
            if i == n - 1:
                return esmagico_2(S)
            else:
                i += 1
                j = 0
        suma = 0
        for k in range(1, n*n + 1):
            if I[k - 1] == 0:
                # descarto k y modifico las sumas parciales
                I[k - 1] = 1
                S[i] += k
                S[n + j] += k
                if i == j:
                    S[2*n] += k
                if i == (n - 1 - j):
                    S[2*n + 1] += k
                # recurro
                suma += _magico(i, j + 1)
                # deshago las modificaciones
                I[k - 1] = 0
                S[i] -= k
                S[n + j] -= k
                if i == j:
                    S[2*n] -= k
                if i == (n - 1 - j):
                    S[2*n + 1] -= k
        return suma    

    return _magico(0, 0)


# ej 1.2; idea 3, sumas precalculadas con el algoritmo de Heap        
def magico_3(n):
    M = [x for x in range(1, n*n + 1)]  # solucion inicial
    # sumas parciales
    S = [0] * (2*n + 2)                 
    tmp = np.array(M).reshape(n, n)
    for k in range(n):
        S[k] = tmp[k, :].sum()
        S[n + k] = tmp[:, k].sum()
    S[2*n] = np.trace(tmp)
    S[2*n + 1] = np.trace(tmp[::-1])
    
    def _magico(k):
        nonlocal M, S, n
        if k == 1:
            return esmagico_2(S)
        else:
            suma = 0
            for i in range(k):
                # recurro
                suma += _magico(k - 1)
                # decido que elementos swappear
                p = i if (k % 2) == 0 else 0          
                # precalculo algunos valores
                f1, c1 = p // n, p % n
                f2, c2 = (k - 1) // n, (k - 1) % n 
                a, b = M[k - 1], M[p]
                c, d = a - b, b - a
                # actualizo filas
                S[f1] += c
                S[f2] += d
                # actualizo columnas
                S[n + c1] += c
                S[n + c2] += d
                # actualizo diagonales
                if f1 == c1:
                    S[2*n] += c
                if f1 == (n - 1 - c1):
                    S[2*n + 1] +=  c
                if f2 == c2:
                    S[2*n] += d
                if f2 == (n - 1 - c2):
                    S[2*n + 1] += d
                # swappeo
                M[p] = a
                M[k - 1] = b
            return suma

    return _magico(len(M))


# ej 1.2; idea 4, sumas precalculadas, usando poda de número mágico y cota inferior
# (sin conocerlo de antemano, basta asumir que la suma de la primer fila debería serlo)
def magico_4(n):
    S = [0] * (2*n + 2)
    I = [0] * (n * n)                 
    cota = n * n * (n * n + 1) / 2

    def _magico(cota, i, j):
        nonlocal I, S, n
        if j == n:
            if i == n - 1:
                return esmagico_2(S)
            else:
                i += 1
                j = 0
        suma = 0
        for k in range(1, n*n + 1):
            if I[k - 1] == 0:
                # poda por numero magico asumido y cota inferior
                nm = S[0]
                lb = nm - cota - k
                if (i == 0 or (lb <= S[i] + k <= nm and 
                               lb <= S[n + j] <= nm and
                               lb <= S[2*n] <= nm and
                               lb <= S[2*n + 1] <= nm)):
                    # descarto k y modifico las sumas parciales
                    I[k - 1] = 1
                    S[i] += k
                    S[n + j] += k
                    if i == j:
                        S[2*n] += k
                    if i == (n - 1 - j):
                        S[2*n + 1] += k
                    # recurro
                    suma += _magico(cota - k, i, j + 1)
                    # deshago las modificaciones
                    I[k - 1] = 0
                    S[i] -= k
                    S[n + j] -= k
                    if i == j:
                        S[2*n] -= k
                    if i == (n - 1 - j):
                        S[2*n + 1] -= k
        return suma

    return _magico(cota, 0, 0)


# ej 1.2; idea 5, sumas precalculadas, usando poda de número mágico exacta y cota inferior
def magico_5(n):
    S = [0] * (2*n + 2)    
    I = [0] * (n * n)                 
    cota = n * n * (n * n + 1) / 2
    nm = (n * n * n + n) / 2

    def _magico(cota, i, j):
        nonlocal I, S, nm, n
        if j == n:
            if i == n - 1:
                return esmagico_2(S)
            else:
                i += 1
                j = 0
        suma = 0
        for k in range(1, n*n + 1):
            if I[k - 1] == 0:
                # poda por numero magico asumido y cota inferior
                lb = nm - cota - k
                if (i == 0 or (lb <= S[i] + k <= nm and 
                               lb <= S[n + j] <= nm and
                               lb <= S[2*n] <= nm and
                               lb <= S[2*n + 1] <= nm)):
                    # descarto k y modifico las sumas parciales
                    I[k - 1] = 1
                    S[i] += k
                    S[n + j] += k
                    if i == j:
                        S[2*n] += k
                    if i == (n - 1 - j):
                        S[2*n + 1] += k
                    # recurro
                    suma += _magico(cota - k, i, j + 1)
                    # deshago las modificaciones
                    I[k - 1] = 0
                    S[i] -= k
                    S[n + j] -= k
                    if i == j:
                        S[2*n] -= k
                    if i == (n - 1 - j):
                        S[2*n + 1] -= k
        return suma

    return _magico(cota, 0, 0)


# tests
if __name__ == "__main__":
    n = 3
    s1 = time.time()
    print('magico_1 (naive):', magico_1(n), '. tiempo: ', time.time() - s1)
    s2 = time.time()
    print('magico_2 (sumas precomputadas):', magico_2(n), '. tiempo: ', time.time() - s2)
    s3 = time.time()
    print('magico_3 (sumas pre + Heap):', magico_3(n), '. tiempo: ', time.time() - s3)
    s4 = time.time()
    print('magico_4 (sumas pre + podas naive):', magico_4(n), '. tiempo: ', time.time() - s4)
    s5 = time.time()
    print('magico_5 (sumas pre + podas mas exactas):', magico_5(n), '. tiempo: ', time.time() - s5)
