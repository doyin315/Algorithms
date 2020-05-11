def doesWordExits(board, word):
    d=dict()
    result=[]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==word[0]:
                result.append(validate(board,i,j,word,1,d))
    return any(result)

def validate(grid, x,y,word,Curindex,store):
    if Curindex==len(word):
        return True

    for x1,y1 in [(x+1,y),(x-1,y),(x,y+1),(x+1,y-1)]:
        if 0<=x1<len(grid) and 0<=y1<len(grid[0]) and grid[x1][y1]==word[Curindex] and not store.get((x1,y1), False):
            store[(x1,y1)]=True
            if validate(grid, x1,y1, word,Curindex+1, store):
                return True
                
    store[(x,y)]=False
    return False


board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = 'AB'

print(doesWordExits(board,word))