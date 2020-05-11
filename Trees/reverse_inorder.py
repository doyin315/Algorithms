class Node(object):
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None 



def preOrder(node): 
    if not node: 
        return      
    preOrder(node.left) 
    print(node.data)
    preOrder(node.right)   


def gen(arr):
    if not arr:
        return None
    mid= len(arr)//2
    node=Node(arr[mid])
    node.left=gen(arr[:mid])
    node.right=gen(arr[mid+1:])
    return node

l=[1,2,3,4,5,6]
preOrder(gen(l))




# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# def sorted_array_to_bst(nums):
#     if not nums:
#         return None
#     mid_val = len(nums)//2
#     node = TreeNode(nums[mid_val])
#     node.left = sorted_array_to_bst(nums[:mid_val])
#     node.right = sorted_array_to_bst(nums[mid_val+1:])
#     return node

# def preOrder(node): 
#     if not node: 
#         return      
#     preOrder(node.left) 
#     print(node.val)
#     preOrder(node.right)   
    
# result = sorted_array_to_bst([1, 2, 3, 4, 5, 6, 7])
# preOrder(result)