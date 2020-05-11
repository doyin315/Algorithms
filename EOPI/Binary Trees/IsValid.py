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


root = Node(10)
root.insert(5)
root.insert(15)
root.insert(6)
root.insert(20)


def isValidBST(root):
    if not root or not root.left and not root.right:
        return True
    if root.left and root.right:
        return root.data>root.left.data and root.data<root.right.data and isValidBST(root.left) and isValidBST(root.right)
    if root.left and not root.right:
        return root.data>root.left.data
    else:
        return root.data<root.right.data

print(isValidBST(root))


