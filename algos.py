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

    def ajout(self, value):
        if self.root is None:
            self.root = MinHeapNode(value)
        else:
            self._ajout(self.root, MinHeapNode(value))

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
            self.root.deepest = new_node
            self._heapify(new_node)
        else:
            if not node.left.completed:
                self._ajout(node.left, new_node)
            elif not node.right.completed:
                self._ajout(node.right, new_node)
            else:
                self._ajout(node.left, new_node)
                

    def _heapify(self, node):
        while node.parent is not None and node.parent.value > node.value:
            self._swap(node, node.parent)
            node = node.parent
            
    def _heapify_down(self, node):
        while node.left is not None or node.right is not None:
            if node.left is not None and node.right is not None:
                if node.left.value < node.right.value:
                    if node.value > node.left.value:
                        self._swap(node, node.left)
                        node = node.left
                    else:
                        break
                else:
                    if node.value > node.right.value:
                        self._swap(node, node.right)
                        node = node.right
                    else:
                        break
            elif node.left is not None:
                if node.value > node.left.value:
                    self._swap(node, node.left)
                    node = node.left
                else:
                    break
            else:
                if node.value > node.right.value:
                    self._swap(node, node.right)
                    node = node.right
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
        
        if deepest.parent.left == deepest:
            deepest.parent.left = None
        else:
            deepest.parent.right = None
        node.value = deepest.value
        node.deepest = deepest.parent
        self._heapify_down(node)
        
        return node.value
        
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



heap_ex = MinHeapBinaryTree()
heap_ex.ajout(10)
heap_ex.ajout(35)
heap_ex.ajout(33)
#heap_ex.print_heap()
heap_ex.ajout(42)
# heap_ex.print_heap()
heap_ex.ajout(10)
heap_ex.ajout(14)
heap_ex.ajout(19)
#heap_ex.print_heap()
heap_ex.ajout(27)
heap_ex.ajout(44)
heap_ex.ajout(26)
heap_ex.ajout(31)
heap_ex.print_heap() # 10 10 14 27 26 33 19 42 44 35 31

print("min : " +str(heap_ex._suppmin()) + "\n\n") # 10
heap_ex.print_heap() # 10 26 14 27 31 33 19 42 44 35


class MinHeapTable :
    def __init__(self):
        self.heap = []
        self.size = 0

    def ajout(self, value):
        self.heap.append(value)
        self.size += 1
        self._heapify_up(self.size - 1)

    def _heapify_up(self, index):
        while index != 0 and self.heap[self._parent(index)] > self.heap[index]:
            self._swap(index, self._parent(index))
            index = self._parent(index)

    def _heapify_down(self, index):
        while self._left(index) < self.size:
            if self._right(index) < self.size:
                if self.heap[self._left(index)] < self.heap[self._right(index)]:
                    if self.heap[index] > self.heap[self._left(index)]:
                        self._swap(index, self._left(index))
                        index = self._left(index)
                    else:
                        break
                else:
                    if self.heap[index] > self.heap[self._right(index)]:
                        self._swap(index, self._right(index))
                        index = self._right(index)
                    else:
                        break
            else:
                if self.heap[index] > self.heap[self._left(index)]:
                    self._swap(index, self._left(index))
                    index = self._left(index)
                else:
                    break

    def _suppmin(self):
        if self.size == 0:
            return None
        else:
            self._swap(0, self.size - 1)
            self.size -= 1
            self._heapify_down(0)
            return self.heap.pop()

    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return 2 * index + 1

    def _right(self, index):
        return 2 * index + 2
    
    def ajout_iteratif(self, list_values):
        for value in list_values:
            self.ajout(value)

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def print_heap(self):
        print(self.heap)
        

heap_ex = MinHeapTable()
heap_ex.ajout_iteratif([10, 35, 33, 42, 10, 14, 19, 27, 44, 26, 31])
print("final : \n" )
heap_ex.print_heap()
print("min : " +str(heap_ex._suppmin()) + "\n") # 10
heap_ex.print_heap() # 10 26 14 27 31 33 19 42 44 35
