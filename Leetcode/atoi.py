from math import floor,pow
def atoi(s):
    store="-0123456789"
    new=""
    s=s.strip()
    if len(s)==0:
        return 0
    elif s[0] not in store:
        return 0
    else:
        for i in s:
            if i in store:
                new+=i
            else:
                break
    if int(new)>(pow(2,31))-1:
        return floor((pow(2,31))-1)
    elif int(new)<(0-(pow(2,31))-1):
        return floor((0-(pow(2,31))))
    else:
        return int(new)
        
# print(atoi("-91283472332")) 

# print(pow(2,31)-1)
