

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
        d.append(chr((ord(code[i]) + key)))
    return d


#obsolete function
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
            tmp.append(code[j])
        d.append(tmp)
    return d



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


def vigcle(code, nb_cle):
    """
    Applie vigenere methode to cypher/decypher a message with vigenere methode
    in : code (str/list) > message to cypher/decypher , nb_cle (int) 
    out : (str) > cyphered/decyphered message
    >>> m = "ahahah"
    >>> vigcle(m, 2)
    "      "
    """
    d = []
    cuted = cut(code, nb_cle)
    for c in cuted:
        max_char = ord(max(freq(c).items(), key=operator.itemgetter(1))[0])
        guess =  ord(" ") - max_char 
        d.append(caesar(c, guess))
    return glue(d)