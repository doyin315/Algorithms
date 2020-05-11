class Node(object):

    def __init__(self, value):
        self.value= value
        self.nextnode =None 



def insert(a,l):
    prev=a
    current=None 
    n=len(l)
    count=0
    while n:
        current=Node(l[count])
        prev.nextnode=current
        prev=current


        n-=1
        count+=1
a=Node(1)
l=[383,484,392,975,321]
insert(a,l)
print(a.nextnode.nextnode.value)

