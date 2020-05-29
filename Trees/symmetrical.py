class Node(object):
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None 

    def insert(self,data):
        if self.data:
            if data < self.data:
                if not self.left:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            else:
                if not self.right:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def symmetry(self):
        def checker(root1,root2):
            if not root1 and not root2:
                return True
            elif root1 and root2:
                return root1.data==root2.data and  checker(root1.left,root2.right) and checker(root1.right,root2.left)
            return False
        if root:
            return checker(self.left,self.right)
        return False


    
root=Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(8)
root.insert(13)
root.insert(16)

print(root.symmetry())

