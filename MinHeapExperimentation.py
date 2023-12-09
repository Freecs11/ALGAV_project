from MinHeap import *
import matplotlib.pyplot as plt
import numpy as np


''' expérimentations du tas min avec un arbre binaire et avec table '''

list_of_sizes = [1000, 5000 ,10000, 20000, 50000, 80000, 120000 ,200000]

def format_func(value, _):
    return f'{value:.2f}'

def moyenne_temps_construction_table(list_of_sizes):
    list_of_times = []
    for size in list_of_sizes:
        list_of_times_for_size = []
        for i in range(1,6):
            list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
            start_time = time.time()
            heap = MinHeapTable()
            heap.construction(list_of_values)
            end_time = time.time()
            list_of_times_for_size.append(end_time - start_time)
        list_of_times.append(np.mean(list_of_times_for_size))
    return list_of_times

# list_of_times = moyenne_temps_construction_table(list_of_sizes)
# plt.plot(list_of_sizes, list_of_times)
# plt.xlabel("taille de la liste")
# plt.ylabel("temps de construction")
# plt.title("temps de construction_table en fonction de la taille de la liste")
# # plt.show()
# plt.savefig("experiments/temps_de_construction_table.png")


def moyenne_temps_construction_tree(list_of_sizes):
    list_of_times = []
    for size in list_of_sizes:
        list_of_times_for_size = []
        for i in range(1,6):
            list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
            start_time = time.time()
            heap = MinHeapBinaryTree()
            heap.construction(list_of_values)
            end_time = time.time()
            list_of_times_for_size.append(end_time - start_time)
        list_of_times.append(np.mean(list_of_times_for_size))
    return list_of_times

# # save it a png with the name "temps_de_construction_tree.png"
# list_of_times = moyenne_temps_construction_tree(list_of_sizes)
# # reset the plot
# plt.clf()
# plt.plot(list_of_sizes, list_of_times)
# plt.xlabel("taille de la lste")
# plt.ylabel("temps de construction")
# plt.title("temps de construction_tree en fonction de la taille de la liste")
# # plt.show()
# plt.savefig("experiments/temps_de_construction_tree.png")


def moyenne_temps_suppression_table(list_of_sizes):
    list_of_times = []
    for size in list_of_sizes:
        list_of_times_for_size = []
        for i in range(1,6):
            list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
            heap = MinHeapTable()
            heap.construction(list_of_values)
            for j in range(700):
                start_time = time.perf_counter()
                heap._suppmin()
                end_time = time.perf_counter()
                list_of_times_for_size.append(end_time - start_time)
        list_of_times.append(np.mean(list_of_times_for_size))
    return list_of_times

# list_of_times = moyenne_temps_suppression_table(list_of_sizes)
# plt.clf()
# plt.plot(list_of_sizes, list_of_times)
# plt.xlabel("taille de la lste")
# plt.ylabel("temps de suppression")
# plt.title("temps de suppression_table en fonction de la taille de la liste")
# # plt.show()
# plt.savefig("experiments/temps_de_suppression_tables.png")

def moyenne_temps_suppression_tree(list_of_sizes):
    list_of_times = []
    for size in list_of_sizes:
        list_of_times_for_size = []
        for i in range(1,6):
            list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
            heap = MinHeapBinaryTree()
            heap.construction(list_of_values)
            for j in range(800):
                start_time = time.perf_counter()
                heap.suppmin()
                end_time = time.perf_counter()
                list_of_times_for_size.append(end_time - start_time)
        list_of_times.append(np.mean(list_of_times_for_size))
    return list_of_times

# list_of_times = moyenne_temps_suppression_tree(list_of_sizes)
# plt.clf()
# plt.plot(list_of_sizes, list_of_times)
# plt.xlabel("taille de la lste")
# plt.ylabel("temps de suppression")
# plt.title("temps de suppression_tree en fonction de la taille de la liste")
# # plt.show()
# plt.savefig("experiments/temps_de_suppression_trees.png")



def moyenne_temps_ajoutIteratif_table(list_of_sizes):
    list_of_times = []
    for size in list_of_sizes:
        list_of_times_for_size = []
        for i in range(1,6):
            list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
            heap = MinHeapTable()
            start_time = time.perf_counter()
            heap._ajout_iteratif(list_of_values)
            end_time = time.perf_counter()
            list_of_times_for_size.append(end_time - start_time)
        list_of_times.append(np.mean(list_of_times_for_size))
    return list_of_times

