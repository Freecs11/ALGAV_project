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
            return False
        if node.right is not None and st.sup(node.value , node.right.value):
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


class MinHeapTable:
    def __init__(self):
        self.heap = []
        self.size = 0
        
    def parent(self, pos):
        return (pos - 1) // 2  
    
    def leftChild(self, pos):
        return 2 * pos + 1  
    
    def rightChild(self, pos):
        return 2 * pos + 2  
    
    def isLeaf(self, pos):
        return pos >= (self.size // 2)  
    
    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]
        
    def _heapify_down(self, pos):
        while not self.isLeaf(pos):
            leftChild = self.leftChild(pos)
            rightChild = self.rightChild(pos)
            smallest = pos 
            
            if leftChild < self.size and st.inf(self.heap[leftChild], self.heap[smallest]):
                smallest = leftChild
                
            if rightChild < self.size and st.inf(self.heap[rightChild], self.heap[smallest]):
                smallest = rightChild
                
            if smallest != pos:
                self.swap(pos, smallest)
                self._heapify_down(smallest)
                
            else:
                break
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
        for pos in range((self.size // 2) - 1, -1, -1):  
            self._heapify_down(pos)
            
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
        self.size = len(keys) 
        self.minHeap()
        return self    



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
    heap.construction(list_heap1 + list_heap2)
    heap.size = heap1.size + heap2.size
    return heap
