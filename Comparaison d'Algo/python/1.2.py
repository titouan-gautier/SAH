

def extented_gcd(a, b) :
    if a == 0 :
        return (b, 0, 1)
    d, u, v = extented_gcd(b%a, b)

u1 = v - (b//a) * u
v1 = u

a = int(input("Saisir le premier terme: "))
b = int(input("Saisir le second terme: "))
d, u1, v1 = extented_gcd(a, b)
print(d, u1, v1)