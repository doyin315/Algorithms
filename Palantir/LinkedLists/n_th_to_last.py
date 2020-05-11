class Node(object):

    def __init__(self, value):
        self.value= value
        self.nextnode =None 

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
a.nextnode=b
b.nextnode=c
c.nextnode=d
d.nextnode=e

# from collections import defaultdict
# def nlast(n,node):
#     d=defaultdict(int)
#     left=node
#     count=0
#     while node:
#         d[count]=node
#         node=node.nextnode
#         count+=1
#     return d[len(d)-n].value

# print(nlast(2,a))

def n_last(n,node):
    left=node 
    right= node 

    for _ in range(n-1):
        if not right.nextnode:
            raise LookupError("Node not long enough")

        right= right.nextnode

    while right.nextnode:
        left= left.nextnode
        right = right.nextnode
    
    return left.value

print(n_last(2,a))


