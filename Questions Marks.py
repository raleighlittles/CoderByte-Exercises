def QuestionsMarks(strParam):

  # Iterate through the characters.
  # If a digit is found, store it as the first digit
  # Then keep track of the number of '?'s seen 
  # If another digit is then seen, check that its sum with the first digit is 10
  
  first_digit, second_digit = -1, -1
  num_question_marks_seen = 0
  target_sum = 10
  good_pair_found = False

  for ch in strParam:
    if ch.isnumeric():
      if (first_digit == -1):
        first_digit = ch

      elif (second_digit == -1):
        # Second digit is found
        second_digit = ch

    else: # String isn't a number.
      if ((ch == "?") and (first_digit != -1)):
        # Remember we only care about question marks found BETWEEN numbers.
        # if a question mark occurs in the search string before any number, disregard it
        num_question_marks_seen += 1

    # Both numbers are already set, so check their sums.
    # By now you should've already seen 3 question marks
    if (first_digit != -1) and (second_digit != -1):
      if (int(first_digit) + int(second_digit) == target_sum):
        # Must be exactly 3 question marks by this point
        if (num_question_marks_seen == 3):
          good_pair_found = True

        else:
          return "false"


      # Move forward the values -- the second digit becomes the first
      first_digit = second_digit
      second_digit = -1
      num_question_marks_seen = 0

  # Reached the end of the string. Check if you're in the 'middle' of finding a pair
  # in which case, the answer would be false
  return "true" if good_pair_found else "false"
      

# keep this function call here 
print(QuestionsMarks(input()))
