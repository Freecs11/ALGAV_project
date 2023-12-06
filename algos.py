import time

import numpy as np
import structures as st
import matplotlib.pyplot as plt
class MinHeapNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
        self.deepest = self

class MinHeapBinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def ajout(self, value):
        if self.root is None:
            self.root = MinHeapNode(value)
        else:
            self._ajout(self.root, MinHeapNode(value))
        self.size += 1

    def _ajout(self, node, new_node):
        if node.left is None:
            new_node.parent = node
            new_node.height = node.height + 1
            node.left = new_node
            self.root.deepest = new_node
            self._heapify(new_node)
        elif node.right is None:
            new_node.parent = node
            new_node.height = node.height + 1
            node.right = new_node
            self.root.deepest = new_node
            self._heapify(new_node)
        else:
            if node.left.height <= node.right.height:
                self._ajout(node.left, new_node)
            else:
                self._ajout(node.right, new_node)
        
        

    def _heapify(self, node):
        while node.parent is not None and st.sup(node.parent.value , node.value):
            self._swap(node, node.parent)
            node = node.parent

    def _heapify_down(self, node):
        while node is not None:
            min_node = node
            if node.left is not None and st.inf(node.left.value , min_node.value):
                min_node = node.left
            if node.right is not None and st.inf(node.right.value , min_node.value):
                min_node = node.right
            if min_node != node:
                self._swap(node, min_node)
                node = min_node
            else:
                break
    
    def _swap(self, node1, node2):
        nodeheight1 = node1.height
        nodeheight2 = node2.height
        node1.value, node2.value = node2.value, node1.value
        node1.height = nodeheight2
        node2.height = nodeheight1

    def suppmin(self):
        if self.root is None:
            return None
        else:
            return self._supp(self.root)

    def _supp(self, node):
        deepest = node.deepest
        mins = node.value

        if deepest.parent is not None and deepest.parent.left == deepest:
            deepest.parent.left = None
        else:
            if deepest.parent is not None:
                deepest.parent.right = None
                deepest.parent.completed = False
            else:
                self.root = None
        self.size -= 1
        node.value = deepest.value
        node.deepest = deepest.parent
        self._heapify_down(node)
        return mins

    def ajout_iteratif(self, list_values):
        for value in list_values:
            self.ajout(value)

    def print_heap(self):
        self._print_heap(self.root)

    def _print_heap(self, root):
        if root:
            print("PARENT:", root.value, end=" ")
            if root.left:
                print("LEFT CHILD:", root.left.value, end=" ")
            if root.right:
                print("RIGHT CHILD:", root.right.value, end=" ")
            print()
            self._print_heap(root.left)
            self._print_heap(root.right)
    
    def verify_min_heap_property(self):
        if self.root is None:
            return True
        return self._verify_min_heap_property(self.root)
    
    def _verify_min_heap_property(self, node):
        if node is None:
            return True
        if node.left is not None and st.sup(node.value , node.left.value):
            # print("node 2: " + str(node.value) + " left : " + str(node.left.value)) 
            return False
        if node.right is not None and st.sup(node.value , node.right.value):
            # print ("node 2: " + str(node.value) + " right : " + str(node.right.value))
            return False
        return self._verify_min_heap_property(node.left) and self._verify_min_heap_property(node.right)
    
    # pseudo code construction
    # construction(keys):
    #   noeuds = [MinHeapNode(key) for key in keys] # on crée les noeuds pour chaque clé du tas et on les stocke dans une liste
    #   tas = MinHeapBinaryTree() # on crée un tas vide
    #   tas.root = noeuds[0] # on met le premier noeud de la liste comme racine du tas
    #   tas.size = length(keys) # on met à jour la taille du tas
    #   pour i de 0 à length(keys): # on parcourt les noeuds du tas
    #       si 2*i+1 < length(keys): # si le noeud courant a un fils gauche
    #           noeuds[i].left = noeuds[2*i+1] # on met le fils gauche du noeud courant
    #           noeuds[2*i+1].parent = noeuds[i] # on met le noeud courant comme parent du fils gauche
    #          noeuds[2*i+1].hight = noeuds[i].hight + 1 # on met à jour la hauteur du fils gauche
    #           tas.root.deepest = noeuds[2*i+1] # on met à jour le noeud le plus profond du tas
    #       si 2*i+2 < length(keys): # si le noeud courant a un fils droit
    #           noeuds[i].right = noeuds[2*i+2] # on met le fils droit du noeud courant
    #           noeuds[2*i+2].parent = noeuds[i] # on met le noeud courant comme parent du fils droit
    #           noeuds[2*i+2].hight = noeuds[i].hight + 1 # on met à jour la hauteur du fils droit
    #           tas.root.deepest = noeuds[2*i+2] # on met à jour le noeud le plus profond du tas
    #   pour i de length(keys)//2 à 0: # on parcourt les noeuds non feuilles du tas de la fin vers le début
    #       tas._heapify_down(noeuds[i]) # on heapify le noeud courant
    #   return tas
    def construction(self, keys):# pseudo code
        # Cree les noeuds pour chaque cle du tas et les stocke dans une liste nodes
        nodes = [MinHeapNode(key) for key in keys]
        self.root = nodes[0]
        self.size = len(keys)
        # Lie les noeuds entre eux pour former un arbre binaire complet
        for i in range(len(nodes)):
            if 2*i+1 < len(nodes):
                nodes[i].left = nodes[2*i+1]
                nodes[2*i+1].parent = nodes[i]
                nodes[2*i+1].hight = nodes[i].hight + 1
                self.root.deepest = nodes[2*i+1]
            if 2*i+2 < len(nodes):
                nodes[i].right = nodes[2*i+2]
                nodes[2*i+2].parent = nodes[i]
                nodes[2*i+2].hight = nodes[i].hight + 1
                self.root.deepest = nodes[2*i+2]
        # Heapify the tree
        for i in range(len(nodes)//2, -1, -1):
            self._heapify_down(nodes[i])
        return self


exem = MinHeapBinaryTree()
listofvalues = st.treat_from_file("cles_alea/jeu_1_nb_cles_1000.txt")
# listofvalues2 = st.treat_from_file("cles_alea/jeu_2_nb_cles_1000.txt")
# exem.ajout_iteratif(listofvalues)
# # exem.print_heap()



# print("min tree : " +str(exem.suppmin()) + "\n\n") 
# # print("last element : " + str(exem.root.deepest.value) + "\n\n")
# print("new min tree : " +str(exem.suppmin()) + "\n\n")


# print("verify min heap property : " + str(exem.verify_min_heap_property()) + "\n\n")

class MinHeapTable:
    def __init__(self):
        self.heap = []
        self.size = 0
        
    def parent(self, pos):
        if pos == 0:
            return 0
        return pos  // 2
    
    def leftChild(self, pos):
        if pos == 0 : 
            return 1
        return 2 * pos  
    
    def rightChild(self, pos):
        if pos == 0:
            return  2
        return (2 * pos) + 1
    
    def isLeaf(self, pos):
        return pos * 2 > self.size
    
    
    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]
        
    def _heapify(self, pos):
        # Check if the current position is a non-leaf node
        if not self.isLeaf(pos):
            # Check if the left child exists
            if self.leftChild(pos) < self.size:
                # if self.heap[self.leftChild(pos)] < self.heap[pos]:
                if st.sup(self.heap[pos], self.heap[self.leftChild(pos)]):
                    self.swap(pos, self.leftChild(pos))
                    self._heapify(self.leftChild(pos))
            # Check if the right child exists
            if self.rightChild(pos) < self.size:
                # if self.heap[self.rightChild(pos)] < self.heap[pos]:
                if st.sup(self.heap[pos], self.heap[self.rightChild(pos)]):
                    self.swap(pos, self.rightChild(pos))
                    self._heapify(self.rightChild(pos))

    def _suppmin(self):
        popped = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heap.pop()
        self._heapify(0)
        return popped

    def ajout(self, element):
        self.size += 1
        self.heap.append(element)
        current = self.size - 1
        
        
        # while self.heap[current] < self.heap[self.parent(current)]:
        while current!=self.parent(current) and st.inf(self.heap[current], self.heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)
            
        self._heapify(current)
    
    def minHeap(self):
        for pos in range((self.size // 2) +1, -1, -1):  # goes from half of the size to 0 
            self._heapify(pos)
            
    def _ajout_iteratif(self, list_values):
        for value in list_values:
            self.ajout(value)
            
    
    def print_heap(self):
        for i in range(0, self.size):
            print(self.heap[i], end=" \n")      
            
    def verify_min_heap_property(self):
        for pos in range((self.size // 2)-1 , -1, -1):
            if pos == 0:
                return True
            if not self.isLeaf(pos):
                if st.sup(self.heap[pos] , self.heap[self.leftChild(pos)]):
                    return False
                if st.sup(self.heap[pos] , self.heap[self.rightChild(pos)]):
                    return False
        return True
    
    # Donner le pseudo code de la fonction avec des explications puis l’implémenter
    # pseudo code
    # build_heap(keys):
    #    heap = keys # on ajoute les clés dans le tas
    #    size = length(keys) # on met à jour la taille du tas
    #    pour i de length(keys) // 2 à 0: # on parcourt les noeuds non feuilles du tas de la fin vers le début
    #        _heapify(i) # on heapify le noeud courant
    #    return heap
    def construction(self, keys):
        self.heap = keys[:]
        print("len : " + str(len(keys)))
        self.size = len(keys) 
        self.minHeap()
        return self    
        
# heap_ex = MinHeapTable()
# heap_ex._ajout_iteratif(listofvalues)
# print("min table : " +str(heap_ex._suppmin()) + "\n\n")
# # print("last element : " + str(heap_ex.heap[-1]) + "\n\n")
# # # heap_ex.print_heap()
# print("new min table : " +str(heap_ex._suppmin()) + "\n\n")
# print("new min table : " +str(heap_ex._suppmin()) + "\n\n")

# print("verify min heap property : " + str(heap_ex.verify_min_heap_property()) + "\n\n")


# (13784548702449909963, 17644899806406222366)
# (8365161608125828369, 9394554881227400599)
# (12629357224835867491, 9869174147496533916)
# (6242588491462870437, 8850496006118104447)
# last element : (6242588491462870437, 8850496006118104447)




# ex2 = MinHeapBinaryTree()
# ex2.construction(listofvalues)
# # ex2.print_heap()
# print("min tree of build tree : " +str(ex2.suppmin()) + "\n\n")
# print("min tree of build tree : " +str(ex2.suppmin()) + "\n\n")
# print("property : " + str(ex2.verify_min_heap_property()) + "\n\n")
# ex2.suppmin()
# ex2.print_heap()



ex =  MinHeapTable()
ex.construction(listofvalues)
# ex.print_heap()
# print("last element : " + str(ex.heap[ex.size-1]) + "\n\n")
# print("min : " +str(ex._suppmin()) + "\n\n")


def Union (heap1, heap2):
    heap = MinHeapTable()
    heap.heap = heap1.heap + heap2.heap
    heap.size = heap1.size + heap2.size
    heap.minHeap()
    return heap

# je pense qu'on nous demande d'implémenter la fonction Union pour juste une des structures
# def Union2 (heap1:MinHeapBinaryTree , heap2:MinHeapBinaryTree, _class = MinHeapBinaryTree):
#     heap = _class()
#     while heap1.root is not None and heap2.root is not None:
#         if st.inf(heap1.root.value, heap2.root.value):
#             heap.ajout(heap1.suppmin())
#         else:
#             heap.ajout(heap2.suppmin())
#     while heap1.root is not None:
#         heap.ajout(heap1.suppmin())
#     while heap2.root is not None:
#         heap.ajout(heap2.suppmin())
#     return heap

# heap1 = MinHeapTable()
# heap1.construction(listofvalues)
# l = st.treat_from_file("cles_alea/jeu_5_nb_cles_1000.txt")
# heap2 = MinHeapTable()
# heap2.construction(l)
# heap3 = Union(heap1, heap2)
# heap3.print_heap()
# print("len heap1 : " + str(heap1.size) + "\n\n")
# print("len heap2 : " + str(heap2.size) + "\n\n")
# print("len heap3 : " + str(heap3.size) + " should be : " + str(heap1.size + heap2.size) + "\n\n") 
# print("min heap2: " +str(heap2._suppmin()) + "\n\n")
# print("min heap1: " +str(heap1._suppmin()) + "\n\n")

# print("min heap3: " +str(heap3._suppmin()) + "\n\n")





list_of_sizes = [1000, 5000 ,10000, 20000, 50000, 80000, 120000 ,200000]

# def moyenne_temps_construction_table(list_of_sizes):
#     list_of_times = []
#     for size in list_of_sizes:
#         list_of_times_for_size = []
#         for i in range(1,6):
#             list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
#             start_time = time.time()
#             heap = MinHeapTable()
#             heap.construction(list_of_values)
#             end_time = time.time()
#             list_of_times_for_size.append(end_time - start_time)
#         list_of_times.append(np.mean(list_of_times_for_size))
#     return list_of_times

# list_of_times = moyenne_temps_construction_table(list_of_sizes)
# plt.plot(list_of_sizes, list_of_times)
# plt.xlabel("taille de la liste")
# plt.ylabel("temps de construction")
# plt.title("temps de construction_table en fonction de la taille de la liste")
# # plt.show()
# plt.savefig("experiments/temps_de_construction_table.png")

# # On remarque que le temps de construction est linéaire en fonction de la taille de la liste
# # ce qui est cohérent avec la complexité théorique de la fonction build_heap qui est O(n)
# # On remarque aussi que le temps de construction est plus important pour les petites listes
# # que pour les grandes listes
# # Cela est dû au fait que la fonction build_heap fait appel à la fonction minHeap qui
# # parcourt les noeuds de l'arbre des la fin vers le début et qui effectue des heapify
# # ce qui prend plus de temps pour les petits arbres que pour les grands arbres

# def moyenne_temps_construction_tree(list_of_sizes):
#     list_of_times = []
#     for size in list_of_sizes:
#         list_of_times_for_size = []
#         for i in range(1,6):
#             list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
#             start_time = time.time()
#             heap = MinHeapBinaryTree()
#             heap.construction(list_of_values)
#             end_time = time.time()
#             list_of_times_for_size.append(end_time - start_time)
#         list_of_times.append(np.mean(list_of_times_for_size))
#     return list_of_times

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


# def moyenne_temps_suppression_table(list_of_sizes):
#     list_of_times = []
#     for size in list_of_sizes:
#         list_of_times_for_size = []
#         for i in range(1,6):
#             list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
#             heap = MinHeapTable()
#             heap._ajout_iteratif(list_of_values)
#             start_time = time.time()
#             heap._suppmin()
#             end_time = time.time()
#             list_of_times_for_size.append(end_time - start_time)
#         list_of_times.append(np.mean(list_of_times_for_size))
#     return list_of_times

# list_of_times = moyenne_temps_suppression_table(list_of_sizes)
# plt.clf()
# plt.plot(list_of_sizes, list_of_times)
# plt.xlabel("taille de la lste")
# plt.ylabel("temps de suppression")
# plt.title("temps de suppression en fonction de la taille de la liste")
# # plt.show()
# plt.savefig("experiments/temps_de_suppression_table.png")

# def moyenne_temps_suppression_tree(list_of_sizes):
#     list_of_times = []
#     for size in list_of_sizes:
#         list_of_times_for_size = []
#         for i in range(1,6):
#             list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
#             heap = MinHeapBinaryTree()
#             heap.ajout_iteratif(list_of_values)
#             start_time = time.time()
#             heap.suppmin()
#             end_time = time.time()
#             list_of_times_for_size.append(end_time - start_time)
#         list_of_times.append(np.mean(list_of_times_for_size))
#     return list_of_times

# list_of_times = moyenne_temps_suppression_tree(list_of_sizes)
# plt.clf()
# plt.plot(list_of_sizes, list_of_times)
# plt.xlabel("taille de la lste")
# plt.ylabel("temps de suppression")
# plt.title("temps de suppression_tree en fonction de la taille de la liste")
# # plt.show()
# plt.savefig("experiments/temps_de_suppression_tree.png")



def moyenne_temps_ajoutIteratif_table(list_of_sizes):
    list_of_times = []
    for size in list_of_sizes:
        list_of_times_for_size = []
        for i in range(1,6):
            list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
            heap = MinHeapTable()
            start_time = time.time()
            heap._ajout_iteratif(list_of_values)
            end_time = time.time()
            list_of_times_for_size.append(end_time - start_time)
        list_of_times.append(np.mean(list_of_times_for_size))
    return list_of_times

list_of_times = moyenne_temps_ajoutIteratif_table(list_of_sizes)
plt.clf()
plt.plot(list_of_sizes, list_of_times)
plt.xlabel("taille de la lste")
plt.ylabel("temps d'ajout")
plt.title("temps d'ajout en fonction de la taille de la liste")
# plt.show()
plt.savefig("experiments/temps_d_ajoutIteratif_table.png")

# def moyenne_temps_ajoutIteratif_tree(list_of_sizes):
#     list_of_times = []
#     for size in list_of_sizes:
#         list_of_times_for_size = []
#         for i in range(1,6):
#             list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
#             heap = MinHeapBinaryTree()
#             start_time = time.time()
#             heap.ajout_iteratif(list_of_values)
#             end_time = time.time()
#             list_of_times_for_size.append(end_time - start_time)
#         list_of_times.append(np.mean(list_of_times_for_size))
#     return list_of_times

# list_of_times = moyenne_temps_ajoutIteratif_tree(list_of_sizes)
# plt.clf()
# plt.plot(list_of_sizes, list_of_times)
# plt.xlabel("taille de la lste")
# plt.ylabel("temps d'ajout")
# plt.title("temps d'ajout_tree en fonction de la taille de la liste")
# # plt.show()
# plt.savefig("experiments/temps_d_ajout_tree.png")


# # le test d'union fait les tests suivant :
# # pour une taille de liste donnée,exemple 1000, fait jeu1 union jeu2, jeu2 union jeu3, jeu3 union jeu4 et jeu4 union jeu5
# def moyenne_temps_union_table(list_of_sizes):
#     list_of_times = []
#     for size in list_of_sizes:
#         list_of_times_for_size = []
#         for i in range(1,5 , 1):
#             list_of_values1 = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
#             list_of_values2 = st.treat_from_file("cles_alea/jeu_"+str(i+1)+"_nb_cles_"+str(size)+".txt")
#             heap1 = MinHeapTable()
#             heap1.construction(list_of_values1)
#             heap2 = MinHeapTable()
#             heap2.construction(list_of_values2)
#             start_time = time.time()
#             Union(heap1, heap2)
#             end_time = time.time()
#             list_of_times_for_size.append(end_time - start_time)
#         list_of_times.append(np.mean(list_of_times_for_size))
#     return list_of_times

# list_of_times = moyenne_temps_union_table(list_of_sizes)
# plt.clf()
# plt.plot(list_of_sizes, list_of_times)
# plt.xlabel("taille de la lste")
# plt.ylabel("temps d'union")
# plt.title("temps d'union en fonction de la taille de la liste")
# # plt.show()
# plt.savefig("experiments/temps_d_union_table.png")



# def moyenne_temps_union_tree(list_of_sizes):
#     list_of_times = []
#     for size in list_of_sizes:
#         list_of_times_for_size = []
#         for i in range(1,5 , 2):
#             list_of_values1 = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
#             list_of_values2 = st.treat_from_file("cles_alea/jeu_"+str(i+1)+"_nb_cles_"+str(size)+".txt")
#             heap1 = MinHeapBinaryTree()
#             heap1.construction(list_of_values1)
#             heap2 = MinHeapBinaryTree()
#             heap2.construction(list_of_values2)
#             start_time = time.time()
#             Union2(heap1, heap2)
#             end_time = time.time()
#             list_of_times_for_size.append(end_time - start_time)
#         list_of_times.append(np.mean(list_of_times_for_size))
#     return list_of_times

# list_of_times = moyenne_temps_union_tree(list_of_sizes)
# plt.clf()
# plt.plot(list_of_sizes, list_of_times)
# plt.xlabel("taille de la lste")
# plt.ylabel("temps d'union")
# plt.title("temps d'union en fonction de la taille de la liste")
# # plt.show()
# plt.savefig("experiments/temps_d_union_tree.png")





