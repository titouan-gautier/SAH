#### Import ####

import numpy as np


#### Programme qui convertit une matrice de 4 bit en 7 bit #### 

def matrice7(msg) :
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
    
    for i in range(len(msg)) :
        vect_msg.append([int(msg[i])])

    math = M@vect_msg
    
    for j,k in enumerate(math) :
        math[j] = k%2
        
    return math


#### Programme qui bruite une matrice de 7 bits ####

def noise(vect_msg):
    """
    prend un vecteur vect_msg et renvoie ce vecteur potentiellement bruite
    """
    ### on fait une copie du vecteur initial
    msg_noise = vect_msg.copy()
    ### une chance sur quatre de ne pas bruiter le vecteur
    test = np.random.randint(0,4)
    if test>0:
        index = np.random.randint(0,np.size(msg_noise))
        msg_noise[index] = (msg_noise[index] +1)%2
    return msg_noise


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


#### Variables ####

msg = [1,1,0,1]
vect_msg = matrice7(msg)
msg_noise = noise(vect_msg)
mfinal = denoise(msg_noise)


#### Print ####

print("Message de 4 bits :")
print(msg,"\n")
print("Message de 7 bits :")
print(vect_msg,"\n")
print("Message bruité :")
print(msg_noise,"\n")
print("Message débruité")
print(mfinal,"\n")

