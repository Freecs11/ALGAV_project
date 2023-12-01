import copy
from math import log2
from queue import LifoQueue
from collections import deque
import structures as st


class BinomialNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0  
        self.parent = None
        self.childs = deque()  # Ensemble des fils
        
    # toString
    def __str__(self):
        description = "{key: " + str(self.key) + ", degree: " + str(self.degree)  + ", childs: " 
        for child in self.childs:
            description += str(child) + " *"+str(self.key)+"*, "
        return description+ "}\n"

class BinomialHeap:
    # def __init__(self, root_key):
    #     self.root = BinomialNode(root_key)
    #     self.size = 0
    #     self.left = None
    #     self.right = None
        
    def __init__(self):
        self.root = None
        self.size = 0
        self.left = None
        self.right = None

    def __str__(self):
        descrition =  "Heap -> root: " + str(self.root) + ", size: " + str(self.size) + ", left: "
        if self.left is None:
            descrition += "None"
        else:
            descrition += str(self.left.root.key)
        descrition += ", right: "
        if self.right is None:
            descrition += "None"
        else:
            descrition += str(self.right.root.key)
        return descrition
        
    def estVide(self):
        return self.root is None
    
    def init(self, node):
        self.root = node
        self.size = 2 ** node.degree
        self.left = None
        self.right = None
        return self
    
    def minimum (self):
        return self.root.key
    
    def _ajout_iteratif(self, list_values):
        list_values = deque(sorted(list_values))
        if len(list_values) == 0:
            return
        length = len(list_values)
        self.root = BinomialNode(list_values.popleft())
        self.size = length
        self.root.degree = int(log2(length))
        self.__ajout(self.root, list_values, self.root.degree)
        
        return self
    
    def __ajout(self, node, list_values, degree):
        if degree == 0:
            return
        else:
            node.degree = degree
            for i in range(degree):
                child = BinomialNode(list_values.popleft())
                child.parent = node
                node.childs.append(child)
                self.__ajout(child, list_values, degree - i - 1)
        
        return self
                
        
    def (self, list_values):
        
            
    def union2Tid(self, other_tree):
        if other_tree is None:
            raise ValueError("union avec un tas vide")
        if self.root.degree != other_tree.root.degree:
            raise ValueError("union avec un tas de degré différent")
        if self.root.key > other_tree.root.key:
            self.root, other_tree.root = other_tree.root, self.root
        other_tree.root.parent = self.root
        self.root.childs.appendleft(other_tree.root)
        self.root.degree += 1
        self.size += other_tree.size
        
        return self

    def degre(self):
        return self.root.degree

    def decapite(self):
        binomialQueue = BinomialQueue()
        # binomialQueue.minimum = self.root
        binomialQueue.size = 2 ** self.root.degree - 1
        copybinomialQueue = copy.deepcopy(self)
        newBinomialHeap = BinomialHeap()
        # s'il n'y a qu'un seul noeud dans le tas
        if self.root.degree == 0:
            binomialQueue.firstNode = None
            binomialQueue.lastNode = None
            binomialQueue.minimum = None
            return binomialQueue
        # s'il y a plus d'un noeud dans le tas
        binomialQueue.firstNode = newBinomialHeap.init(copybinomialQueue.root.childs.popleft())
        lastNode = binomialQueue.firstNode
        binomialQueue.minimum = lastNode
        for child in copybinomialQueue.root.childs:
            binomialHeapChild = BinomialHeap()
            binomialHeapChild.init(child)
            if child.key < binomialQueue.minimum.root.key:
                binomialQueue.minimum = binomialHeapChild
            lastNode.right = binomialHeapChild
            binomialHeapChild.left = lastNode
            lastNode = binomialHeapChild
        lastNode.right = None
        binomialQueue.lastNode = lastNode

        return binomialQueue
        
    def file(self):
        binomialQueue = BinomialQueue()
        return binomialQueue.ajoutMin(self)
        
