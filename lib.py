
# coding: utf-8
import os, operator


def read(adress = "D:/code/UE_Crypto_Charpak/Codes/message6.txt"):
    with open(adress, 'r', encoding='UTF-8') as file:
        message = file.read() 
    return message

#Complexity: O(n!n)
def scytale(code,key):
    """
    Cypher and decypher Scytale messages
    in : code (str/list) > message to cypher/decypher , key (int) 
    out : (str) > cyphered/decyphered message
    >>>scytale("MGOEN  SMEECSRSEAT", 2)
    "MON MESSAGE SECRET"
    """
    d = []
    for i in range(key):
        for j in range(i, len(code), key):
            d.append(code[j])
    return ''.join(map(str, d)) 


#Complexity: O(n)
def freq(code):
    """
    return a dic with the number of occurence of each char of the text given
    in : code (str/list) > text from wich you want to extract frequency
    out : dic (dic) > dic with the number of occurence of each char of the text given
    >>>freq("eeebaaa")
    {"e" : 3, "b" : 1, "a": 3}
    """
    dic = {"e": 0 } #initialise dic so it is not empty
    for i in range(len(code)):
        if code[i] not in dic:
            dic[code[i]] = 1
        else:
            dic[code[i]] += 1
    return dic


#Complexity: O(n)
def caesar(code,key):
    """
    cypher/decypher message using caesar methode
    in : code (str/list) > message to cypher/decypher , key (int) 
    out : (list) > cyphered/decyphered message
    >>>caesar("abc",2)
    ["c","d","e"]
    """
    d = []
    for i in range(len(code)):
        d.append(chr((ord(code[i]) + key)%1000))
    return d


#obsolete function
#Complexity: O(n)
def oddEven(code):
    """
    put each odd and even char into separate list
    in : code (str/list) > text from wich you want to extract odd and even char
    out : odd (list) > list containing only odd char, even (list) > list containing only even char
    >>>oddEven("ababab")
    ["a","a","a"], ["b","b","b"]
    """
    odd = []
    even = []
    for i in range(len(code)):
        if i%2 == 0:
            odd.append(code[i])
        else:
            even.append(code[i])
    return odd, even


#Complexity: O(n)
def cut(code,p):
    """
    cut message into p lists (extension of the "oddEven" function)
    in : code (str) > message you want to cut, p (int) number of list you want
    out : d (list of list) > list containing the p list you  just cut
    >>>cut("abcabcabc", 3)
    [["a","a","a"], ["b","b","b"],["c","c","c"]]
    """
    d = []
    for i in range(p):
        tmp = []
        for j in range(i, len(code), p):
            print(1)
            tmp.append(code[j])
        d.append(tmp)
    return d


#Complexity: O(n² log(n))
def glue(codes):
    """
    Reverse of cut function
    in : codes (list of list) > lists you want to glue
    out : (str) > message glued
    >>> m = [['a', 'a', 'a'], ['b', 'b', 'b']]
    >>>glue(m)
    "ababab"
    """
    d = []
    for i in range(round(sum(len(i) for i in codes)/len(codes))):
        for j in range(len(codes)):
            try:
                d.append(codes[j][i])
            except:
                pass
    return ''.join(map(str, d)) 

#Complexity: O(n^5 log n)
def vigenere(code, nb_cle):
    """
    Applie vigenere methode to cypher/decypher a message with vigenere methode
    in : code (str/list) > message to cypher/decypher , nb_cle (int) 
    out : (str) > cyphered/decyphered message
    >>> m = "ahahah"
    >>> vigenere(m, 2)
    "      "
    """
    d = []
    cuted = cut(code, nb_cle)
    for c in cuted:
        max_char = ord(max(freq(c).items(), key=operator.itemgetter(1))[0])
        guess =  ord(" ") - max_char 
        d.append(caesar(c, guess))
    return glue(d)




