def supp_doub(l):
    lbis=l.copy()
    for i in range(len(l)-1):
        pas_enleve=True
        for j in range(i+1,len(l)):
            if l[i]==l[j] and pas_enleve:
                lbis.remove(l[i])
                pas_enleve=False 
    return lbis

l=[1,2,2,3,1,2,5,4,5,1,2,1,1]
print(supp_doub(l))
