class Node:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

class BST:
    def __init__(self):
        self.rt = None

    def findMin(self):
        if not self.rt:
            return None
        c = self.rt
        while c.l:
            c = c.l
        return c.v

    def findMax(self):
        if not self.rt:
            return None
        c = self.rt
        while c.r:
            c = c.r
        return c.v

#test
bst = BST()
bst.rt = Node(10)
bst.rt.l = Node(5)
bst.rt.r = Node(15)
bst.rt.l.l = Node(3)
print("Min:", bst.findMin())  
print("Max:", bst.findMax())  
