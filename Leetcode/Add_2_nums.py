class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

a=ListNode(3)
b=ListNode(3)
# c=ListNode(9)
a.next=b
# b.next=c

d=ListNode(1)
e=ListNode(4)
d.next=e


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    head=l1
    rem=0
    while l1 and l2:
        l1.val+=l2.val+rem
        rem=l1.val//10
        l1.val%=10
        if not l1.next and not l2.next and rem:
            l1.next=ListNode(rem)
            l1=l1.next.next
            l2=l2.next
            rem=0
            break
        if not l1.next and l2.next:
            l2=l2.next
            break
        l1=l1.next
        l2=l2.next
    
    while l1 and not l2:
        l1.val+=rem
        rem=l1.val//10
        l1.val%=10
        if not l1.next and rem:
                l1.next=ListNode(rem)
                break
        l1=l1.next
        
    while l2:
        print("l2 remains")
        l2.val+=rem
        rem=l2.val//10
        l2.val%=10
        l1.next=ListNode(l2.val)
        if not l2.next and rem:
                l1.next.next=ListNode(rem)
                rem=0
                break
        l1=l1.next
        l2=l2.next 
    while head:
        print(head.val)
        head=head.next
    return head

addTwoNumbers(d,a)

            #     break
            # elif not l1.next and l2.next:
            #     l1.next=ListNode(rem+l2.next.val)
            #     break
            # elif l1.next and not l2.next:
            #     l1.next.val+=rem
            #     break 