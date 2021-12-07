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
    return p,q,n,pub,priv,fiN

msg = "salut gros bg comment vas-tu?"

def convert_msg(msg) :
    msgcrypte = ""
    car = 0
    for i in range(len(msg)) :
        car = str(ord(msg[i]))
        if len(str(car)) <= 2 :
            msgcrypte += "0" + str(ord(msg[i]))
        else :
            msgcrypte += str(ord(msg[i]))
    while len(msgcrypte)%4 !=0 :
        msgcrypte = "0" + msgcrypte
    return msgcrypte

p,q,n,pub,priv,fiN = key_creation()


def encryption(n,pub,msg) :
    msgconvert = convert_msg(msg)
    e = pub[1]
    n = pub[0]
    msgc = []
    for i in msgconvert:
        msgc.append((int(i)**e)%n)
    return msgc

""" print(encryption(n,pub,msg)) """
""" print(p,q,n,pub,priv,fiN) """
msgc = encryption(n,pub,msg)

def decryption(n,priv,msgc):
    d = priv[1]
    msgf = []
    for i in msgc : 
        msgf.append((i**d)%n)
    return msgf 

msgf = decryption(n,priv,msgc)

def convert_inverse(msgf):
    for e in msgf :
        msgdecrypte = "".join(str(i) for i in msgf)
        e = e + 1 


    msgdecryptefin = ""
    part = ""
    while msgdecrypte[0] == "0" : 
        msgdecrypte = msgdecrypte[1:]
    while len(msgdecrypte) != 0 :
        part = msgdecrypte[:3]
        msgdecryptefin += str(chr(int(part)))
        msgdecrypte = msgdecrypte[3:] 
        part = ""
    return msgdecryptefin          

print(convert_inverse(msgf))