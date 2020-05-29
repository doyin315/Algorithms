def climb(n):
    if n==0 or n==1:
        return 1
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        
        dp[n]=dp[n-1]+dp[n-2]
    
    return dp[n]


print(climb(3))


s="racecar"
def longestPalindrome(word):
  
  def helper(word, start, end):
    palin = ''
    while start >= 0 and end < len(word):
      if word[start] != word[end]:
        break
       palin = word[start:end+1]
      start -= 1
      end += 1
    return palin
  
  maxPalin = ''
  for i in range(len(word)):
    tempPalin  = helper(word, i, i)
    tempPalin2 = helper(word, i, i+1)
    maxPalin = max(maxPalin, tempPalin, tempPalin2)
  return maxPalin