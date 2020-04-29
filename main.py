# coding: utf-8
import os
from lib import *
from tqdm import tqdm

# Vigenere complexity : O(n^3 log(n) + n^3 + n^2 + n)
# Cesar complexity : O(n²n! + n) 

def auto_decipher(code, n):
    if max(freq(code).items(), key=operator.itemgetter(1))[0] == ' ':
        method = scytale
    else:
        method = vigenere
    print(method)
    for i in tqdm(range(1, n)):
        dc = method(code, i)
        if "Joël" in dc :   # Choose a word wich could the most probably appear in the message
            f = open("D:/code/UE_Crypto_Charpak/message_decrypted.txt", "a", encoding='UTF-8')
            f.write(dc)
            f.close()
            print(dc)
            break



def decipher(code,method, n):
    for i in tqdm(range(1, n)):
        dc = method(code, i)
        if "Joël" in dc :   # Choose a word wich could the most probably appear in the message
            f = open("D:/code/UE_Crypto_Charpak/message_decrypted.txt", "a")
            f.close()
            print(dc)
            break


#decipher(read("D:/code/UE_Crypto_Charpak/Codes/message1.txt"),scytale ,len(read("D:/code/UE_Crypto_Charpak/Codes/message1.txt")))
#decipher(read("D:/code/UE_Crypto_Charpak/Codes/message7.txt"),vigenere, 100)

#auto_decipher(read("D:/code/UE_Crypto_Charpak/Codes/message1.txt") ,len(read("D:/code/UE_Crypto_Charpak/Codes/message1.txt")))
#auto_decipher(read("D:/code/UE_Crypto_Charpak/Codes/message7.txt"), 100)




