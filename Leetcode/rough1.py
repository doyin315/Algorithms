class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
i=0
l=[1,2,3,4,5]
head=ListNode(l[i])
current=head
i+=1
while i<len(l):
    current.next=ListNode(l[i])
    i+=1
    current=current.next

current=head
arr=[]

