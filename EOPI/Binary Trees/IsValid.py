class Node(object):
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
 
    def insert(self,n):
        if self.val:
            if n<self.val:
                if not self.left:
                    self.left=Node(n)
                else:
                    self.left.insert(n)
            else:
                if not self.right:
                    self.right=Node(n)
                else:
                    self.right.insert(n)
        else:
            self.val=n

class ListNode:
    def __init__(self,val=0, nextnode=None):
        self.val=val
        self.next=nextnode



root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(40)


def isValidBST(root):
    if not root or not root.left and not root.right:
        return True
    if root.left and root.right:
        return root.val>root.left.val and root.val<root.right.val and isValidBST(root.left) and isValidBST(root.right)
    if root.left and not root.right:
        return root.val>root.left.val
    else:
        return root.val<root.right.val


def getLeafs(tree):
    res=[]
    def traverse(node):
        if not node:
            return True
        left = traverse(node.left) 
        right = traverse(node.right)

        if left and right:
            res.append(node.val)
    
    traverse(tree)
    head = ListNode(res[0])
    final=head
    i=1

    while i<len(res):
        final.next=ListNode(res[i])
        i+=1
        final=final.next
        
    return head

        


finalList=getLeafs(root)

print(finalList.val)
print(finalList.next.val)
print(finalList.next.next.val)
print(finalList.next.next.next.val)


