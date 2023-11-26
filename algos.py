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
        self.completed = False
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
            node.left = new_node
            self.root.deepest = new_node
            self._heapify(new_node)
        elif node.right is None:
            new_node.parent = node
            node.right = new_node
            node.completed = True
            self._heapify(new_node)
        else:
            if not node.left.completed:
                self._ajout(node.left, new_node)
            elif not node.right.completed:
                self._ajout(node.right, new_node)
            else:
                self._ajout(node.left, new_node)
                

    def _heapify(self, node):
        while node.parent is not None and st.sup(node.parent.value , node.value):
            self._swap(node, node.parent)
            node = node.parent
            
    def _heapify_down(self, node):
        while node.left is not None:
            if node.right is None:
                if st.sup(node.value, node.left.value):
                    self._swap(node, node.left)
                break
            else:
                if st.sup(node.left.value, node.right.value):
                    if st.sup(node.value, node.right.value):
                        self._swap(node, node.right)
                        node = node.right
                    else:
                        break
                else:
                    if st.sup(node.value, node.left.value):
                        self._swap(node, node.left)
                        node = node.left
                    else:
                        break
                    
            
    def _suppmin(self):
        if self.root is None:
            return None
        else:
            return self._supp(self.root)
    
    def _supp(self, node):
        deepest = node.deepest
        mins = node.value

        if deepest.parent is not None and  deepest.parent.left == deepest:
            deepest.parent.left = None
        else:
            if deepest.parent is not None:
                deepest.parent.right = None
                deepest.parent.completed = False  # Add this line
            else:
                self.root = None
        self.size -= 1
        node.value = deepest.value
        node.deepest = deepest.parent
        self._heapify_down(node)
        return mins
        

    
        
    def _ajout_iteratif(self, list_values):
        for value in list_values:
            self.ajout(value)

    def _swap(self, node1, node2):
        node1.value, node2.value = node2.value, node1.value


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
            
    



exem = MinHeapBinaryTree()
listofvalues = st.treat_from_file("cles_alea/jeu_1_nb_cles_1000.txt")
# exem._ajout_iteratif(listofvalues)
# exem.print_heap()
# print("min : " +str(exem._suppmin()) + "\n\n") 


