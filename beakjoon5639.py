class Node:
    def __init__(self,key):
        self.key = Key
        self.left = self.right = self.parent = None

    def __str__(self):
        return str(self.key)

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self,v):
        if v != None:
            print(v.key, end=' ')
            self.preorder(v.left)
            self.preorder(v.right)

    def insert(self,key1,key2,key3):

        




