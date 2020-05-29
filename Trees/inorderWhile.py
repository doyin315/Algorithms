class Node(object):
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None 

    def insert(self,val):
        if self.val:
            if val < self.val:
                if not self.left:
                    self.left=Node(val)
                else:
                    self.left.insert(val)
            else:
                if not self.right:
                    self.right=Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.val)
        if self.right:
            self.right.PrintTree()


    
root=Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(8)
root.insert(13)
root.insert(16)

def inorder(node):
    if not node:
        return []
    res=[]
    stack=[]
    while node or stack:
        while node:
            stack.append(node)
            node=node.left

        current = stack.pop()
        res.append(current.val)
        node=current.right
    return res

def validate()
print(inorder(root))