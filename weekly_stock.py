dp=[1,1,1,1,1,1,1,7,7,7,7,7,7,7]

def price(d):
    price=[]
    for i in range(len(d)-6):
        price.append(str(round((sum(d[i:i+7])/7),2)))
    print(price)
price(dp)

sample=[7,8,8,11,9,7,5,6]
price(sample)