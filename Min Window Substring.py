def MinWindowSubstring(strArr):

  main_str, search_str = strArr[0], strArr[1]

  # build up search string letter frequency dictionary
  search_str_letter_freq = dict()

  for char in search_str:
    search_str_letter_freq[char] = 1 + search_str_letter_freq.get(char, 0)

  window_str_letter_freq = dict()
  
  num_letters_found, num_letters_needed = 0, len(search_str_letter_freq)
  
  # Initial values
  result_idx = [0, len(main_str)]
  result_len = len(main_str)

  i = 0
  for j, char in enumerate(main_str):
    # Add the current letter to the dict
    window_str_letter_freq[char] = 1 + window_str_letter_freq.get(char, 0)

    if (char in search_str_letter_freq) and (search_str_letter_freq[char] == window_str_letter_freq[char]):
      # We have exactly enough copies of this letter that we need
      num_letters_found += 1

    while (num_letters_found == num_letters_needed):

      # A new shortest result has been found, so store it
      if ((j - i + 1) < result_len):
        result_len = j - i + 1
        result_idx = [i, j]

      # Start "trimming" the window string (from the left)
      leftmost_letter = main_str[i]
      window_str_letter_freq[leftmost_letter] -= 1

      # Make sure you can still remove a letter
      if (leftmost_letter in search_str_letter_freq) and (window_str_letter_freq[leftmost_letter] < search_str_letter_freq[leftmost_letter]):
        num_letters_found -= 1

      i += 1

  return main_str[result_idx[0] : result_idx[1] + 1]



# keep this function call here 
print(MinWindowSubstring(input()))
