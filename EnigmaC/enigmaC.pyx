#ENIGMA
import itertools





def initialise(gears,key):
    gearspicked = []
    for i in range(3):
        gearspicked.append(rotate(gears[key[0][i]], key[1][i]))
    return gearspicked

  
def rotate(position, angle, radius = 256):
    pos = position[:] # copie
    retenue = angle
    for i in range(len(pos)):
        pos[i] += retenue
        pos[i], retenue = pos[i] % radius, pos[i] // radius
    return pos

def encode_chr(c, gears, position, radius = 256, sens = 1):
    x = ord(c)
    for i in range(len(position)) if sens > 0 else range(len(position)-1, -1, -1):
        x = (gears[i][(x + position[i]) % radius] - position[i]) % radius
    return chr(x)


def encode(txt, gears, position, radius = 256, sens = 1):
    encoded = ""
    for i in range(len(txt)):
        encoded += encode_chr(txt[i], gears, position, radius, sens)
        position = rotate(position, 1,radius)
    return encoded

def invert(gears):
    T = []
    for gear in gears:
        g = gear[:]
        for i in range(len(gear)):
            g[gear[i]] = i
        T.append(g)
    return T


def enigma(message,gears, key = [[0,1,3], [0,0,0]], radius = 256, sens = 1):
    gearspicked = initialise(gears,key)
    encoded = encode(message, gearspicked, key[1], radius, sens)
    return encoded


# test_chiffre = '#¨à\r\x7f\x87\x1aå\x02¯höÝÃ\x95E&{\n«\x1fAr²i*%¥¿¾¬B\x9aZVä\x9cB}\x0f6\n\x8b_}È¥Å\x98¨sáº\x07¤\n\x04\x8bbúç\x82v¾Û«¢2\x9d\x07²\x17\x80xr\x98«8ëy5¬wÏ\x80-èW½¿D®úH\x89N×\x8bY\x87bþî\n\x0c\n-èX`ÿDac\x03Ø3E©¬>:\x1d\x08±\x1b\x05¦2ûÈ$u\x16ÆÄû)ãmM\x0cVu*ÀÐÃäÆ\x8d@y!;\x00[¼\x85¡F\x14vx\n\x9ehN{xìUpm>Ä®\x84eØ*ä\x91¶\xa0Æ"\x97\x98i³\x0e\x03½P6åN§\x7f\x1fÞ\x15¸16YH\x95þå\x9f¿\x1d.OB\x05\x16\x85-\x88= ¶=ª\x894gÂm\x12û&\x8fo\x16Zã\x83»GaS\x01°\x94òî8À6«\x08\x18\x10â.i\x7f×©\x16·\x1c\x8bÉúç\nðµÛ¬æ±£\x99\x83\x84J\x9eÊ¿\x0c\x94&\'5gx\x8d\x89¢\x1b\x8dÚn\x99hÕ©øäñð·³_\x19¿¥eÀc¥°Ö\x87\xa0\x0bá\x16ökZ¼\x95v\x08\x19\x7f´þ\x83MO\x85\x9fÂìpÛ\x8a\x81\x04\x06\t´\x90âÀ²EÕ\x96ª\x19\x11_\x879Z\x82Ç\xadúo\x06\x9fTÄjïµ\x1c\x0cÜ\x89Å[Ë¦c$\x92ó\x1f8\xad\x02\\dÑRÍ\x9a6M±\x8al±euâ\x14ö\x03û@\xa0\x1dZ\x85.3~\x88Á¡f×CìÙ>°\x0e{|[\x9c]ßµþâö\x01tJôdþ¾.\x9cR;i»_e_mÂ;!¶ÞÅ![@lÇá%\x98E\x82\x10º=©(À<½\x0c"Ö`\x86X²}÷9\x1cL¤ê¨\x8f¡>îøgÈêq*¤\x03Þ\x7fk)MGÑ-\x89Îf\x1f_\x8aý»\x8cCïÆ\x8f\x94¹X¼#ñýær\x15=«@\x93¸Ù/r0a¤á×$\x84\x9ds"¶Ð6n[¯MìíÊÎùñÂn½°¾bî$\x7fûÖ(InáL×H\x18\x1a\x93EÞP\x90\x07?¡\t\xa0\x0c¿¥Ø[W:^\r\x81½ÕÙåöúónÙû} îa\x8a\x16¨\x12Î\x18\xa0.\x89\x9c\x8bñ\x80c¼Ò\x12\x00\rè\x98Êû+\x07¦J\x04\x97ÿ1m\x9bô\x9abçÒ=üèàöXÍb»\x83¯«\x90\x80¾¼Äg»\x03æC.½\x82\x016¡T{\x9f\x1e\x8f¹¦Q!+\x00ùä\t\x19í\x8e\x8d\x8dñ\x11\x8aäû@SR\x81\x01ÑÞ^\x0få£\x12FI¥\'ôÄ÷(I[Ü±à:+\xa0®Ö\'´M\x87!?ÎÒ-[&3H\x9azuÒ´8Cém\x8d6ÂcÎMF3\x01\x81Ó\x1cù9\x9bñ1êÓÔ\x9fõB¡°ÜY´\x82½f·\x15ú74q\x8d\x16baøJWáëT'
# key = [[0,1,2],[0,0,0]]
# test_clair = "Pour trouver la clé, il n'y aura pas tellement d'autre choix a priori que la force brute. Mais la force brute requiert ici un peu de finesse si l'on veut avoir fini avant la fin de l'univers ! En particulier, on peut essayer de tester rapidement si une clé de déchiffrement donne un message en clair qui ressemble à quelque chose (on peut par exemple penser à éliminer rapidement des cas avec des tests simples, et envisager des tests plus élaborées pour ensuite éliminer d'autres cas). Dans tous les cas, la tâche risque de prendre du temps, pensez à largement tester votre algorithme avant de vous lancer et bon déchiffrement ! Pour vous permettre de tester, voici ce que donne le présent paragraphe que je le chiffre avec mon algorithme en utilisant les 3 première roues ci-dessus, en position initiale 0,0,0 :"

# s = enigma(test_clair,key, 256)
# if  s != test_chiffre:
#     print(s[:100])
# else :
#     print("Victoire ! :)")


def brutforce(message, gears):
    for x in itertools.permutations([0,1,2,3,4,5,6,7], 3):
        for y in itertools.product(range(256), repeat=3):
            key = [list(x),list(y)]
            #print(key)
            s = enigma(message, gears ,key, 256, 0)
            if  s == "Félicitations":
                print("Victoire ! " + key)



