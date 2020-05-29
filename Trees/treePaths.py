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


    
# # root=Node(3)
# # root.insert(1)
# # root.insert(5)
# # root.insert(6)
# root=Node(12)
# root.insert(8)
# root.insert(9)
# root.insert(10)

root=Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(8)
root.insert(13)
root.insert(16)


def paths(tree):
    def helper(node):
        if not node:
            return [""]
        left = helper(node.left)
        right=helper(node.right)

        if left[0]=="" and right[0]=="" :
            return  [str(node.val)+""]

        if left[0]!="" and right[0]!="":
            return  [str(node.val)+'->'+i for i in left]+[str(node.val)+'->'+i for i in right]

        if left[0]=="":
            left=None
        else:
            right = None
        return  [str(node.val)+'->'+i for i in left or right]

    return helper(tree)


print(paths(root))