# list_of_times = moyenne_temps_ajoutIteratif_table(list_of_sizes)
# plt.clf()
# plt.plot(list_of_sizes, list_of_times)
# # make the x axis logarithmic but don't write 10^3, 10^4, 10^5, 10^6, 10^7, 10^8	
# plt.xlabel("taille de la lste")
# plt.ylabel("temps d'ajout")
# plt.title("temps d'ajout_table en fonction de la taille de la liste")
# # plt.show()
# plt.savefig("experiments/temps_d_ajoutIteratif_table.png")

def moyenne_temps_ajoutIteratif_tree(list_of_sizes):
    list_of_times = []
    for size in list_of_sizes:
        list_of_times_for_size = []
        for i in range(1,6):
            list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
            heap = MinHeapBinaryTree()
            start_time = time.perf_counter()
            heap.ajout_iteratif(list_of_values)
            end_time = time.perf_counter()
            list_of_times_for_size.append(end_time - start_time)
        list_of_times.append(np.mean(list_of_times_for_size))
    return list_of_times

# list_of_times = moyenne_temps_ajoutIteratif_tree(list_of_sizes)
# plt.clf()
# plt.plot(list_of_sizes, list_of_times)
# plt.xlabel("taille de la lste")
# plt.ylabel("temps d'ajout")
# plt.title("temps d'ajout_tree en fonction de la taille de la liste")
# # plt.show()
# # plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(format_func))
# plt.savefig("experiments/temps_d_ajoutIteratif_tree.png")


# le test d'union fait les tests suivant :
# pour une taille de liste donnée,exemple 1000, fait jeu1 union jeu2, jeu2 union jeu3, jeu3 union jeu4 et jeu4 union jeu5
def moyenne_temps_union_table(list_of_sizes):
    list_of_times = []
    for size in list_of_sizes:
        list_of_times_for_size = []
        for i in range(1,5 , 1):
            list_of_values1 = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
            list_of_values2 = st.treat_from_file("cles_alea/jeu_"+str(i+1)+"_nb_cles_"+str(size)+".txt")
            heap1 = MinHeapTable()
            heap1.construction(list_of_values1)
            heap2 = MinHeapTable()
            heap2.construction(list_of_values2)
            start_time = time.perf_counter()
            Union(heap1, heap2)
            end_time = time.perf_counter()
            list_of_times_for_size.append(end_time - start_time)
        list_of_times.append(np.mean(list_of_times_for_size))
    return list_of_times

# list_of_times = moyenne_temps_union_table(list_of_sizes)
# plt.clf()
# plt.plot(list_of_sizes, list_of_times)
# plt.xlabel("taille de la lste")
# plt.ylabel("temps d'union")
# plt.title("temps d'union_table en fonction de la taille de la liste")
# # plt.show()
# plt.savefig("experiments/temps_d_union_table.png")



def moyenne_temps_union_tree(list_of_sizes):
    list_of_times = []
    for size in list_of_sizes:
        list_of_times_for_size = []
        for i in range(1,5 , 1):
            list_of_values1 = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
            list_of_values2 = st.treat_from_file("cles_alea/jeu_"+str(i+1)+"_nb_cles_"+str(size)+".txt")
            heap1 = MinHeapBinaryTree()
            heap1.construction(list_of_values1)
            heap2 = MinHeapBinaryTree()
            heap2.construction(list_of_values2)
            start_time = time.perf_counter()
            Union2(heap1, heap2)
            end_time = time.perf_counter()
            list_of_times_for_size.append(end_time - start_time)
        list_of_times.append(np.mean(list_of_times_for_size))
    return list_of_times

# list_of_times = moyenne_temps_union_tree(list_of_sizes)
# plt.clf()
# plt.plot(list_of_sizes, list_of_times)
# plt.xlabel("taille de la lste")
# plt.ylabel("temps d'union")
# plt.title("temps d'union_tree en fonction de la taille de la liste")
# # plt.show()
# plt.savefig("experiments/temps_d_union_tree.png")

