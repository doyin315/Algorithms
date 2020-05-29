def spiral(matrix):
    res=[]
    rowbegin=0
    colbegin=0
    rowend=len(matrix)-1
    colend=len(matrix[0])-1

    while rowbegin<=rowend and colbegin<=colend:
        for i in range(colbegin, colend+1):
            res.append(matrix[rowbegin][i])
        
        rowbegin+=1

        for i in range(rowbegin,rowend+1):
            res.append(matrix[i][colend])

        colend-=1

        if colbegin<=colend:
            for i in reversed(range(colbegin,colend+1)):
                res.append(matrix[rowend][i])

            rowend-=1
        if rowbegin<=rowend:
            for i in reversed(range(rowbegin,rowend+1)):
                res.append(matrix[i][colbegin])
            
            colbegin+=1

    print(res)
    # for k in reversed(range(len(matrix[col])-right)):
    #     res.append(matrix[rowbottom][k])
    # bottom
    # for l in reversed(range())
    

    

l=[[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]

spiral(l)