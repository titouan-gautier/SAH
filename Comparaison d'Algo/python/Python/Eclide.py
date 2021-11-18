a = 210
b = 55
res = 0
def euclide(a, b):
    for i in range(a):
        res = a%b
        if res == 0 :
            d = b 
            return d
        else : 
            a = b 
            b = res
print(euclide(a, b))