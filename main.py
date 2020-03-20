# coding: utf-8
import os
from lib import *
from tqdm import tqdm


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