#ENIGMA 
# 
#    L'algorithme de chiffrement d'Enigma est un chiffre poly-alphabétique similaire au chiffre de Vigenère. Le mécanisme de la machine est basé sur plusieurs rotors
# (roues crantées mécaniques) qui effectuent chacune une permutation de l'alphabet (la permutation effectuée dépend de la position du rotor); le décalage obtenu
# en composant les permutations effectuées par chacun des rotors. A chaque frappe sur le clavier, les rotors tournent de la manière suivante : le rotor 1 tourne
# d'un cran à chaque frappe; à chaque tour complet du rotor 1, le rotor 2 tourne d'un cran; à chaque tour complet du rotor 2, le rotor 3 tourne d'un cran; à 
# chaque tour complet du rotor 3, le rotor 4 tourne d'un cran. La clé secrète de ce cryptosystème est la position initiale des rotors. Le nombre de positions 
# possibles des rotors est donc le produit du nombre de crans de chaque rotor. Ainsi, si chaque rotor possède n crans et qu'il y a m rotors, il faudra alors n^m
# frappes pour que les roues reviennent dans leur position initiale. Par exemples pour des machines Enigma de 3 roues à 26 cran, on a déjà 17576 positions des 
# rotors, ce qui empêche les attaques par analyse de fréquence auxquelles le chiffre de Vigenère était susceptible. Néanmoins 17576 reste une nombre raisonnablement
# petit pour des attaques par force brute (surtout de nos jours avec un ordinateur récent).
#
#   L'algorithme utilisé pour coder le message suivant s'inspire du principe général de la machine. Plutôt que d'utiliser de se limiter à l'alphabet à 26 lettres, nous 
# utilisons la table ASCII de 256 symbôles. Notre machine simulée utilise 3 roues qui effectuent des permutations sur l'ensemble de la table ASCII. La machine n'utilise
# pas de panneau de connexion (afin de simplifier), ni de réflecteur (afin de supprimer une faille d'Enigma). Les 3 rotors sont sélectionnées dans une liste de 8 rotors
# disponibles (numérotés 0 à 7) et mis dans un certain ordre et des positions initiales (chacune un entier entre 0 et 255).
#
# Une clé pour cette machine est donc constituée de :
#   - le choix des rotors, indiqués par leurs trois numéros. Par exemple :  4, 0, 1- la position initiale de chaque rotors. Par exemple :  123, 34, 231
#    
# On code ici un rotor par un tableau d'entiers x = [x0,x1,x2,...,x255]. L'effet du rotor est de chiffre le charactère ascii de numero i en entrée par le caractère ascii de numéro x[i] en sortie.


def initialise(gears,key):

    return gears


def rotate(gears):
    rotated_gears = gears
    return rotated_gears


