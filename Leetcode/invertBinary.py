class Node(object):
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
 
    def insert(self,n):
        if self.val:
            if n<self.val:
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
            self.val=n

class ListNode:
    def __init__(self,val=0, nextnode=None):
        self.val=val
        self.next=nextnode



root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(40)


def invertTree(root):
    
    def invert(node1,node2):
        if not root:
            return root
      
        left = invert(root.left)
        right = invert(root.right)
        
        root.left = right
        root.right = left
        
        return root
        
def inorder(node):
    res=[]
    if node:
        res=inorder(node.left)
        res.append(node.val)
        res+=inorder(node.right)
    
    return res

print(inorder(root))
invertTree(root)
print(inorder(root))
