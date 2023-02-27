def BracketCombinations(num):

  # https://en.wikipedia.org/wiki/Catalan_number#Applications_in_combinatorics
  return catalan_number(num)

# Recursive Catalan number function
def catalan_number(num):
    if num <=1:
         return 1
   
    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num-i-1)
    return res_num

# keep this function call here 
print(BracketCombinations(input()))