def enigma(message, key):
    gears = [
        [211, 173, 77, 35, 89, 44, 92, 214, 80, 54, 3, 157, 191, 72, 16, 21, 200, 164, 202, 61, 31, 34, 129, 68, 63, 43, 232, 136, 87, 197, 251, 74, 250, 1, 193, 104, 47, 10, 110, 160, 188, 124, 153, 171, 170, 6, 206, 161, 152, 96, 40, 62, 172, 144, 175, 168, 123, 38, 18, 242, 79, 53, 228, 48, 186, 184, 210, 140, 162, 143, 253, 150, 235, 145, 45, 91, 134, 248, 5, 90, 59, 75, 84, 249, 127, 76, 132, 66, 165, 57, 128, 217, 33, 11, 100, 203, 26, 121, 213, 247, 216, 199, 46, 114, 154, 101, 0, 115, 105, 4, 155, 187, 130, 147, 12, 41, 149, 219, 239, 107, 56, 39, 69, 70, 238, 234, 158, 15, 19, 196, 221, 236, 86, 65, 243, 231, 98, 182, 51, 177, 28, 71, 169, 241, 222, 117, 178, 112, 131, 167, 111, 141, 205, 25, 183, 229, 230, 122, 208, 135, 245, 113, 24, 223, 201, 13, 190, 64, 156, 106, 94, 185, 93, 126, 254, 212, 109, 81, 240, 237, 224, 218, 17, 215, 176, 194, 226, 220, 166, 83, 50, 73, 225, 118, 20, 108, 36, 14, 138, 244, 78, 67, 174, 8, 95, 159, 116, 37, 32, 2, 133, 139, 85, 227, 9, 179, 255, 102, 97, 233, 27, 42, 82, 195, 55, 246, 252, 30, 189, 207, 198, 58, 99, 7, 103, 163, 60, 120, 137, 142, 125, 22, 181, 209, 119, 23, 180, 88, 204, 52, 29, 146, 49, 148, 192, 151],
        [70, 36, 41, 129, 87, 233, 155, 96, 185, 204, 65, 80, 137, 221, 89, 167, 220, 58, 131, 23, 20, 237, 132, 53, 15, 180, 85, 195, 38, 149, 72, 218, 173, 120, 123, 110, 94, 81, 148, 127, 77, 251, 62, 56, 230, 44, 34, 71, 136, 54, 166, 236, 21, 108, 249, 29, 223, 106, 12, 18, 217, 184, 203, 210, 39, 60, 78, 152, 197, 244, 189, 206, 143, 156, 27, 7, 103, 198, 107, 145, 69, 135, 182, 164, 74, 10, 202, 99, 111, 224, 199, 196, 254, 215, 250, 97, 178, 101, 47, 208, 19, 227, 33, 248, 43, 128, 64, 40, 109, 162, 1, 138, 86, 134, 46, 207, 95, 122, 79, 126, 9, 209, 90, 124, 214, 246, 228, 229, 37, 200, 0, 76, 13, 133, 98, 165, 187, 91, 179, 193, 172, 48, 157, 114, 175, 168, 255, 8, 66, 75, 125, 57, 102, 51, 119, 240, 118, 211, 243, 11, 88, 235, 216, 141, 183, 159, 55, 24, 150, 192, 194, 6, 231, 28, 100, 219, 68, 144, 186, 82, 139, 73, 130, 176, 161, 245, 45, 63, 61, 239, 14, 117, 4, 234, 190, 42, 242, 169, 59, 163, 17, 121, 147, 154, 112, 225, 191, 35, 52, 116, 22, 212, 142, 232, 188, 151, 158, 174, 226, 32, 238, 140, 5, 25, 213, 253, 252, 205, 83, 105, 67, 201, 3, 104, 31, 146, 93, 16, 92, 171, 49, 50, 2, 170, 241, 181, 153, 160, 247, 177, 30, 115, 113, 26, 84, 222],
        [7, 106, 109, 229, 172, 34, 253, 174, 130, 14, 99, 107, 157, 79, 30, 147, 39, 19, 35, 24, 47, 205, 124, 67, 136, 246, 27, 237, 149, 142, 55, 245, 105, 21, 74, 101, 91, 10, 120, 137, 233, 8, 72, 73, 1, 119, 122, 20, 100, 251, 203, 85, 81, 153, 150, 83, 127, 50, 48, 144, 197, 70, 133, 210, 234, 227, 179, 68, 219, 71, 76, 173, 22, 167, 90, 190, 58, 64, 60, 244, 5, 28, 95, 63, 159, 195, 140, 236, 56, 115, 193, 65, 213, 89, 239, 145, 108, 23, 97, 6, 61, 25, 31, 228, 254, 231, 206, 164, 217, 32, 148, 232, 126, 141, 16, 11, 77, 188, 112, 154, 138, 255, 57, 135, 146, 88, 3, 121, 224, 223, 160, 152, 215, 46, 62, 132, 249, 111, 176, 170, 184, 93, 202, 103, 104, 87, 177, 86, 118, 171, 41, 165, 155, 230, 44, 175, 15, 163, 13, 98, 180, 94, 226, 114, 194, 207, 26, 162, 178, 9, 182, 183, 216, 143, 123, 196, 158, 169, 218, 186, 38, 116, 51, 204, 29, 198, 250, 185, 80, 12, 211, 191, 78, 125, 161, 208, 54, 200, 247, 17, 168, 252, 37, 166, 0, 181, 242, 187, 139, 241, 151, 53, 201, 36, 243, 214, 238, 43, 192, 220, 18, 225, 113, 134, 45, 129, 96, 40, 156, 248, 84, 75, 209, 235, 52, 42, 92, 240, 110, 4, 189, 66, 49, 221, 117, 199, 102, 59, 82, 128, 212, 33, 2, 222, 131, 69],
        [24, 210, 76, 63, 167, 40, 13, 203, 90, 34, 102, 163, 15, 230, 100, 182, 179, 31, 58, 255, 57, 0, 122, 137, 104, 98, 231, 26, 70, 254, 33, 4, 1, 88, 206, 28, 65, 125, 164, 93, 186, 187, 16, 223, 87, 127, 64, 123, 101, 99, 83, 154, 66, 191, 121, 29, 218, 174, 138, 77, 142, 9, 194, 132, 247, 215, 89, 113, 107, 216, 196, 162, 43, 32, 213, 151, 190, 81, 124, 69, 169, 112, 176, 59, 51, 165, 68, 193, 80, 141, 156, 211, 135, 120, 208, 160, 228, 140, 35, 12, 25, 229, 147, 38, 133, 131, 168, 92, 245, 62, 157, 114, 67, 136, 202, 242, 105, 6, 42, 48, 253, 184, 204, 61, 241, 220, 161, 158, 39, 183, 198, 18, 209, 119, 172, 175, 106, 221, 177, 235, 11, 27, 94, 170, 181, 129, 30, 188, 19, 47, 7, 199, 145, 139, 23, 74, 91, 71, 95, 244, 224, 152, 53, 75, 251, 201, 45, 10, 17, 200, 207, 195, 5, 116, 236, 166, 60, 205, 14, 72, 185, 2, 49, 130, 79, 3, 178, 149, 180, 134, 252, 86, 148, 243, 20, 238, 85, 37, 155, 82, 197, 84, 217, 171, 212, 246, 21, 227, 111, 54, 55, 240, 219, 143, 225, 97, 233, 128, 234, 36, 73, 44, 249, 150, 117, 248, 126, 214, 46, 108, 118, 22, 250, 52, 153, 232, 78, 56, 96, 159, 222, 8, 103, 144, 146, 239, 189, 50, 41, 226, 110, 237, 192, 173, 115, 109],
        [179, 102, 107, 105, 6, 147, 40, 66, 8, 160, 89, 116, 126, 244, 176, 118, 167, 57, 86, 163, 17, 70, 1, 157, 231, 219, 187, 191, 196, 58, 199, 141, 183, 59, 100, 53, 43, 148, 245, 54, 65, 158, 241, 227, 60, 82, 52, 5, 72, 139, 207, 228, 90, 161, 20, 4, 31, 75, 96, 240, 106, 251, 37, 223, 128, 62, 94, 42, 190, 173, 172, 47, 101, 35, 152, 236, 119, 92, 253, 204, 93, 229, 188, 115, 230, 64, 117, 211, 136, 169, 170, 249, 175, 131, 88, 24, 14, 224, 125, 193, 138, 233, 248, 95, 22, 151, 28, 71, 41, 25, 132, 174, 255, 87, 239, 149, 130, 153, 69, 155, 192, 171, 74, 9, 112, 56, 83, 232, 39, 144, 97, 21, 242, 2, 213, 79, 78, 68, 111, 225, 7, 142, 80, 146, 206, 134, 137, 0, 30, 216, 184, 209, 98, 33, 217, 159, 198, 124, 122, 91, 135, 210, 23, 181, 154, 182, 252, 76, 156, 189, 77, 49, 61, 16, 12, 104, 45, 15, 11, 195, 178, 18, 208, 113, 127, 212, 34, 38, 108, 254, 203, 50, 166, 238, 202, 150, 3, 214, 200, 143, 63, 32, 205, 109, 44, 129, 13, 27, 180, 215, 48, 145, 140, 162, 234, 84, 36, 243, 221, 26, 19, 29, 120, 67, 168, 226, 177, 218, 73, 237, 103, 247, 81, 194, 10, 165, 110, 114, 121, 164, 250, 197, 133, 85, 186, 235, 51, 46, 246, 185, 201, 55, 222, 123, 99, 220],
        [7, 188, 27, 179, 50, 254, 167, 117, 35, 149, 89, 81, 186, 39, 133, 28, 83, 112, 249, 165, 31, 194, 86, 237, 64, 203, 45, 241, 6, 226, 156, 171, 172, 43, 200, 41, 24, 90, 131, 122, 127, 232, 168, 180, 139, 78, 108, 0, 22, 94, 107, 162, 14, 59, 175, 84, 98, 132, 251, 46, 116, 70, 99, 29, 74, 135, 182, 44, 15, 192, 229, 138, 201, 198, 79, 92, 77, 69, 208, 75, 253, 148, 109, 134, 174, 96, 34, 5, 93, 151, 185, 189, 164, 8, 72, 227, 114, 20, 106, 142, 231, 103, 204, 129, 244, 19, 217, 25, 80, 71, 145, 23, 17, 178, 221, 169, 88, 214, 215, 219, 32, 143, 230, 42, 195, 177, 255, 121, 85, 36, 157, 183, 225, 222, 216, 181, 144, 191, 193, 212, 243, 202, 250, 38, 110, 58, 209, 240, 111, 205, 224, 223, 37, 82, 245, 115, 21, 102, 128, 210, 239, 68, 147, 234, 54, 52, 206, 238, 176, 100, 53, 137, 118, 40, 184, 155, 4, 220, 199, 247, 150, 57, 30, 48, 10, 26, 236, 197, 158, 130, 2, 63, 55, 166, 16, 124, 228, 60, 95, 65, 153, 213, 190, 163, 126, 97, 62, 161, 141, 123, 104, 207, 76, 3, 125, 218, 146, 91, 140, 9, 196, 119, 47, 235, 12, 1, 11, 105, 18, 173, 13, 154, 51, 152, 67, 160, 248, 33, 73, 211, 66, 242, 56, 61, 170, 233, 187, 252, 120, 136, 87, 49, 113, 246, 159, 101],
        [106, 72, 252, 44, 50, 129, 83, 110, 116, 119, 183, 182, 202, 22, 100, 225, 228, 181, 126, 26, 130, 36, 78, 209, 164, 5, 59, 43, 82, 24, 174, 138, 150, 97, 180, 233, 84, 235, 237, 96, 28, 221, 109, 159, 142, 132, 111, 128, 205, 11, 55, 191, 62, 115, 87, 18, 239, 224, 108, 139, 77, 135, 167, 219, 34, 112, 215, 236, 158, 151, 105, 157, 89, 155, 49, 67, 136, 131, 14, 52, 127, 73, 208, 211, 234, 216, 196, 254, 71, 137, 41, 51, 147, 247, 107, 161, 251, 194, 162, 39, 58, 175, 133, 206, 120, 184, 192, 232, 88, 148, 94, 91, 45, 176, 60, 122, 144, 65, 203, 198, 156, 1, 117, 10, 85, 160, 134, 190, 3, 32, 226, 249, 80, 21, 231, 223, 230, 118, 61, 48, 19, 171, 35, 245, 213, 4, 253, 57, 66, 165, 0, 244, 76, 204, 199, 143, 74, 125, 113, 99, 30, 248, 218, 47, 40, 163, 177, 20, 69, 93, 121, 27, 255, 238, 246, 222, 166, 200, 217, 29, 90, 68, 124, 243, 152, 146, 141, 12, 70, 170, 33, 86, 197, 63, 104, 229, 242, 186, 114, 101, 227, 95, 16, 212, 220, 201, 64, 98, 46, 240, 42, 2, 102, 38, 179, 9, 75, 189, 178, 154, 53, 241, 250, 37, 140, 8, 13, 145, 149, 31, 210, 25, 153, 17, 123, 185, 103, 168, 56, 173, 79, 188, 7, 92, 172, 54, 169, 193, 187, 214, 81, 207, 15, 195, 6, 23],
        [215, 216, 89, 97, 48, 193, 179, 241, 131, 172, 17, 102, 107, 10, 2, 121, 153, 164, 175, 143, 43, 203, 122, 134, 126, 64, 132, 23, 79, 250, 53, 152, 83, 56, 58, 184, 211, 69, 86, 19, 112, 162, 37, 125, 156, 151, 123, 109, 44, 88, 42, 251, 174, 142, 199, 113, 26, 163, 210, 65, 117, 232, 141, 50, 106, 15, 252, 81, 165, 119, 249, 66, 243, 205, 104, 240, 234, 183, 192, 130, 227, 185, 3, 39, 74, 145, 24, 35, 32, 218, 182, 148, 78, 129, 76, 248, 6, 140, 133, 136, 59, 194, 173, 25, 30, 222, 186, 105, 57, 158, 63, 84, 223, 157, 114, 159, 221, 92, 235, 9, 45, 225, 101, 54, 146, 49, 244, 36, 99, 233, 238, 47, 237, 91, 67, 128, 189, 100, 209, 188, 80, 93, 254, 161, 155, 41, 177, 33, 21, 85, 217, 51, 170, 62, 77, 70, 96, 168, 4, 94, 11, 61, 214, 0, 14, 231, 195, 190, 87, 7, 71, 207, 60, 236, 230, 180, 137, 213, 191, 68, 72, 197, 29, 147, 115, 187, 46, 12, 181, 38, 138, 246, 124, 166, 40, 27, 202, 201, 226, 176, 212, 204, 52, 149, 167, 196, 34, 220, 28, 98, 228, 13, 90, 224, 169, 135, 20, 16, 229, 75, 55, 154, 82, 150, 160, 198, 255, 1, 95, 118, 206, 120, 242, 116, 200, 110, 103, 22, 111, 178, 171, 5, 245, 139, 18, 253, 247, 31, 108, 208, 127, 8, 144, 239, 73, 219]
    ]

#3 roues défini
#prend 1 char qu'on veut coder

