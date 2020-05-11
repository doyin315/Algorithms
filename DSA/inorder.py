class Node(object):
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

    def Inorder(self, root):
        res=[]
        if root:
            res= self.Inorder(root.left)
            res.append(root.data)
            res+= self.Inorder(root.right)
        return res


    def Preorder(self,root):
        res=[]
        if root:
            res.append(root.data)
            res+=self.Preorder(root.left)
            res+= self.Preorder(root.right)
        return res

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

print(root.Preorder(root))
# print(root.Inorder(root))

# root.PrintTree()

