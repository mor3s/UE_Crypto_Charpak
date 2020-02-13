# coding: utf-8


import os

with open("./Codes/message1.txt", 'r') as file:
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
            
M1(message)
#print(Scytale(message,1447))
class Transpose:
    """
    >>> Transpose(2)("abcd")
    'acbd'
    """
    def __init__(self, n: int):
        self.n: int = n

    def __call__(self, _in):
        _out = "".join([_in[i::self.n] for i in range(self.n)])
        return _out

#f = Transpose(1447)
#print(f(message))
