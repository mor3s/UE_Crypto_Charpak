# coding: utf-8


import os, operator, lib

#with open("./Codes/message6.txt", 'r') as file:
    # on fait des choses avec le fichier
    #message = file.read() # chaîne de caractère avec le contenu du fichier
    # bla
# à partir d'ici, le fichier est fermé

codetest  = ['M', ' ', 'S', 'G', 'S', 'R', 'O', 'M', 'S', 'E', 'E', 'E', 'N', 'E', 'A', ' ', 'C', 'T']

print(lib.caesar("abc", 2))

def m1(code):
    for i in range(len(code)):
        dc = scytale(code,i)
        if "Joël" in dc:
            f = open("message1_decrypted.txt", "a")
            f.write(dc + "\n\n\n-------------------------------------------------------------------------------------------------------------------\n\n\n")
            f.close()
            

def m2(code):
    for i in range(200000):
        dc = caesar(code,i)
        if "Joël" in dc:
            f = open("message3_decrypted.txt", "a")
            f.write(dc + "\n\n\n-------------------------------------------------------------------------------------------------------------------\n\n\n")
            f.close()

def m4(code):
    #pour l'ameliorer tester avant la freq de la lettre la plus probable et l'utiliser pour trouver la clé
    odd , even = oddEven(code)
    for i in range(2000):
        for j in range(2000):
            dc1 = list(caesar(odd,i))
            dc2 = list(caesar(even,j))
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






def vigenere(code):
    for i in range(1, 51):
        dc = vigcle(code, i)
        if "Joël" in dc:
            f = open("message6_decrypted.txt", "a")
            f.write(dc + "\n\n\n" +"-"*50 + "\n\n\n")
            f.close()
            print("wiiin")
            # return
            
#Vigenere(message)