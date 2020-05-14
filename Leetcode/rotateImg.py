def rotate(board):
    # d={}
    n=len(board)
    for i in range(n):
        for j in range(i,len(board[0])):
            board[i][j],board[j][i]=board[j][i],board[i][j]

    # for i in d:
    #     board[i[0]][i[1]]=d[(i[0],i[1])]

    for i in range(len(board)):
        j,k = 0,n-1
        while j<k:
            board[i][j],board[i][k]=board[i][k],board[i][j]
            j+=1
            k-=1
        # board[i]=list(reversed(board[i]))
    print(board)
        



board = [[1,2,3],
         [4,5,6],
         [7,8,9]]    

rotate(board)