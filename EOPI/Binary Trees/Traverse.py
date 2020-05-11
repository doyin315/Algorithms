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
from collections import namedtuple
BalancedStatusWithHeight = namedtuple('BalancedStatusWithHeight', ('balanced','height'))
def checkBalanced(Tree):
    if not Tree:
        return BalancedStatusWithHeight(True, -1)

    left=checkBalanced(Tree.left)
    if not left.balanced:
        return BalancedStatusWithHeight(False,0)
        
    right=checkBalanced(Tree.right)
    if not right.balanced:
        return BalancedStatusWithHeight(False,0)

    isbalanced=abs(left.height-right.height)<=1
    height=max(left.height,right.height)+1
    return BalancedStatusWithHeight(isbalanced,height)




# def balance(node):
#     if node:
#         if node.left and not node.right:
#             return balance(node.left)

#         elif node.right and not node.left:
#            return balance(node.right)
        
#         elif not node.right and not node.left:
#             return node

#     node.left=balance(node.left)
#     node.right=balance(node.right)
#     return node


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(40)

print(inorder(root))
print(Preorder(root))
print(Postorder(root))
# print(root.Inorder(root))

# root.PrintTree()

print(checkBalanced(root))