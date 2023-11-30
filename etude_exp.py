import os
import md5
import tree_search
import matplotlib.pyplot as plt
import numpy as np
import structures as st


tree = tree_search.search_tree()
words = []
unique_words = []
words_in_collision = []
hash_dict = {}



list_files = os.listdir("shakespeare")
# print(list_files) 
    
for file in list_files:
    f = open("shakespeare/" + file , "r")
    text = f.read()
    words_file = text.split()
    for word in words_file:
        # on ajoute le mot à la liste des mots
        words.append(word)
        hashed = md5.md5(word) # on hash le mot
        key1 = np.uint64(int(hashed[0:16], 16)) # on convertit les 16 premiers caractères du hash en int puis en uint64
        key2 = np.uint64(int(hashed[16:32], 16)) # idem pour les 16 derniers caractères
        hashed_word_cle128 = np.array(tuple((key1, key2)), dtype=st.cle128) # on crée la clé à partir de key1 et key2
        hashed_word_tuple = hashed_word_cle128.tobytes().hex() # les dictionnaires python accepte pas des types mutable (np.array) donc on convertit la clé en bytes puis en hexa et on le met comme tuple ( qui est immutable ) pour pouvoir l'utiliser comme clé de dictionnaire
        if not tree.search(hashed_word_cle128): # si le mot n'est pas déjà dans l'arbre
            tree.insert(hashed_word_cle128) # on l'ajoute
            unique_words.append(word) # on l'ajoute à la liste des mots uniques
            hash_dict[hashed_word_tuple] = [word] # on ajoute le hash et le mot dans le dictionnaire
        else: 
            if word in unique_words:  # si le mot est dans la liste des mots uniques on le supprime
                unique_words.remove(word) 
            if hashed_word_tuple in hash_dict: # si le hash est déjà dans le dictionnaire
                if word not in hash_dict[hashed_word_tuple]: # si le mot n'est pas déjà dans la liste de mots qui ont le même hash , c'est qu'il y a une collision, on l'ajoute donc
                    hash_dict[hashed_word_tuple].append(word)     
    # close the file
    f.close()

for key in hash_dict:
    if len(hash_dict[key]) > 1:
        words_in_collision.append(hash_dict[key]) # on remplit la liste des mots en collision avec les mots qui ont le même hash

# print(unique_words)
print("unique words = " + str(len(unique_words)))
    
print("words len = " + str(len(words)))
# print(words)
print("words in collision = " + str(len(words_in_collision)))
