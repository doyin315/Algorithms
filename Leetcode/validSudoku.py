def valid(board):
    seen= dict()
    for i in range(len(board)):
        for j in range(len(board[0])):
            current = board[i][j]
            if current!=".":
                if not seen.get(str(current) +' found in row '+ str(i),False) and not seen.get(str(current) +' found in column '+ str(j),False) and not seen.get(str(current) +' found in sub box '+ str(i//3)+ "-"+str(j//3), False):
                    seen[current +' found in row '+ str(i)]=True
                    seen[current +' found in column '+ str(j)]=True
                    seen[str(current) +' found in sub box '+ str(i//3)+ "-"+str(j//3)]=True
                else:
                    return False

    return True



board=[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

board1= [["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]

print(valid(board1))