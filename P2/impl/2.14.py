# nota: me dio fiaca implementarlo con linked lists. 
# En una implementación con ll, se podría obviar todos los chequeos de None
 

def encontrar_ciclo_necesario(A, n):
    S = []
    I = [0] * n
    v = 0
    while I[v] == 0:
        S.append(v)
        I[v] = 1
        i = 0
        while i < len(A[v]) and A[v][i] == None:
            i += 1
        v = A[v][i]
    return S

def rem(A, n):
    S = []      # lista de vertices vacios
    E = [0] * n # si 1, el vertice es vacio
    R = [0] * n # vertices recorridos

    def rem_aux(v): # dfs
        R[v] = 1; c = 0
        for i, u in enumerate(A[v]):
            if u == None:
                continue
            if R[u] == 0:
                rem_aux(u)
            if E[u] == 1:
                A[v][i] = None
                c += 1
        if c == len(A[v]):
            E[v] = 1
            S.append(v)
            A[v] = None

    for v in range(n):
        if R[v] == 0:
            rem_aux(A, v)
    return S
        
def encontrar_ciclo(A, n):
    S = rem(A, n); r = False
    if len(S) < n:
        S = encontrar_ciclo_necesario(A, n); r = True
    return S, r


if __name__ == "__main__":

    A = [
        [1, 2, 3],
        [],
        [],
        [1, 2, 4],
        [0]
    ]
    B = [
        [1, 2, 3],
        [],
        [],
        [1, 2]
    ]
    for x in [A, B]:
        print(encontrar_ciclo(x, len(x)))