class MinHeapTable:
    def __init__(self):
        self.heap = []
        self.size = 0
        self.FRONT = 1
        
    def parent(self, pos):
        return pos // 2
    
    def leftChild(self, pos):
        return 2 * pos 
    
    def rightChild(self, pos):
        return (2 * pos) + 1
    
    def isLeaf(self, pos):
        return pos >= (self.size // 2) and pos <= self.size
    
    
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

    def ajout(self, element):
        self.size += 1
        self.heap.append(element)
        current = self.size - 1
        # while self.heap[current] < self.heap[self.parent(current)]:
        while st.inf(self.heap[current], self.heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)
    
    def minHeap(self):
        for pos in range((self.size // 2), -1, -1):  # goes from half of the size to 0 
            self._heapify(pos)
            
    def _ajout_iteratif(self, list_values):
        for value in list_values:
            self.ajout(value)
            
    def _suppmin(self):
        popped = self.heap[self.FRONT]
        self.heap[self.FRONT] = self.heap[self.size-1]
        self.size -= 1
        self.heap.pop()
        self._heapify(self.FRONT)
        return popped
    
    def print_heap(self):
        for i in range(0, self.size):
            print(self.heap[i], end=" \n")             
    
        
heap_ex = MinHeapTable()
heap_ex._ajout_iteratif(listofvalues)


print("min : " +str(heap_ex._suppmin()) + "\n\n")
# (13784548702449909963, 17644899806406222366)
# (8365161608125828369, 9394554881227400599)
# (12629357224835867491, 9869174147496533916)
# (6242588491462870437, 8850496006118104447)
# last element : (6242588491462870437, 8850496006118104447)


# Donner le pseudo code de la fonction avec des explications puis l’implémenter
    # pseudo code
    # build_heap(keys):
    #    V = tas_vide()
    #    V.heap = keys
    #    V.size = length(keys)
    #    pour i de length(keys) // 2 à 0:
    #        V._heapify(i)
    #    return V
def build_heap_table(keys):
    heap = MinHeapTable()
    heap.heap = keys[:]
    print("len : " + str(len(keys)))
    heap.size = len(keys) 
    heap.minHeap()
    return heap

# je ne vois pas comment faire un build_heap_tree sans avoir une fonction qui permet de
# construire un arbre à partir d'une liste de valeurs ce qui revient à faire un ajout itératif
def build_heap_tree(keys):
    heap = MinHeapBinaryTree()
    heap._ajout_iteratif(keys)
    return heap
    


ex = build_heap_table(listofvalues)
ex.print_heap()
print("last element : " + str(ex.heap[ex.size-1]) + "\n\n")
print("min : " +str(ex._suppmin()) + "\n\n")


# il manque la gestion de l'implémentation de la fonction Union pour la classe MinHeapBinaryTree
def Union (heap1, heap2, _class = MinHeapTable):
    heap = _class()
    heap.heap = heap1.heap[:] + heap2.heap[:]
    heap.size = heap1.size + heap2.size
    heap.minHeap()
    return heap

heap1 = build_heap_table(listofvalues)
l = st.treat_from_file("cles_alea/jeu_4_nb_cles_1000.txt")
heap2 = build_heap_table(l)
heap3 = Union(heap1, heap2)
heap3.print_heap()
print("len heap1 : " + str(heap1.size) + "\n\n")
print("len heap2 : " + str(heap2.size) + "\n\n")
print("len heap3 : " + str(heap3.size) + " should be : " + str(heap1.size + heap2.size) + "\n\n") 
print("min heap2: " +str(heap2._suppmin()) + "\n\n")
print("min heap1: " +str(heap1._suppmin()) + "\n\n")

print("min heap3: " +str(heap3._suppmin()) + "\n\n")





list_of_sizes = [1000, 5000 ,10000, 20000, 50000, 80000, 120000 ,200000]

def moyenne_temps_construction(list_of_sizes):
    list_of_times = []
    for size in list_of_sizes:
        list_of_times_for_size = []
        for i in range(1,6):
            list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
            start_time = time.time()
            build_heap_table(list_of_values)
            end_time = time.time()
            list_of_times_for_size.append(end_time - start_time)
        list_of_times.append(np.mean(list_of_times_for_size))
    return list_of_times

list_of_times = moyenne_temps_construction(list_of_sizes)
plt.plot(list_of_sizes, list_of_times)
plt.xlabel("taille de la lste")
plt.ylabel("temps de construction")
plt.title("temps de construction en fonction de la taille de la liste")
plt.show()


# On remarque que le temps de construction est linéaire en fonction de la taille de la liste
# ce qui est cohérent avec la complexité théorique de la fonction build_heap qui est O(n)
# On remarque aussi que le temps de construction est plus important pour les petites listes
# que pour les grandes listes
# Cela est dû au fait que la fonction build_heap fait appel à la fonction minHeap qui
# parcourt les noeuds de l'arbre des la fin vers le début et qui effectue des heapify
# ce qui prend plus de temps pour les petits arbres que pour les grands arbres


def moyenne_temps_suppression(list_of_sizes):
    list_of_times = []
    for size in list_of_sizes:
        list_of_times_for_size = []
        for i in range(1,6):
            list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
            heap = build_heap_table(list_of_values)
            start_time = time.time()
            heap._suppmin()
            end_time = time.time()
            list_of_times_for_size.append(end_time - start_time)
        list_of_times.append(np.mean(list_of_times_for_size))
    return list_of_times

list_of_times = moyenne_temps_suppression(list_of_sizes)
plt.plot(list_of_sizes, list_of_times)
plt.xlabel("taille de la lste")
plt.ylabel("temps de suppression")
plt.title("temps de suppression en fonction de la taille de la liste")
plt.show()


def moyenne_temps_union(list_of_sizes):
    list_of_times = []
    for size in list_of_sizes:
        list_of_times_for_size = []
        for i in range(1,6):
            list_of_values1 = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
            list_of_values2 = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
            heap1 = build_heap_table(list_of_values1)
            heap2 = build_heap_table(list_of_values2)
            start_time = time.time()
            Union(heap1, heap2)
            end_time = time.time()
            list_of_times_for_size.append(end_time - start_time)
        list_of_times.append(np.mean(list_of_times_for_size))
    return list_of_times

list_of_times = moyenne_temps_union(list_of_sizes)
plt.plot(list_of_sizes, list_of_times)
plt.xlabel("taille de la lste")
plt.ylabel("temps d'union")
plt.title("temps d'union en fonction de la taille de la liste")
plt.show()


def moyenne_temps_ajout(list_of_sizes):
    list_of_times = []
    for size in list_of_sizes:
        list_of_times_for_size = []
        for i in range(1,6):
            list_of_values = st.treat_from_file("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(size)+".txt")
            heap = build_heap_table(list_of_values)
            start_time = time.time()
            heap._ajout_iteratif(list_of_values)
            end_time = time.time()
            list_of_times_for_size.append(end_time - start_time)
        list_of_times.append(np.mean(list_of_times_for_size))
    return list_of_times

list_of_times = moyenne_temps_ajout(list_of_sizes)
plt.plot(list_of_sizes, list_of_times)
plt.xlabel("taille de la lste")
plt.ylabel("temps d'ajout")
plt.title("temps d'ajout en fonction de la taille de la liste")
plt.show()





