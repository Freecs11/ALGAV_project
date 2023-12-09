import time
from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter

import numpy as np
from BinomialQueue import *
from struct import *
 
def moyenne_temps_construction(list_of_sizes):
    list_of_times = []
    for size in list_of_sizes:
        list_of_times_for_size = []
        for i in range(1,6):
            list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
            binomialQueue = BinomialQueue()
            start_time = time.time()
            binomialQueue.construction(list_of_values)
            end_time = time.time()
            list_of_times_for_size.append(end_time - start_time)
        list_of_times.append(np.mean(list_of_times_for_size))
    return list_of_times

def moyenne_temps_union(list_of_sizes):
    list_of_times = []
    for size in list_of_sizes:
        list_of_times_for_size = []
        for i in range(1,5 , 1):
            list_of_values1 = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
            list_of_values2 = st.treat_from_file("cles_alea/jeu_"+str(i+1)+"_nb_cles_"+str(size)+".txt")
            BinomialQueue1 = BinomialQueue()
            BinomialQueue2 = BinomialQueue()
            BinomialQueue1.construction(list_of_values1)
            BinomialQueue2.construction(list_of_values2)
            start_time = time.time()
            BinomialQueue1.union(BinomialQueue2)
            end_time = time.time()
            list_of_times_for_size.append(end_time - start_time)
        list_of_times.append(np.mean(list_of_times_for_size))
    return list_of_times

def representation_graphique(abscisse, ordonnee, nom_fichier, xlabe='', ylabe='', titre='', label='', plot=False):
    fig, ax = plt.subplots()
    ax.plot(abscisse, ordonnee, label=label)

    ax.set_xlabel(xlabe)
    ax.set_ylabel(ylabe)
    ax.set_title(titre)
    ax.legend()

    # Sauvegarder le graphique
    plt.savefig("experiments/binomialQueue/" + nom_fichier)

    if plot:
        plt.show()

if __name__ == '__main__':
    
    list_of_sizes = [1000, 5000 ,10000, 20000, 50000, 80000, 120000 ,200000]
    list_moyenne_temps_construction = moyenne_temps_construction(list_of_sizes)
    print (list_moyenne_temps_construction)
    xlabel = "liste de taille n"
    ylabel = "temps de construction en secondes"
    titre = "Temps d'execution de la construction d'une fil binomial \n en fonction de la taille de la liste"
    label = "construction"
    nom_fichier = "binomialQueue_construction_temps.png"
    representation_graphique(list_of_sizes, list_moyenne_temps_construction, nom_fichier, xlabel, ylabel, titre, label)    
    
    list_moyenne_temps_union = moyenne_temps_union(list_of_sizes)
    print (list_moyenne_temps_union)
    xlabel = "liste de taille n"
    ylabel = "temps d'union en secondes"
    titre = "Temps d'execution de l'union de deux fils binomiaux \n en fonction de la taille de la liste"
    label = "union"
    nom_fichier = "binomialQueue_union_temps.png"
    representation_graphique(list_of_sizes, list_moyenne_temps_union, nom_fichier, xlabel, ylabel, titre, label, True)
    