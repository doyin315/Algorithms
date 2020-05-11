class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None 

    def insert(self,data):
        if self.data:
            if data< self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif data> self.data:
                if self.right is None:
                    self.right = Node(data)
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

def find(tree, x):
    if tree.data==x:
        return True
    elif x> tree.data:
        if tree.right != None:
            return find(tree.right,x)
    elif x< tree.data:
        if tree.left != None:
            return find(tree.left,x)

    return False

root=Node(12)
root.insert(6)
root.insert(14)
root.insert(3)


print(find(root,6))