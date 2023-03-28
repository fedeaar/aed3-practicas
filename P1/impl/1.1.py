# ej. 1.1
def subset_sum(C, i, j):  
    if j < 0:
        return False
    if i == 0: 
        return j == 0
    else: 
        if subset_sum(C, i - 1, j):
            return True
        if subset_sum(C, i - 1, j - C[i - 1]):
            print(C[i - 1])
            return True
        return False


# tests
if __name__ == "__main__":
    C = [6, 1, 1, 13, 4, 7, 1]
    subset_sum(C, len(C), 26)
