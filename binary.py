p=[1,2,3,4,5,6,7,8]

def bin(p,k):
    found=False
    if len(p)==0:
        return False
    else:
        start=0
        end=len(p)-1
        while not found and start<=end:
            mid=(start+end)//2
            if p[mid]==k:
                found=True
            elif p[mid]>k:
                return bin(p[:mid],k)
            else:
                return bin(p[mid+1:],k)