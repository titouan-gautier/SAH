import random 

def list_prime(x) :
    i=1
    liste = []
    for k in range (1, (x+1), 1):
        c=0
        for j in range (1, (i+1), 1):
            a = i%j
            if (a==0):
                c = c+1

        if (c==2):
            liste.append(i)
        else:
            k = k-1
        i=i+1
    return liste

def extended_gcd(a,b):
    if a < b : 
        a,b = b,a
    u0, u1 = 1, 0
    v0, v1 = 0, 1
    while b != 0 :
        q = int(a/b)
        b, a = a%b, b
        u0, u1, v0, v1 = v0, v1, u0-q*v0, u1-q*v1
    return a,u0,u1

def key_creation() :
    p = random.choice(list_prime(1000))
    q = random.choice(list_prime(1000))
    n = p*q
    fiN = (p-1)*(q-1)
    e = 2
    a = 0
    d = 2
    res = 0
    while a != 1 :
        a,u0,u1 = extended_gcd(e, fiN)
        if a != 1 :
            e = e + 1
        pub = (n,e)

    while res != 1 :
        res = (e*d)%fiN
        d = d + 1
    priv = (n,d-1)
    return p,q,n,pub,priv


msg = "salut"

def convert_msg(msg) :
    msgcrypte = ""
    
    for i in range(len(msg)) :
        msgcrypte += str(ord(msg[i]))
        
    
    if len(msgcrypte)%4 !=0 :
        msgcrypte = "0" + msgcrypte
   
    msgcryptefin = []

    while len(msgcrypte) != 0 :
        msgcryptefin.append(msgcrypte[:3])
        msgcrypte = msgcrypte[3:]
    return msgcryptefin


msgc = convert_msg(msg)

def deconvert_msg(msgc) :
    msgdecrypte = []
    for i in range(len(msgc)) :
        msgdecrypte.append(chr(msgc[i]))
    return msg


p,q,n,pub,priv = key_creation()

def encryption(n,pub,msg) :
    e = pub[1]
    n = pub[0]
    msgc = convert_msg(msg)
    print(msgc)
    msgcrypt = []
    for i in range(len(msgc)):
        if msgc[i] < n :
            msgcrypt.append((msgc[i]^e)%n)
    return msgcrypt


print(convert_msg(msg))