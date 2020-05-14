def spiral(matrix):
    top=0
    right=0
    left=0
    row=0
    bottom=0
    rowbottom=len(matrix)-1
    col=len(matrix[0])-1
    res=[]

    # while row<len(matrix) and col>=0:
    for i in range(len(matrix[col])-right):
        res.append(matrix[row][i])
    
    top+=1
    for j in range(top,len(matrix[row])):
        res.append(matrix[j][col])
    right+=1

    for k in reversed(range(len(matrix[col])-right)):
        res.append(matrix[rowbottom][k])
    bottom
    for l in reversed(range())
    
    print(res)

    

l=[[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]

spiral(l)