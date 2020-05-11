def doesWordExist(board, word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==word[0]:
                hasSeen = {}
                result = exists(board, i j, word, 0 ,hasSeen)
                if result:
                    return True
    return False

def exists(board, i ,j, word, n , hasSeen):
    if board[i][j] != word[n]:
        hasSeen[(i,j)]=False
        return False
    if n==len(word)-1:
        return True

    hasSeen[(i,j)]= True

    if i+1<len(board) and not hasSeen.get((i+1, j), False):
        down = exists(board, i+1, j, word, n+1, hasSeen)
        if down:
        return True
    if j + 1 < len(board[0]) and not hasSeen.get((i, j+1), False):
        right = exists(board, i, j+1, word, n+1, hasSeen)
        if right:
        return True
    if i -1 >= 0 and not hasSeen.get((i-1, j), False):
        top = exists(board, i-1, j, word, n+1, hasSeen)
        if top:
        return True
    if j-1 >= 0 and not hasSeen.get((i, j-1), False):
        left = exists(board, i, j-1, word, n+1, hasSeen)
        if left:
        return True
    hasSeen[(i,j)] = False
    return False