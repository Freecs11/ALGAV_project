#  Arbre de Recherche
# Implémenter une structure arborescente de recherche permettant, en moyenne, de savoir si un élément est contenu dans la structure de données en O(log n) comparaisons, où n est le nombre de clés
# stockées. On rappelle que les clés seront codées sur 128 bits
import structures as st

class node:
    
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

class search_tree:
    
    def __init__(self):
        self.root = None
        self.size = 0
        
    def insert(self, key):
        if self.root == None:
            self.root = node(key)
            self.size += 1
        else:
            self._insert(key, self.root)
        
    def _insert(self, key, cur_node):
        if st.inf(key , cur_node.key):
            if cur_node.left == None:
                cur_node.left = node(key)
                cur_node.left.parent = cur_node
                cur_node.left.height = cur_node.height + 1
                self.size += 1
            else:
                self._insert(key, cur_node.left)
        elif st.sup(key , cur_node.key):
            if cur_node.right == None:
                cur_node.right = node(key)
                cur_node.right.parent = cur_node
                cur_node.right.height = cur_node.height + 1
                self.size += 1
            else:
                self._insert(key, cur_node.right)
        else:
            print("Key already in tree!")
    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)
            
    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left)
            print(str(cur_node.key))
            self._print_tree(cur_node.right)
            
    def search(self, key):
        if self.root != None:
            return self._search(key, self.root)
        else:
            return False
    
    def _search(self, key, cur_node):
        if st.inf(key , cur_node.key) and cur_node.left != None:
            return self._search(key, cur_node.left)
        elif st.sup(key , cur_node.key) and cur_node.right != None:
            return self._search(key, cur_node.right)
        elif st.eg(key , cur_node.key):
            return True
        else:
            return False
    
    def toList(self):
        if self.root != None:
            return self._toList(self.root)
        else:
            return []
    # retourne une liste triée des clés de l'arbre et c'est un parcours infixe en O(n)
    def _toList(self, cur_node):
        if cur_node != None:
            return self._toList(cur_node.left) + [cur_node.key] + self._toList(cur_node.right)
        else:
            return []
        
        
        


# test
# tree = search_tree()

# for i in range(1000):
#     tree.insert(st.generate_key())
    

# # print(tree.toList())
# d = tree.list_of_lists()

# for i in range(len(d)):
#     print("level " + str(i) + " : ")
#     print("size = " + str(len(d[i])))
#     print(d[i])
    