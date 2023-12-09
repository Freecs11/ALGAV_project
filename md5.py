#définir et implémenter la fonction de hachage classique nommée Message Digest 5,
#ou MD5. Implémenter l’algorithme dont le pseudo-code est donné sur la page wikipedia de l’algorithme :
#https://fr.wikipedia.org/wiki/MD5
import math

def leftrotate(x: int, c: int) :
    return (x << c) | (x >> (32 - c))

def md5(message: str) -> str:
    # Définition de r et k

    r = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22
            , 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20
            , 5, 9, 14, 20, 4, 11, 16, 23, 4, 11, 16, 23
            , 4, 11, 16, 23, 4, 11, 16, 23
            , 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
            , 6, 10, 15, 21]
    k = [int(abs(math.sin(i + 1)) * 2**32) for i in range(64)]
    
    # Initialisation des variables
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    
    # Pré-traitement du message
    # Conversion du message en tableau d'octets
    message = bytearray(message, encoding='utf-8')
    # Récupération de la longueur du message
    message_len = (8 * len(message)) 
    # Ajout du bit 1 à la fin du message
    message.append(0x80)
    # Ajout de bits nuls jusqu'à ce que la taille du message soit égale à 448 mod 512
    while len(message) % 64 != 56:
        message.append(0)
    # Ajout de la longueur du message à la fin du message
    message += message_len.to_bytes(8, byteorder='little')
    
    # Traitement du message par blocs de 512 bits
    for i in range(0, len(message), 64):
        # Récupération du bloc
        block = message[i:i+64]
        # Création d'un tableau de 16 entiers de 32 bits
        words = [int.from_bytes(block[j:j+4], byteorder='little') for j in range(0, 64, 4)]
        # Copie des valeurs initiales de h
        a = h0
        b = h1
        c = h2
        d = h3
        # Boucle principale
        for j in range(64):
            if 0 <= j <= 15:
                f = (b & c) | ((~b) & d)
                g = j
            elif 16 <= j <= 31:
                f = (d & b) | ((~d) & c)
                g = (5 * j + 1) % 16
            elif 32 <= j <= 47:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            elif 48 <= j <= 63:
                f = c ^ (b | (~d))
                g = (7 * j) % 16
            # Calcul de la nouvelle valeur de d
            d_temp = d
            d = c
            c = b
            b = (b + leftrotate((a + f + k[j] + words[g]) & 0xFFFFFFFF, r[j])) & 0xFFFFFFFF
            a = d_temp
        # Ajout des valeurs finales de h au résultat
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        
    # Conversion des valeurs finales de h en hexadécimal
    digest = (h0.to_bytes(4, byteorder='little') + h1.to_bytes(4, byteorder='little') 
            + h2.to_bytes(4, byteorder='little') + h3.to_bytes(4, byteorder='little'))
    return digest.hex()

    
# # Example usage
# message = "Et l’unique cordeau des trompettes marines"
# hashed_message = md5(message)
# print("MD5 Hash:", hashed_message)
# message ="Et l’unique cordeau des trompettes marinEs" 
# hashed_message = md5(message)
# print("MD5 Hash:", hashed_message)
# message = "fist"
# hashed_message = md5(message)
# print("MD5 fist:", hashed_message)
# message = "hist"
# hashed_message = md5(message)
# print("MD5 hist:", hashed_message)

