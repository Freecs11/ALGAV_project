#définir et implémenter la fonction de hachage classique nommée Message Digest 5,
#ou MD5. Implémenter l’algorithme dont le pseudo-code est donné sur la page wikipedia de l’algorithme :
#https://fr.wikipedia.org/wiki/MD5
import math

def leftrotate(x, c):
    return (x << c) | (x >> (32 - c)) # we shift x by c bits to the left and we add the bits that were shifted to the right

def md5(message):
    # Constants
    r = [7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
        5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
        4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
        6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21]

    k = [math.floor(abs(math.sin(i + 1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

    # Initial hash values
    h0, h1, h2, h3 = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476

    # Padding the message
    message = bytearray(message, 'utf-8')
    message.append(0x80) # we add 1 to the message
    while len(message) % 64 != 56: # we want a length of 448 bits so we add 0s until the length is 448 bits (mod 512) = len % 64 = 56
        message.append(0x00)

    # Append the original message length in bits
    length = (8 * len(message)).to_bytes(8, byteorder='little') # we want the length in bits so we multiply by 8 and convert to bytes ( and also we want order to be little endian )
    message.extend(length) # we add the length to the message

    # Process each 512-bit block
    for i in range(0, len(message), 64): # we process the message by blocks of 512 bits
        block = message[i:i+64]  # we get the block of 512 bits

        # Break the block into 16 words of 32 bits
        w = [int.from_bytes(block[j:j+4], byteorder='little') for j in range(0, 64, 4)] # we break the block into 16 words of 32 bits

        # Initialize hash values for this block
        a, b, c, d = h0, h1, h2, h3

        # Main loop
        for j in range(64):
            if 0 <= j <= 15:
                f = (b & c) | ((~b) & d) # (~ is the bitwise NOT operator so ~b is the bitwise NOT of b)
                g = j # g is just j
            elif 16 <= j <= 31:
                f = (d & b) | ((~d) & c) 
                g = (5 * j + 1) % 16
            elif 32 <= j <= 47:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            elif 48 <= j <= 63:
                f = c ^ (b | (~d))
                g = (7 * j) % 16

            temp = d
            d = c
            c = b
            b = (b + leftrotate((a + f + k[j] + w[g]), r[j])) & 0xFFFFFFFF # we add the result of the function to b and we make sure it's 32 bits long
            a = temp

        # Update hash values
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF

    # Concatenate the hash values
    digest = h0.to_bytes(4, byteorder='little') + h1.to_bytes(4, byteorder='little') + h2.to_bytes(4, byteorder='little') + h3.to_bytes(4, byteorder='little')

    return digest.hex()

# Example usage
message = "archidamus"
hashed_message = md5(message)
print("MD5 Hash:", hashed_message)
