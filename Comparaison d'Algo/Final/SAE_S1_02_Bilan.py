#### Import ####

import random
import numpy as np

#### Message ####

msg = "bonjour, ce message va etre converti e ascii puis crypter puis binariser puis bruiter puis debruiter puis debinariser puis dechiffrer puis mis en caractère "


#### Fonction qui donne une liste de nombre premier de 25 à n. ####

def list_prime(x):
    i = 1
    liste = []
    for k in range(1, (x+1), 1):
        c = 0
        for j in range(1, (i+1), 1):
            a = i % j
            if (a == 0):
                c = c+1

        if (c == 2):
            liste.append(i)
        else:
            k = k-1
        i = i+1
    return liste[25:]


#### Fonction qui code l'algorithme d'Euclide étendu ####

def extended_gcd(a, b):
    if a < b:
        a, b = b, a
    u0, u1 = 1, 0
    v0, v1 = 0, 1
    while b != 0:
        q = int(a/b)
        b, a = a % b, b
        u0, u1, v0, v1 = v0, v1, u0-q*v0, u1-q*v1
    return a, u0, u1


#### Fonction qui créer la clé privée et publique ####

def key_creation():
    p = random.choice(list_prime(1000))
    q = random.choice(list_prime(1000))
    n = p*q
    fiN = (p-1)*(q-1)
    e = 2
    a = 0
    d = 2
    res = 0
    while a != 1:
        a, u0, u1 = extended_gcd(e, fiN)
        if a != 1:
            e = e + 1
        pub = (n, e)

    while res != 1:
        res = (e*d) % fiN
        d = d + 1
    priv = (n, d-1)
    return n, pub, priv


#### Fonction qui converti notre message en code ASCII ####

def convert_msg(msg):
    msgcrypte = ""
    car = ""

    for i in range(len(msg)):
        car = str(ord(msg[i]))
        if len(car) != 3:
            car = "0" + car
        msgcrypte += car

    while (len(msgcrypte) % 4) != 0:
        msgcrypte = "0"+msgcrypte

    msgcrypte2 = []
    while len(msgcrypte) != 0:
        msgcrypte2.append(msgcrypte[:4])
        msgcrypte = msgcrypte[4:]

    return msgcrypte2

    
#### Fonction qui encrypte notre message ####

def encryption(n, pub, msg):
    msgconvert = convert_msg(msg)
    e = pub[1]
    n = pub[0]
    msgc = []
    temp = ""
    for i in msgconvert:
        temp = pow(int(i), e, n)
        while len(str(temp)) != len(str(n)) :
            temp = "0" + str(temp)
        msgc.append(temp)

    msgcv = ""

    for i in msgc :
        msgcv += str(i)
    return msgcv
    

#### Fonction qui transforme notre message crypter en binaire ####

def binaire (msgl) :
    msgbin = bin(int(msgl))
    part = []
    binmid = []
    
    tab = msgbin.split('b')
    strbin = tab[1]
    while len(strbin) != 0 :
        part = strbin[:1]
        binmid.append(int(part))
        strbin = strbin[1:]
        part = ""
    
    binfin = []

    for i in range(int(len(binmid)/4)):
        binfin.append(binmid[:4])
        binmid = binmid[4:]

    return binfin


#### Programme qui convertit notre message binaire en tableau de matrice ####

def tabmatrice(msgbin) :
    vect_msg = []
    
    for i in msgbin :
        vect_msg.append(matrice(i))  
    
    return vect_msg


#### Programme qui convertit une matrice de 4 bit en 7 bit ####

def matrice(msgbin) :
    
    M = np.array([
        [1,1,0,1],
        [1,0,1,1],
        [1,0,0,0],
        [0,1,1,1],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,1]
        ])
    
    vect_msg = []
    
    for i in range(len(msgbin)) :
        vect_msg.append([(msgbin[i])])

    math = M@vect_msg
    
    for j,k in enumerate(math) :
        math[j] = k%2
        
    return math


#### Programme qui bruite notre tableau de matrice ####

def tabnoise(vect_msg) :

    tnoise =[]

    for i in vect_msg :
        tnoise.append(noise(i))

    return tnoise


#### Programme qui bruite une matrice de 7 bits ####

