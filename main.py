# coding: utf-8
import os
from lib import *
from tqdm import tqdm

def test(code,method, n):
    for i in tqdm(range(1, n)):
        dc = method(code, i)
        if "Joël" in dc :
            f = open("D:/code/UE_Crypto_Charpak/message_decrypted.txt", "a")
            f.write(dc + "\n\n\n" +"-"*50 + "\n\n\n")
            f.close()
            print(dc)
            break


#scytale(read("D:/code/UE_Crypto_Charpak/Codes/message1.txt"),scytale ,len(read("D:/code/UE_Crypto_Charpak/Codes/message1.txt")))
#vigenere(read("D:/code/UE_Crypto_Charpak/Codes/message7.txt"),vigenere, 100)



