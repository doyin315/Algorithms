class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l= [1,2,3,4,5,6]
mid=len(l)//3
head=ListNode(l[mid])
current=head
mid+=1
while mid<len(l):
    current.next=ListNode(l[mid])
    mid+=1
    current=current.next

