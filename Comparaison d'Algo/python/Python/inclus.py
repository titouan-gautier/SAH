A = [1, 4, 6]
B = [1, 2, 4, 3, 5, 6]

def inclus(A,B) :
    x = 0   
    for i in range(len(A)):
        for e in range(len(B)):
            if A[i] == B[e]:
                x = x + 1   
    if x == len(A):
        return True
    else :
        return False

print(inclus(A,B))