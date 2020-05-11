class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
a.next=b
b.next=c

d=ListNode(2)
e=ListNode(3)
f=ListNode(4)

def view(node):
    res=[]
    while node:
        res.append(node.val)
        node=node.next
    print(res)

def merger(arr):
    def merge(l,r):
        head=ListNode(0)
        dummy=head

        while l and r:
            if l.val<=r.val:
                dummy.next=ListNode(l.val)
                dummy=dummy.next
                l=l.next
            else:
                dummy.next=ListNode(r.val)
                dummy=dummy.next
                r=r.next
        if l:
            dummy.next=l
        elif r:
            dummy.next=r

        return head

    if not arr:
        return 0
    elif len(arr)==1:
        return arr[0]
    
    mid=len(arr)//2
    l=merger(arr[:mid])
    r=merger(arr[mid:])
    
    return merge(l,r)


test=[a,d]

view(merger(test))
