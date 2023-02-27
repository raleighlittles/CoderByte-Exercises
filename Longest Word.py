import string

def LongestWord(sen):

  longest_word = ""

  for word in sen.split(" "):
    # Problem description says to remove punctuation
    for ch in string.punctuation:
      word = word.replace(ch, "")
      
    if (len(word) > len(longest_word)):
      # New longest word found
      longest_word = word

  return longest_word

# keep this function call here 
print(LongestWord(input()))
