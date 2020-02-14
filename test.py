# coding: utf-8


import os

with open("./Codes/message4.txt", 'r') as file:
    # on fait des choses avec le fichier
    message = file.read() # chaîne de caractère avec le contenu du fichier
    # bla
# à partir d'ici, le fichier est fermé

codetest  = ['M', ' ', 'S', 'G', 'S', 'R', 'O', 'M', 'S', 'E', 'E', 'E', 'N', 'E', 'A', ' ', 'C', 'T']

def Scytale(code,p):
    d = []
    for i in range(p):
        for j in range(i, len(code), p):
            d.append(code[j])
    return ''.join(map(str, d)) 

def M1(code):
    for i in range(len(code)):
        dc = Scytale(code,i)
        if "Joël" in dc:
            f = open("message1_decrypted.txt", "a")
            f.write(dc + "\n\n\n-------------------------------------------------------------------------------------------------------------------\n\n\n")
            f.close()
            

def freq(code):
    dic = {"e":0}
    for i in range(len(code)):
        if code[i] not in dic:
            dic[code[i]] = 1
        else:
            dic[code[i]] += 1
    return dic

def Caesar(code,key):
    d = []
    for i in range(len(code)):
        d.append(chr((ord(code[i]) + key)%1000))      
    return ''.join(map(str, d)) 

def oddEven(code):
    odd = []
    even = []
    for i in range(len(code)):
        if i%2 == 0:
            odd.append(code[i])
        else:
            even.append(code[i])
    return odd, even

def M2(code):
    for i in range(200000):
        dc = Caesar(code,i)
        if "Joël" in dc:
            f = open("message3_decrypted.txt", "a")
            f.write(dc + "\n\n\n-------------------------------------------------------------------------------------------------------------------\n\n\n")
            f.close()
def M4(code):
    #pour l'ameliorer tester avant la freq de la lettre la plus probable et l'utiliser pour trouver la clé
    odd , even = oddEven(code)
    for i in range(2000):
        for j in range(2000):
            dc1 = list(Caesar(odd,i))
            dc2 = list(Caesar(even,j))
            dc = [] #contenu du message dechiffré
            for k in range(len(code)):
                if k%2 == 0  and len(odd)!=0:
                    dc.append(dc1[0])
                    dc1.pop(0)
                elif len(even) != 0 :
                    dc.append(dc2[0])
                    dc2.pop(0)
            dc = ''.join(map(str, dc)) 
            if "Joël" in dc:
                f = open("message4_decrypted.txt", "a")
                f.write(dc + "\n\n\n-------------------------------------------------------------------------------------------------------------------\n\n\n")
                f.close()
            if freq(dc1)["e"] > 10 and freq(dc2)["e"] > 10:
                for k in range(len(code)):
                    if k%2 == 0  and len(odd)!=0:
                        dc.append(dc1[0])
                        dc1.pop(0)
                    elif len(even) != 0 :
                        dc.append(dc2[0])
                        dc2.pop(0)
                dc = ''.join(map(str, dc)) 
                if "Joël" in dc:
                    f = open("message4_decrypted.txt", "a")
                    f.write(dc + "\n\n\n-------------------------------------------------------------------------------------------------------------------\n\n\n")
                    f.close()


def cut(code,p):
    d = []
    for i in range(p):
        tmp = []
        for j in range(i, len(code), p):
            tmp.append(code[j])
        d.append(tmp)
    return d

def glue(codes):
    d = []
    for i in range(len(codes[0])):
        for j in range(len(codes)):
            d.append(codes[j][i])
    return ''.join(map(str, d)) 


    