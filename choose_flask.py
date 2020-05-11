def chooseFlask(requirements, markings):
    countings=[]
    count=0
    time=0
    store=set()
    bads=set()
    pending=False
    for i in range(len(markings)):
        shift=(len(markings)//3) + i -1
        if count==0 and markings[sg][1]<requirements[-1]:
                pending=True
                bads.add(markings[i][0])
        if markings[i][0] not in bads:        
            for j in range(len(requirements)):
                if j not in store:
                    if markings[i][1]< requirements[j]:
                        break
                    else:
                        count+=markings[i][1]-requirements[j]
                        store.add(j)
            time+=1
            print(time)
            if time==len(markings)//3:
                countings.append(count)
                time=0
                count=0
                store=set()
    print(countings)
markings=[[0,3],[0,5],[0,7],[1,6],[1,8],[1,9],[2,3],[2,5],[2,6]]
requirements=[4,6,6,7]
chooseFlask(requirements,markings)

