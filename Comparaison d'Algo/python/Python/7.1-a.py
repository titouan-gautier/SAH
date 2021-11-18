a = 17
b = 4
def division(a, b) : 
    for i in range(a) :
        if b <= a :
            a = a - b
        else :
            return a, i 
print(division(a, b))
