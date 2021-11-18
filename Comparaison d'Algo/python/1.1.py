
max= int(input("Entrez n :"))
liste = [0]
def list_prime(n) :
    for n in range(max):
        if n > 1:
            for i in range(2,n):
                if (n % i) == 0:
                     break
                else:
                    liste.append(i)
                
print(list_prime(10))