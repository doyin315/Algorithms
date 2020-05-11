def sqrt(n,min,max):
    guess=(min+max)//2
    if guess*guess == n:
        return guess
    elif guess*guess<n:
        return sqrt(n,guess+1,max)
    else:
        return sqrt(n,min,guess-1)

print(sqrt(9,1,9))