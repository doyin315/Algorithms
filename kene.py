sub='ABBCZBAC'
for i in range(len(sub)):
    for j in range(len(sub)+1):
        if sub[i:j]!="":
            print(sub[i:j])