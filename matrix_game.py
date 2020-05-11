ssmatr=[[3,7,5,3,4,5],[4,5,2,6,5,4],[7,4,9,7,8,3]]
def matrix(mat):
    tom=0
    jerry=0
    stage_1=[]
    for j in range(len(mat[0])):
        temp=[]
        for i in range(len(mat)):
           temp.append(mat[i][j])
        stage_1.append(sorted(temp, reverse=True))
    stage_2=sorted(stage_1, key=lambda x: x[0], reverse=True)
    print(stage_2)
    for i in range(len(stage_2)):
        if i%2==0:
            tom+=stage_2[i][0]
        else:
            jerry+=stage_2[i][0]
    return tom-jerry
      
print(matrix(matr))





