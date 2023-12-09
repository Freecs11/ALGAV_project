import decimal
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
        curr = node
        while curr.parent is not None and st.inf(curr.value, curr.parent.value):
            self._swap(curr, curr.parent)
            curr = curr.parent

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
        node1.value, node2.value = node2.value, node1.value
        node1.height, node2.height = node2.height, node1.height
        

    def suppmin(self):
        if self.root is None:
            return None
        else:
            mins = self.root.value
            deepest = self.root.deepest
            if deepest.parent is None :
                self.root = None
            elif deepest.parent.left == deepest:
                deepest.parent.left = None
            else:
                deepest.parent.right = None
            if self.root is not None and deepest is not None:
                self.root.value = deepest.value
                self.root.deepest = self._maj_deepest(self.root)
                self._heapify_down(self.root)
                self.size -= 1
            return mins
            
    def _maj_deepest(self, node):
        if node is None:
            return None
        if node.left is None and node.right is None:
            return node
        if node.left is None:
            return self._maj_deepest(node.right)
        if node.right is None:
            return self._maj_deepest(node.left)
        if node.left.height > node.right.height:
            return self._maj_deepest(node.left)
        else:
            return self._maj_deepest(node.right)

    def ajout_iteratif(self, list_values):
        for value in list_values:
            self.ajout(value)
            
    def toList(self):
        list = []
        self._toList(self.root, list)
        return list
    
    def _toList(self, node, list):
        if node is None:
            return
        list.append(node.value)
        self._toList(node.left, list)
        self._toList(node.right, list)

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
                nodes[2*i+1].height = nodes[i].height + 1
                self.root.deepest = nodes[2*i+1]
            if 2*i+2 < len(nodes):
                nodes[i].right = nodes[2*i+2]
                nodes[2*i+2].parent = nodes[i]
                nodes[2*i+2].height = nodes[i].height + 1
                self.root.deepest = nodes[2*i+2]
        # Heapify the tree
        for i in range(len(nodes)//2, -1, -1):
            self._heapify_down(nodes[i])
        return self


# exem = MinHeapBinaryTree()
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
        return (pos - 1) // 2  # Subtract 1 before dividing by 2
    
    def leftChild(self, pos):
        return 2 * pos + 1  # Add 1 after multiplying by 2
    
    def rightChild(self, pos):
        return 2 * pos + 2  # Add 2 after multiplying by 2
    
    def isLeaf(self, pos):
        return pos >= (self.size // 2)  # Check if pos is greater than or equal to half the size
    
    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]
        
    def _heapify_down(self, pos):
        if not self.isLeaf(pos):
            leftChild = self.leftChild(pos)
            rightChild = self.rightChild(pos)
            if rightChild < self.size and leftChild < self.size:
                if st.inf(self.heap[leftChild], self.heap[rightChild]):
                    if st.inf(self.heap[leftChild], self.heap[pos]):
                        self.swap(pos, leftChild)
                        self._heapify_down(leftChild)
                else:
                    if st.inf(self.heap[rightChild], self.heap[pos]):
                        self.swap(pos, rightChild)
                        self._heapify_down(rightChild)
            elif leftChild < self.size:
                if st.inf(self.heap[leftChild], self.heap[pos]):
                    self.swap(pos, leftChild)
                    self._heapify_down(leftChild)
            elif rightChild < self.size:
                if st.inf(self.heap[rightChild], self.heap[pos]):
                    self.swap(pos, rightChild)
                    self._heapify_down(rightChild)

    def _suppmin(self):
        if self.size == 0:
            return None
        popped = self.heap.pop()
        if self.size == 0:
            return popped
        mins = self.heap[0]
        self.heap[0] = popped 
        self.size -= 1
        self._heapify_down(0)
        return mins

    def ajout(self, element):
        self.size += 1
        self.heap.append(element)
        current = self.size - 1
        
        while current != self.parent(current) and st.inf(self.heap[current], self.heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)
    
    def minHeap(self):
        for pos in range((self.size // 2) - 1, -1, -1):  # goes from half of the size to 0 
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



# ex =  MinHeapTable()
# ex.construction(listofvalues)
# ex.print_heap()
# print("last element : " + str(ex.heap[ex.size-1]) + "\n\n")
# print("min : " +str(ex._suppmin()) + "\n\n")


def Union (heap1, heap2):
    heap = MinHeapTable()
    heap.heap = heap1.heap + heap2.heap
    heap.size = heap1.size + heap2.size
    heap.minHeap()
    return heap

def Union2(heap1: MinHeapBinaryTree, heap2: MinHeapBinaryTree):
    heap = MinHeapBinaryTree()
    list_heap1 = heap1.toList()
    list_heap2 = heap2.toList()
    list_heap = list_heap1 + list_heap2
    heap.construction(list_heap)
    heap.size = heap1.size + heap2.size
    return heap

# helap = MinHeapBinaryTree()
# r = st.treat_from_file("cles_alea/jeu_1_nb_cles_200000.txt")
# x = st.treat_from_file("cles_alea/jeu_2_nb_cles_200000.txt")
# helap.construction(r)
# helap2 = MinHeapBinaryTree()
# helap2.construction(x)
# heap4 = Union2(helap, helap2)
# # heap4.print_heap()
# print("verify min heap property : " + str(heap4.verify_min_heap_property()) + "\n\n")



''' expérimentations du tas min avec un arbre binaire et avec table '''

list_of_sizes = [1000, 5000 ,10000, 20000, 50000, 80000, 120000 ,200000]

def format_func(value, _):
    return f'{value:.2f}'

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
# # plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(format_func))
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
# # plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(format_func))
# plt.savefig("experiments/temps_de_construction_tree.png")


# def moyenne_temps_suppression_table(list_of_sizes):
#     list_of_times = []
#     for size in list_of_sizes:
#         list_of_times_for_size = []
#         for i in range(1,6):
#             list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
#             heap = MinHeapTable()
#             heap.construction(list_of_values)
#             for j in range(700):
#                 start_time = time.perf_counter()
#                 heap._suppmin()
#                 end_time = time.perf_counter()
#                 list_of_times_for_size.append(end_time - start_time)
#         list_of_times.append(np.mean(list_of_times_for_size))
#     return list_of_times

# list_of_times = moyenne_temps_suppression_table(list_of_sizes)
# plt.clf()
# plt.plot(list_of_sizes, list_of_times)
# plt.xlabel("taille de la lste")
# plt.ylabel("temps de suppression")
# plt.title("temps de suppression_table en fonction de la taille de la liste")
# # plt.show()
# plt.savefig("experiments/temps_de_suppression_tables.png")

# def moyenne_temps_suppression_tree(list_of_sizes):
#     list_of_times = []
#     for size in list_of_sizes:
#         list_of_times_for_size = []
#         for i in range(1,6):
#             list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
#             heap = MinHeapBinaryTree()
#             heap.construction(list_of_values)
#             for j in range(800):
#                 start_time = time.perf_counter()
#                 heap.suppmin()
#                 end_time = time.perf_counter()
#                 list_of_times_for_size.append(end_time - start_time)
#         list_of_times.append(np.mean(list_of_times_for_size))
#     return list_of_times

# list_of_times = moyenne_temps_suppression_tree(list_of_sizes)
# plt.clf()
# plt.loglog(list_of_sizes, list_of_times)
# plt.xlabel("taille de la lste")
# plt.ylabel("temps de suppression")
# plt.title("temps de suppression_tree en fonction de la taille de la liste")
# # plt.show()
# plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(format_func))
# plt.savefig("experiments/temps_de_suppression_trees1.png")



# def moyenne_temps_ajoutIteratif_table(list_of_sizes):
#     list_of_times = []
#     for size in list_of_sizes:
#         list_of_times_for_size = []
#         for i in range(1,6):
#             list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
#             heap = MinHeapTable()
#             start_time = time.perf_counter()
#             heap._ajout_iteratif(list_of_values)
#             end_time = time.perf_counter()
#             list_of_times_for_size.append(end_time - start_time)
#         list_of_times.append(np.mean(list_of_times_for_size))
#     return list_of_times

# list_of_times = moyenne_temps_ajoutIteratif_table(list_of_sizes)
# # plt.clf()
# plt.plot(list_of_sizes, list_of_times)
# # make the x axis logarithmic but don't write 10^3, 10^4, 10^5, 10^6, 10^7, 10^8	
# plt.xlabel("taille de la lste")
# plt.ylabel("temps d'ajout")
# plt.title("temps d'ajout_table en fonction de la taille de la liste")
# # plt.show()
# # Apply the custom formatter to the y-axis
# # plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(format_func))
# plt.savefig("experiments/temps_d_ajoutIteratif_table.png")

# def moyenne_temps_ajoutIteratif_tree(list_of_sizes):
#     list_of_times = []
#     for size in list_of_sizes:
#         list_of_times_for_size = []
#         for i in range(1,6):
#             list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
#             heap = MinHeapBinaryTree()
#             start_time = time.perf_counter()
#             heap.ajout_iteratif(list_of_values)
#             end_time = time.perf_counter()
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
# # plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(format_func))
# plt.savefig("experiments/temps_d_ajout_tree.png")


# # le test d'union fait les tests suivant :
# # pour une taille de liste donnée,exemple 1000, fait jeu1 union jeu2, jeu2 union jeu3, jeu3 union jeu4 et jeu4 union jeu5
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

list_of_times = moyenne_temps_union_table(list_of_sizes)
plt.clf()
plt.plot(list_of_sizes, list_of_times)
plt.xlabel("taille de la lste")
plt.ylabel("temps d'union")
plt.title("temps d'union_table en fonction de la taille de la liste")
# plt.show()
plt.savefig("experiments/temps_d_union_table.png")



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

list_of_times = moyenne_temps_union_tree(list_of_sizes)
plt.clf()
plt.plot(list_of_sizes, list_of_times)
plt.xlabel("taille de la lste")
plt.ylabel("temps d'union")
plt.title("temps d'union_tree en fonction de la taille de la liste")
# plt.show()
plt.savefig("experiments/temps_d_union_tree.png")