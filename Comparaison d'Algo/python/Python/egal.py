t1 = [2, 3, 8, 7, 9, 5, 1]
t2 = [1, 2, 3, 8, 7, 9, 5]
def egal(A,B):
    nb = 0
    for i in range (len(A)):
        x = True
        for e in range (len(B)):
            if A[i] == B[e] and x:
                x = False
                nb = nb + 1
    if nb == len(A) :
        return True 
    else : 
        return False

print(egal(t1,t2))
        

