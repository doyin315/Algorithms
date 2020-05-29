def palindromeSearch(word,k):
  def helper(word, start, end, delete):
    while start < end:
      if word[start] == word[end]:
        start += 1
        end -= 1
      elif delete == k:
        return False
      else:
        return helper(word, start+1, end, delete+1) or helper(word, start, end-1, delete+1)
    return True
  return helper(word, 0, len(word)-1, 0)
  

  
word = ''
print(palindromeSearch(word, 2))
