class ListNode:
    def __init__(self,data=0, nextnode=None):
        self.data=data
        self.next=nextnode


def search_List(L,key):
    while L and L.data != key:
        L=L.next
    return L

def insert_after(node, new_node):
    new_node.next=node.next
    node.next=new_node

def delete_after(node):
    node.next=node.next.next

a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
a.next=b
b.next=c

d=ListNode(4)
e=ListNode(5)
f=ListNode(6)

def merge(l1,l2):
    tail=ListNode()

    while l1 and l2:
        if l1.data<l2.data:
            tail.next, l1 = l1,l1.next
        else:
            tail.next, l2 = l2,l2.next
        tail=tail.next
    tail.next= l1 or l2


def reverse(l):
    current=l
    nextnode=None
    prev=None

    while current!=None:
        nextnode = current.next
        current.next=prev

        prev=current
        current=nextnode
    return prev

reverse(a)
print(c.next.data)
