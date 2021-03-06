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

msg = "salut gros bg comment vas-tu? Moi ça va je m'appelle jules, je suis à l'iut du centre de nantes et j'ai fait un programme avec titouan pour crypter et decrypter des messages. C'est super cela marche tres bien je suis content et je vai reussir mon année avec succès grace a mes effort acharné"

def convert_msg(msg) :
    msgcrypte = ""
    
    for i in range(len(msg)) :
        msgcrypte += str(ord(msg[i]))
    
    while len(msgcrypte)%4 !=0 :
        msgcrypte = "0" + msgcrypte

    msgcryptefin = []

    while len(msgcrypte) != 0 :
        msgcryptefin.append(msgcrypte[:4])
        msgcrypte = msgcrypte[4:]
    return msgcryptefin

p,q,n,pub,priv,fiN = key_creation()


def encryption(n,pub,msg) :
    msgconvert = convert_msg(msg)
    e = pub[1]
    n = pub[0]
    msgc = []
    for i in msgconvert:
        msgc.append((int(i)**e)%n)
    return msgc

msgc = encryption(n,pub,msg)

def decryption(n,priv,msgc):
    d = priv[1]
    msgf = []
    for i in msgc : 
        msgf.append((i**d)%n)
    return msgf

#print(convert_msg(msg))
print(encryption(n,pub,msg))
#print(decryption(n,priv,msgc))
msgf = decryption(n,priv,msgc)

def deconvert_msg(msgf) :
    msgdecrypte = []
    while len(msgf) != 0 :
        msgdecrypte.append(msgf[:3])
        msgf = msgf[3:]
    return msgdecrypte

""" print(decryption(n,priv,msgc))
print(deconvert_msg(msgf))
 """

""" Tout mettre en un string pour tous redecouper en paquet de 3 """