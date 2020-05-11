class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

a=SinglyLinkedListNode(1)
b=SinglyLinkedListNode(2)
c=SinglyLinkedListNode(3)

a.next=b
b.next=c
c.next=a

def has_cycle(head):
    l1=head
    l2=head

    while l2.next:
        l1=l1.next
        l2=l2.next.next
        if l1==l2:
            return True

    return False

print(has_cycle(a))

