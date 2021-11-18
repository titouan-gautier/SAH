A = [4, 5, 8, 9]
B = [7, 6, 3, 1]
def union(A,B):
    C = []
    for i in range(len(A)):
        C.append(A[i])
    for e in range(len(B)):
        C.append(B[e])
    return C
print(union(A,B))