def sort(C, n, m):
    M = [] 
    for i in range(n):
        M.append([])
    K = [0] * m
    for i in range(m):
        for c in C[i]:
            M[c[0]].append((i, c))
    for i in range(n):
        for j, c in M[i]:
            C[j][K[j]] = c
            K[j] += 1
    return

def designar(A, B, D, i):
    if D[i][1] >= 0:    # i tiene más cercanías con A
        B.append(i)
        D[i][0] = -1   # i pertenece a B
    else:
        A.append(i)
        D[i][0] = 1    # i pertenece a A
    return

def particionar(n, c, E, C):
    m = len(E)
    sort(C, n, m)
    # matriz de cercanias: col1 = pertenece a B=-1, NA=0, A=1, col2 balance actual.
    D = []
    for i in range(n):
        D.append([0, 0])
    # resultado
    P = []
    # greedy
    for i in range(m):
        A = []
        B = []
        if len(C[i]) < c:  # caso trivial
            A = E[i]
        else:
            for s, t in C[i]:
                if D[s][0] == 0: # designamos 1ero
                    designar(A, B, D, s)
                D[t][1] = D[t][1] + D[s][0] # balance 2do
            for k in E[i]:
                if D[k][0] == 0:
                    designar(A, B, D, k)
        P.append((A, B))
    return P


if __name__ == "__main__":
    n = 8
    c = 1
    E = [[0, 1, 2, 7], [4, 5, 6, 3]]
    C = [[(2, 7), (1, 2), (0, 1)], [(3, 4), (4, 5), (3, 6), (5, 6)]]
    print(particionar(n, c, E, C))
