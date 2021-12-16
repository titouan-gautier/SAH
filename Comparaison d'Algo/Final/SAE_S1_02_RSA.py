## Import ##

import random

## Message ##

msg = "hello world"

## Question 1.1 ##

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
    return liste[25:]

## Question 1.2 ##

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

## Question 1.3 ##

def key_creation() :
    p = random.choice(list_prime(2000))
    q = random.choice(list_prime(2000))
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
    return n,pub,priv

## Question 1.4 ##

    # Convertir le message en code ASCII #

def convert_msg(msg) :
    msgcrypte = ""
    car = ""
    
    for i in range(len(msg)) :
        car = str(ord(msg[i]))
        if len(car) != 3 :
            car = "0" + car
        msgcrypte += car
    

    while (len(msgcrypte) % 4) != 0 :
        msgcrypte = "0"+msgcrypte
    
    
    msgcrypte2 = []
    while len(msgcrypte) != 0:
        msgcrypte2.append(msgcrypte[:4])
        msgcrypte = msgcrypte[4:]
    
    return msgcrypte2

    # Encrypter le msg #

def encryption(n,pub,msg) :
    msgconvert = convert_msg(msg)
    e = pub[1]
    n = pub[0]
    msgc = []
    for i in msgconvert:
        msgc.append(pow(int(i),e,n))
    return msgc

## Question 1.5 ##

    # Décrypter le message #

def decryption(n,priv,msgc):
    d = priv[1]
    msgd = []
    a = ""
    for i in msgc :
        a = str(pow(i,d,n))
        while len(a) < 4 :
            a = "0" + a
        msgd.append(a)
    
    return msgd

    # Convertir le code ASCII en message #

def convert_inverse(msgd):
    msgdecrypte = ""
    msgdecryptefin = ""
    count = 0

    for i in range(len(msgd)):
        msgdecrypte += str(msgd[i])
    
    while msgdecrypte[count] == "0" :
        count = count + 1

    if len(msgdecrypte[count:]) % 3 == 0 :
        msgdecrypte = msgdecrypte[count:]
    else :
        msgdecrypte = msgdecrypte[count-1:]

    while len(msgdecrypte) != 0 :
        part = msgdecrypte[:3]
        msgdecryptefin += str(chr(int(part)))
        msgdecrypte = msgdecrypte[3:] 
        part = ""
    return msgdecryptefin

## Variables ##

n,pub,priv = key_creation()
msgc = encryption(n,pub,msg)
msgd = decryption(n,priv,msgc)

## Print ##

print(convert_msg(msg))
print(encryption(n,pub,msg))
print(decryption(n,priv,msgc))
print(convert_inverse(msgd))