def noise(vect_msg):
    ### on fait une copie du vecteur initial
    msg_noise = vect_msg.copy()
    ### une chance sur quatre de ne pas bruiter le vecteur
    test = np.random.randint(0,4)
    if test>0:
        index = np.random.randint(0,np.size(msg_noise))
        msg_noise[index] = (msg_noise[index] +1)%2
    
    return msg_noise


#### Programme

def tabledenoise(msg_noise) :

    tdenoise = []
    for i in msg_noise:
        tdenoise.append(denoise(i))

    return tdenoise


#### Programme qui retire le bruit d'une matrice de 7 bits ####

def denoise(msg_noise) :
    
    mat16 = np.array([
        [0,0,0,0,0,0,0],
        [1,1,0,1,0,0,1],
        [0,1,0,1,0,1,0],
        [1,0,0,0,0,1,1],
        [1,0,0,1,1,0,0],
        [0,1,0,0,1,0,1],
        [0,0,1,1,0,0,1],
        [0,0,0,1,1,1,1],
        [1,1,1,0,0,0,0],
        [1,1,0,0,1,1,0],
        [1,0,1,1,0,1,0],
        [0,1,1,0,0,1,1],
        [0,1,1,1,1,0,0],
        [1,0,1,0,1,0,1],
        [0,0,1,0,1,1,0],
        [1,1,1,1,1,1,1],
    ])

    for m in mat16 :
        
        msgcomp = []
        
        for i in range(7):
            msgcomp.append(msg_noise[i] + (m[i] % 2))
            
        c = 0
        
        for j in msgcomp :
            if j == 1 :
                c = c + 1
        if c == 0 or c == 1 :
            return str(m[2]) + str(m[4]) + str(m[5]) + str(m[6])
 

#### Fonctions qui transforme notre message bianire en décimal ####

def debin(mfinal) :
    
    strm =""

    for i in mfinal :
        strm += str(i)

    strm = "0b" + strm
    
    msgl = int(strm,2)

    return msgl


#### Fonctions qui décrypte notre message ####

def decryption(n, priv, msgl):
    
    length = len(str(n))
    msg = str(msgl)
    while len(msg) % length != 0 :
        msg = "0" + msg
    
    part = ""
    msgd = []

    while len(msg) != 0 :
        part = msg[:length]
        msgd.append(int(part))
        msg = msg[length:]
        part= ""

    d = priv[1]
    msg = []
    a = ""
    for i in msgd:
        a = str(pow(i, d, n))
        while len(a) < 4:
            a = "0" + a
        msg.append(a)
    
    msgdv =""

    for i in msg :
        msgdv += str(i)

    return msgdv


#### Fonction qui transforme notre message ASCII en caractère ##

def convert_inverse(msgdv):
    msgdecrypte = ""
    msgdecryptefin = ""
    count = 0

    msgdecrypte = msgdv

    while msgdecrypte[count] == "0":
        count = count + 1

    if len(msgdecrypte[count:]) % 3 == 0:
        msgdecrypte = msgdecrypte[count:]
    else:
        msgdecrypte = msgdecrypte[count-1:]

    while len(msgdecrypte) != 0:
        part = msgdecrypte[:3]
        msgdecryptefin += str(chr(int(part)))
        msgdecrypte = msgdecrypte[3:]
        part = ""
    
    msgfin = msgdecryptefin
    
    return msgfin


#### Variables ####

n, pub, priv = key_creation()
msgconvert = convert_msg(msg)
msgc = encryption(n, pub, msg)
msgbin = binaire(msgc)

vect_msg = tabmatrice(msgbin)
msg_noise = tabnoise(vect_msg)
mfinal = tabledenoise(msg_noise)
msgl = debin(mfinal)

msgdv = decryption(n,priv,msgl)
msgfin = convert_inverse(msgdv)


#### Print ####

print("Message envoyé :")
print(msg,"\n")
print("Message converti en code ASCII :")
print(msgconvert,"\n")
print("Message crypté :")
print(msgc,"\n")
print("Message converti en binaire :" ,)
print(msgbin,"\n")
""" print("Message sous forme de tableau de matrice de 7 bits :")
print(vect_msg,"\n")
print("Message bruité :")
print(msg_noise,"\n")
print("Message debruité :")
print(mfinal,"\n") """
print("Debin :",)
print(msgl,"\n")
print("Decryptr :")
print(msgdv,"\n")
print("Deconvert :")
print(msgfin,"\n")