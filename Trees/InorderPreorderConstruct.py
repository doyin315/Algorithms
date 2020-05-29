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


preOrder=[3,9,20,15,7]
testint=[1,2,3,4,5,6]
Inorder=[9,3,15,20,7]

def inTrav(nums):
    if nums:
        left = 0
        right = len(nums)-1
        mid = left + ((right-left)//2)

        node=Node(nums[mid])
        node.left=inTrav(nums[:mid])
        node.right=inTrav(nums[mid+1:])

        return node

def printTree(node):
    if node:
        if node.left:
            printTree(node.left)
        print(node.data)
        if node.right:
            printTree(node.right)

test=inTrav(Inorder)

printTree(test)