class BinomialQueue:
    def __init__(self):
        self.firstNode = None
        self.lastNode = None
        self.minimum = None
        self.size = 0
        
    def __str__(self):
        if self.estVide():
            return "Queue -> \nfirstNode: None, \nlastNode: None, \nminimum: None, \nsize: " + str(self.size)
        
        description =  "Queue -> \nfirstNode: " + str(self.firstNode.root.key) + ", \nlastNode: " + str(self.lastNode.root.key) + ", \nminimum: " + str(self.minimum.root.key) + ", \nsize: " + str(self.size)
        node = self.firstNode
        description += "\n"
        while node.right is not None:
            description +=  str(node.root.key) +":"+ str(node.size) + " -> "
            node = node.right
        description +=  str(node.root.key) +":"+ str(node.size) + "\n"
        return description
    
    def estVide(self):
        return self.size == 0
        
    def minDeg(self):
        if self.estVide():
            raise ValueError("Le tournoi est vide")
        return self.lastNode

    def reste(self):
        if self.estVide():
            raise ValueError("Le tournoi est vide")
        self.removeNode(self.lastNode)
        return self
    
    def removeNode(self, node):
        if node.left is None and node.right is None:
            self.firstNode = None
            self.lastNode = None
            self.minimum = None
            self.size = 0
            return self
        elif node.left is None:
            self.firstNode = node.right
            self.firstNode.left = None
        elif  node.right is None:
            self.lastNode = node.left
            self.lastNode.right = None
        else:
            node.left.right = node.right
            node.right.left = node.left
        self.size -= node.size
        return self
    
    def ajoutMin(self, minDeg):
        if  self.lastNode and self.lastNode.degre() <= minDeg.degre():
            raise ValueError("Le degré du dernier arbre est inférieur ou égal au degré de l'arbre à ajouter")
        
        if self.estVide():
            self.firstNode = minDeg
            self.lastNode = minDeg
            self.minimum = minDeg
            self.size = minDeg.size
        else:
            self.lastNode.right = minDeg
            minDeg.left = self.lastNode
            self.lastNode = minDeg
            self.size += minDeg.size
            if self.minimum is None or minDeg.root.key < self.minimum.root.key:
                self.minimum = minDeg
        
        return self
    
    ''' cette fonction supprime le minimum de la file'''
    def supprMin(self):
        if self.minimum is None:
            raise ValueError("suppression min sur un tournoi vide")
        res = self.removeNode(self.minimum).union(self.minimum.decapite())
        # replace self with res of union
        self.minimum = res.minimum
        self.firstNode = res.firstNode
        self.lastNode = res.lastNode
        self.size = res.size
        # update minimum
        node = self.firstNode
        self.minimum = node
        while node is not None:
            if node.root.key < self.minimum.root.key:
                self.minimum = node
            node = node.right
        return self
    
    ''' cette fonction ajoute un tournoi binomial a la file '''
    def ajout(self, binomialHeap):        
        if binomialHeap is None:
            raise ValueError("ajout d'un tournoi vide")
        res = self.union(binomialHeap.file())
        self.firstNode = res.firstNode
        self.lastNode = res.lastNode
        self.minimum = res.minimum
        self.size = res.size
        return self
        

    # def ajout(self, binomialHeap):
    #     if binomialHeap is None:
    #         raise ValueError("ajout d'un tournoi vide")
        
    #     if self.estVide():
    #         self.firstNode = binomialHeap
    #         self.lastNode = binomialHeap
    #         self.minimum = binomialHeap
    #         self.size = binomialHeap.size
    #     elif self.lastNode.degree() > binomialHeap.degree():
    #         self.AjoutMin(binomialHeap)
    #     else:
    #         node = self.firstNode
    #         while node and node.degree() > binomialHeap.degree():
    #             node = node.right
            
    #         if node.degree() == binomialHeap.degree():
    #             self.removeNode(node) 
    #             # on ajoute la fusion des deux tournois
    #             binomialHeap.union2Tid(node)
    #             self.ajout(binomialHeap)
    #         else:
    #             binomialHeap.left = node.left
    #             binomialHeap.right = node
    #             node.left.right = binomialHeap
    #             node.left = binomialHeap
    #             self.size += binomialHeap.size
    #             if self.minimum is None or binomialHeap.root.key < self.minimum.root.key:
    #                 self.minimum = binomialHeap
    #             if binomialHeap.left is None:
    #                 self.firstNode = binomialHeap
        # 
        # return self
    
    def construction(self, list):
        for value in list:
            binomialHeap = BinomialHeap()
            res = self.ajout(binomialHeap._ajout_iteratif([value]))
            self.firstNode = res.firstNode
            self.lastNode = res.lastNode
            self.minimum = res.minimum
            self.size = res.size
        return self
    
    ''' cette fonction permet de fusionner cette file avec une autre file '''
    def union(self, binomialQueue):
        if binomialQueue is None:
            raise ValueError("union avec un tournoi vide")
        
        return self.uFret(binomialQueue, BinomialHeap())
    
    ''' cette fonction permet de fusionner cette file avec une autre file et un tas binomial en retenue '''
    def uFret(self, binomialQueue, binomialHeap):
        if binomialHeap.estVide():  # Pas de tournoi en retenue
            if self.estVide():
                return binomialQueue
            if binomialQueue.estVide():
                return self

            T1 = self.minDeg()
            T2 = binomialQueue.minDeg()

            if T1.degre() < T2.degre():
                return self.reste().union(binomialQueue).ajoutMin(T1)
            if T2.degre() < T1.degre():
                return binomialQueue.reste().union(self).ajoutMin(T2)

            if T1.degre() == T2.degre():
                return self.reste().uFret(binomialQueue.reste(), T1.union2Tid(T2))
        else:
            if self.estVide():
                return binomialHeap.file().union(binomialQueue)
            if binomialQueue.estVide():
                return binomialHeap.file().union(self)
            
            T1 = self.minDeg()
            T2 = binomialQueue.minDeg()
            
            if binomialHeap.degre() < T1.degre() and binomialHeap.degre() < T2.degre():
                return self.union(binomialQueue).ajoutMin(binomialHeap)
            if binomialHeap.degre() == T1.degre() and binomialHeap.degre() == T2.degre():
                return self.reste().uFret(binomialQueue.reste(), T1.union2Tid(T2)).ajout(binomialHeap)
            if binomialHeap.degre() == T1.degre() and binomialHeap.degre() < T2.degre():
                return self.reste().uFret(binomialQueue, T1.union2Tid(binomialHeap))
            if binomialHeap.degre() == T2.degre() and binomialHeap.degre() < T1.degre():
                return binomialQueue.reste().uFret(self, T2.union2Tid(binomialHeap))
