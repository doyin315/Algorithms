class Node(object):

    def __init__(self, value):
        self.value= value
        self.nextnode =None 

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
a.nextnode=b
b.nextnode=c
c.nextnode=d

def reverse(node):
    current=node
    nextnode= None
    prev=None 
    while current:
        nextnode = current.nextnode
        current.nextnode=prev

        prev=current
        current= nextnode
    return prev

reverse(a)



