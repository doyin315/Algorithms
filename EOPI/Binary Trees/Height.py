class Node(object):
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
 
    def insert(self,n):
        if self.data:
            if n<self.data:
                if not self.left:
                    self.left=Node(n)
                else:
                    self.left.insert(n)
            else:
                if not self.right:
                    self.right=Node(n)
                else:
                    self.right.insert(n)
        else:
            self.data=n


def inorder(node):
    res=[]
    if node:
        res=inorder(node.left)
        res.append(node.data)
        res+=inorder(node.right)
    
    return res

def Preorder(node):
    res=[]
    if node:
        res.append(node.data)
        res+=inorder(node.left) 
        res+=inorder(node.right)
    return res

def Postorder(node):
    res=[]
    if node:
        res=inorder(node.left)
        res+=inorder(node.right)
        res.append(node.data)

    return res

def height(tree):
    if not tree:
        return -1

    left=height(tree.left)
    right=height(tree.right)

    h=max(left,right)+1

    return h






root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(40)
root.insert(72)
root.insert(100)

print(inorder(root))
print(Preorder(root))
print(Postorder(root))
# print(root.Inorder(root))

# root.PrintTree()

print(height(root))

