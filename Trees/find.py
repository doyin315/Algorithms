class Node(object):
    def __init__(self,data):
        self.data=data
        self.left= None
        self.right= None

    def insert(self,data):
        if self.data:
            if data< self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            elif data > self.data:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data=data
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
    
root=Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()
