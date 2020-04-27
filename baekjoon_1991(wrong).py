class Node:
    def __init__(self,key=None,parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key)

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self,v,m):
        if self.root == None:
            self.root = v
            print("alalal")
            print(self.root.key)

        else: 
            print(v.key)
            current = self.find(v,m)
            current = v


    def find(self,v,x):
        if x.key == v.key:
            return x
      
        else:
            self.find(v,x.left)
            self.find(v,x.right)


    def preorder(self,v):
        if (v.key!='.' and v!=None):
            print(self.key)
            self.preorder(v.left)
            self.preorder(v.right)

    def postorder(self,v):
        if (v.key!='.' and v!=None):
            self.postorder(v.left)
            self.postorder(v.right)
            print(self.key)

    def inorder(self,v):
        if (v.key!='.' and v!=None):
            self.inorder(v.left)
            print(self.key)
            self.inorder(v.right)


a = input()
a = int(a)
T = Tree()
current = Node(None)
for i in range(a):
    x,y,z=input().split(' ')
    L = Node(x)
    M = Node(y)
    N = Node(z)
    L.left = M
    M.parent = L
    L.right = N
    N.parent = L
    T.insert(L,T.root)
print(T.root.left.key)
#T.inorder(T.root)
#T.postorder(T.root)
#T.preorder(T.root)




             