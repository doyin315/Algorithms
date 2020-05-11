        

def rotate(node,k):
    
    arr=[]
    
    while node:
        arr.append(node.val)
        node=node.next
    
    Newarr=[0]*len(arr)
    
    for i in range(len(arr)):
        i+=k
        temp=arr[i]
        if i>len(arr)-1:
            i%=len(arr)
        Newarr[i]=temp
    j=0
    head=ListNode(Newarr[j])
    current=head
    while j<len(Newarr):
        current.next=ListNode(Newarr[j])
        j+=1
        current=head.next
        
    return head
        
          