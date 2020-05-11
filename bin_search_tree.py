class treenode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

def create_bst(nums):
    if not nums:
        return None
    
    mid= len(nums)//2
    node= = treenode()