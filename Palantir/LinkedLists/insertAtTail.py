
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    node=head
    if not head:
        head=SinglyLinkedListNode(data)
        return head
    while True:
        if node.next==None:
            node.next=SinglyLinkedListNode(data)
            break
        node=node.next
    
    return head


a=SinglyLinkedListNode(1)
b=SinglyLinkedListNode(2)
c=SinglyLinkedListNode(3)
a.next=b
b.next=c

print(insertNodeAtTail(a,4))
print(a.next.next.next.data)