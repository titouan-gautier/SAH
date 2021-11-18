t1 = [1, 2, 3, 4, 5]
t2 = [6, 7, 8, 9, 10, 56, 98]
def disjoint(A, B):
    nb = 0
    for i in range (len(A)):
        x = True
        for e in range (len(B)):
            if A[i] == B[e] and x:
                x = False
                return False
            else : 
                nb = nb + 1
    if nb == len(A) or nb == len(B):
        return False
    else : 
        return True

print(disjoint(t1,t2))