def representation_graphique(abscisse, ordonnee, nom_fichier, xlabe='', ylabe='', titre='', label='', plot=False):
    fig, ax = plt.subplots()
    ax.plot(abscisse, ordonnee, label=label)

    ax.set_xlabel(xlabe)
    ax.set_ylabel(ylabe)
    ax.set_title(titre)
    ax.legend()

    plt.gca().get_yaxis().get_major_formatter().set_scientific(False)


    # Sauvegarder le graphique
    plt.savefig("experiments/MinHeap/" + nom_fichier)

    if plot:
        plt.show()


if __name__ == '__main__':
    # list_of_times = moyenne_temps_construction_table(list_of_sizes)
    # xlabel = "liste de taille n"
    # ylabel = "temps de construction en secondes"
    # titre = "Temps d'execution de la construction d'un tas min avec table \n en fonction de la taille de la liste"
    # label = "construction"
    # nom_fichier = "MinHeap_construction_table_temps.png"
    # representation_graphique(list_of_sizes, list_of_times, nom_fichier, xlabel, ylabel, titre, label)
    
    # list_of_times = moyenne_temps_construction_tree(list_of_sizes)
    # xlabel = "liste de taille n"
    # ylabel = "temps de construction en secondes"
    # titre = "Temps d'execution de la construction d'un tas min avec arbre binaire \n en fonction de la taille de la liste"
    # label = "construction"
    # nom_fichier = "MinHeap_construction_tree_temps.png"
    # representation_graphique(list_of_sizes, list_of_times, nom_fichier, xlabel, ylabel, titre, label)
    
    # list_of_times = moyenne_temps_suppression_table(list_of_sizes)
    # xlabel = "liste de taille n"
    # ylabel = "temps de suppression en secondes"
    # titre = "Temps d'execution de la suppression d'un tas min avec table \n en fonction de la taille de la liste"
    # label = "suppression"
    # nom_fichier = "MinHeap_suppression_table_temps.png"
    # representation_graphique(list_of_sizes, list_of_times, nom_fichier, xlabel, ylabel, titre, label)
    
    # list_of_times = moyenne_temps_suppression_tree(list_of_sizes)
    # xlabel = "liste de taille n"
    # ylabel = "temps de suppression en secondes"
    # titre = "Temps d'execution de la suppression d'un tas min avec arbre binaire \n en fonction de la taille de la liste"
    # label = "suppression"
    # nom_fichier = "MinHeap_suppression_tree_temps.png"
    # representation_graphique(list_of_sizes, list_of_times, nom_fichier, xlabel, ylabel, titre, label)
    
    # list_of_times = moyenne_temps_ajoutIteratif_table(list_of_sizes)
    # xlabel = "liste de taille n"
    # ylabel = "temps d'ajout en secondes"
    # titre = "Temps d'execution de l'ajout_iteratif d'un tas min avec table \n en fonction de la taille de la liste"
    # label = "ajout"
    # nom_fichier = "MinHeap_ajout_table_temps.png"
    # representation_graphique(list_of_sizes, list_of_times, nom_fichier, xlabel, ylabel, titre, label)
    
    # list_of_times = moyenne_temps_ajoutIteratif_tree(list_of_sizes)
    # xlabel = "liste de taille n"
    # ylabel = "temps d'ajout en secondes"
    # titre = "Temps d'execution de l'ajout_iteratif d'un tas min avec arbre binaire \n en fonction de la taille de la liste"
    # label = "ajout"
    # nom_fichier = "MinHeap_ajout_tree_temps.png"
    # representation_graphique(list_of_sizes, list_of_times, nom_fichier, xlabel, ylabel, titre, label)
    
    list_of_times = moyenne_temps_union_table(list_of_sizes)
    xlabel = "liste de taille n"
    ylabel = "temps d'union en secondes"
    titre = "Temps d'execution de l'union de deux tas min avec table \n en fonction de la taille de la liste"
    label = "union"
    nom_fichier = "MinHeap_union_table_temps.png"
    representation_graphique(list_of_sizes, list_of_times, nom_fichier, xlabel, ylabel, titre, label)
    
    list_of_times = moyenne_temps_union_tree(list_of_sizes)
    xlabel = "liste de taille n"
    ylabel = "temps d'union en secondes"
    titre = "Temps d'execution de l'union de deux tas min avec arbre binaire \n en fonction de la taille de la liste"
    label = "union"
    nom_fichier = "MinHeap_union_tree_temps.png"
    representation_graphique(list_of_sizes, list_of_times, nom_fichier, xlabel, ylabel, titre, label)