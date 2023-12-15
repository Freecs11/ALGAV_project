import os
import time

from matplotlib import gridspec
import md5
import tree_search
import matplotlib.pyplot as plt
import numpy as np
import structures as st
from MinHeap import *
from BinomialQueue import *

''' les experimentations de la partie 6 sont dans le jupyter ainsi que cette etudes  '''

# ex 6.14 
# tree = tree_search.search_tree()
# words = []
# unique_words = []
# words_in_collision = []
# hash_dict = {}

# list_files = os.listdir("shakespeare")
# # print(list_files) 
    
# for file in list_files:
#     f = open("shakespeare/" + file , "r")
#     text = f.read()
#     words_file = text.split()
#     for word in words_file:
#         # on ajoute le mot à la liste des mots
#         words.append(word)
#         hashed = md5.md5(word) # on hash le mot
#         key1 = np.uint64(int(hashed[0:16], 16)) # on convertit les 16 premiers caractères du hash en int puis en uint64
#         key2 = np.uint64(int(hashed[16:32], 16)) # idem pour les 16 derniers caractères
#         hashed_word_cle128 = np.array(tuple((key1, key2)), dtype=st.cle128) # on crée la clé à partir de key1 et key2
#         hashed_word_tuple = hashed_word_cle128.tobytes().hex() # les dictionnaires python accepte pas des types mutable (np.array) donc on convertit la clé en bytes puis en hexa et on le met comme tuple ( qui est immutable ) pour pouvoir l'utiliser comme clé de dictionnaire
#         if not tree.search(hashed_word_cle128): # si le mot n'est pas déjà dans l'arbre
#             tree.insert(hashed_word_cle128) # on l'ajoute
#             if word not in unique_words: # si le mot n'est pas déjà dans la liste des mots uniques
#                 unique_words.append(word)
#             hash_dict[hashed_word_tuple] = [word] # on ajoute le hash et le mot dans le dictionnaire
#         else: 
#             if hashed_word_tuple in hash_dict: # si le hash est déjà dans le dictionnaire
#                 if word not in hash_dict[hashed_word_tuple]: # si le mot n'est pas déjà dans la liste de mots qui ont le même hash , c'est qu'il y a une collision, on l'ajoute donc
#                     hash_dict[hashed_word_tuple].append(word)     
#     # close the file
#     f.close()

# for key in hash_dict:
#     if len(hash_dict[key]) > 1:
#         words_in_collision.append(hash_dict[key]) # on remplit la liste des mots en collision avec les mots qui ont le même hash

# # print(unique_words)
# print("unique words = " + str(len(unique_words))) # 8471
    
# print("words len = " + str(len(words))) # 905534
# # print(words)
# print("words in collision = " + str(len(words_in_collision))) # 0
# print(words_in_collision)

# Question 6.16 Comparer graphiquement les temps d’exécution des algorithmes SupprMin, Ajout,
# Construction, Union pour les deux types de structure de données : tas min et files binomiales sur les
# données extraites de la question 6.14.

# list_tree = tree.toList()
# print(str(len(list_tree)))


def moyenne_temps_construction(list_of_values):
    list_of_times_heaptable = []
    list_of_times_binomialQueue = []
    list_of_times_heaptree = []
    heaptable = MinHeapTable()
    binomialQueue = BinomialQueue()
    heaptree = MinHeapBinaryTree()
    starttime = time.perf_counter()
    heaptable.construction(list_of_values)
    endtime = time.perf_counter()
    list_of_times_heaptable.append(endtime - starttime)
    starttime = time.perf_counter()
    binomialQueue.construction(list_of_values)
    endtime = time.perf_counter()
    list_of_times_binomialQueue.append(endtime - starttime)
    starttime = time.perf_counter()
    heaptree.construction(list_of_values)
    endtime = time.perf_counter()
    list_of_times_heaptree.append(endtime - starttime)
    return list_of_times_heaptable, list_of_times_binomialQueue, list_of_times_heaptree




def moyenne_temps_ajout(list_of_values):
    list_of_times_heaptable = []
    list_of_times_binomialQueue = []
    list_of_times_heaptree = []
    heaptable = MinHeapTable()
    binomialQueue = BinomialQueue()
    heaptree = MinHeapBinaryTree()
    heaptable.construction(list_of_values[1:])
    binomialQueue.construction(list_of_values[1:])
    heaptree.construction(list_of_values[1:])
    
    starttime = time.perf_counter()
    heaptable.ajout(list_of_values[0])
    endtime = time.perf_counter()
    list_of_times_heaptable.append(endtime - starttime)
    
    starttime = time.perf_counter()
    binomialHeap = BinomialHeap()
    binomialHeap.ajout(list_of_values[0])
    binomialQueue.ajout(binomialHeap)
    endtime = time.perf_counter()
    list_of_times_binomialQueue.append(endtime - starttime)
    
    starttime = time.perf_counter()
    heaptree.ajout(list_of_values[0])
    endtime = time.perf_counter()
    list_of_times_heaptree.append(endtime - starttime)
               
    return list_of_times_heaptable, list_of_times_binomialQueue, list_of_times_heaptree

def moyenne_temps_supp(list_of_values):
    list_of_times_heaptable = []
    list_of_times_binomialQueue = []
    list_of_times_heaptree = []
    heaptable = MinHeapTable()
    binomialQueue = BinomialQueue()
    heaptree = MinHeapBinaryTree()
    heaptable.construction(list_of_values)
    for i in range(1):
        start_time = time.perf_counter()
        heaptable._suppmin()
        end_time = time.perf_counter()
        list_of_times_heaptable.append(end_time - start_time)
    binomialQueue.construction(list_of_values)
    for i in range(1):
        start_time = time.perf_counter()
        binomialQueue.supprMin()
        end_time = time.perf_counter()
        list_of_times_binomialQueue.append(end_time - start_time)
    heaptree.construction(list_of_values)
    for i in range(1):
        start_time = time.perf_counter()
        heaptree.suppmin()
        end_time = time.perf_counter()
        list_of_times_heaptree.append(end_time - start_time)
    return list_of_times_heaptable, list_of_times_binomialQueue, list_of_times_heaptree

def moyenne_temps_union(list_of_values):
    list_of_times_heaptable = []
    list_of_times_binomialQueue = []
    list_of_times_heaptree = []
    heaptable = MinHeapTable()
    heaptable2 = MinHeapTable()
    binomialQueue = BinomialQueue()
    BinomialQueue2 = BinomialQueue()
    heaptree = MinHeapBinaryTree()
    heaptree2 = MinHeapBinaryTree()
    # split the list of values in two lists
    list_of_values1 = list_of_values[:len(list_of_values)//2]
    list_of_values2 = list_of_values[len(list_of_values)//2:]
    heaptable.construction(list_of_values1)
    heaptable2.construction(list_of_values2)
    starttime = time.perf_counter()
    Union(heaptable, heaptable2)
    endtime = time.perf_counter()
    list_of_times_heaptable.append(endtime - starttime)
    binomialQueue.construction(list_of_values1)
    BinomialQueue2.construction(list_of_values2)
    starttime = time.perf_counter()
    binomialQueue.union(BinomialQueue2)
    endtime = time.perf_counter()
    list_of_times_binomialQueue.append(endtime - starttime)
    heaptree.construction(list_of_values1)
    heaptree2.construction(list_of_values2)
    starttime = time.perf_counter()
    Union2(heaptree, heaptree2)
    endtime = time.perf_counter()
    list_of_times_heaptree.append(endtime - starttime)
    return list_of_times_heaptable, list_of_times_binomialQueue, list_of_times_heaptree
