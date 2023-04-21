def act(A):
    
    n = len(A)
    M = []
    for i in range(n):
        M.append([-1]*n)

    def _act(s, i):
        if i == n:
            return s
        if M[s][i] == -1:
            a = _act(s, i+1)
            k = i + 1
            while k < n and A[k][0] < A[i][1]:
                k += 1
            b = _act(s+1, k)
            M[s][i] = max(a, b)
        return M[s][i]

    _act(0, 0)
    S = []
    s = 0
    for j in range(n-1, -1, -1):
        t = M[0][j]
        if t > s:
            s = t
            S.insert(0, A[j])
    return S

if __name__ == "__main__":
    A = [(6, 7), (1, 4), (0, 3), (4, 10), (3, 6)]
    A.sort()
    B = [(0, 6), (1, 4), (4, 6), (5, 7), (6, 8), (7, 8)]
    C = [(0, 20), (0, 10), (1, 2), (1, 3), (1, 4), (1, 5), (10, 11)]
    D = [(0, 5), (1, 10), (5, 12), (10, 11)]
    T = B
    print(T)
    print(act(T))