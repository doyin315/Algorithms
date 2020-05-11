class Node(object):

    def __init__(self, value):
        self.value= value
        self.nextnode =None 

# a=Node(1)
# b=Node(2)
# c=Node(3)
# a.nextnode=b
# b.nextnode=c


# class DoublyLinkedListNode(object):
#     def __init__(self, value):
#         self.value =value
#         self.next_node =None 
#         self.prev_node=None 

# a=DoublyLinkedListNode(1)
# b= DoublyLinkedListNode(2)
# c= DoublyLinkedListNode(3)

# a.next_node=b
# b.prev_node=a
# b.next_node=c
# c.prev_node=b

def cycle(node):
    marker1=node
    marker2=node

    while marker2!=None and marker2.nextnode!=None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker1 == marker2:
            return True

    return False



a=Node(1)
b=Node(2)
c=Node(3)
a.nextnode=b
b.nextnode=c
c.nextnode = a

print(cycle(a))

