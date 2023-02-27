def BracketMatcher(strParam):

  # No brackets found
  if not any([((x == "(") or (x == ")")) for x in strParam]):
    return 1

  active_bracket_cnt = 0

  for char in strParam:
    if (char == "("):
      active_bracket_cnt += 1

    elif (char == ")"):
      active_bracket_cnt -= 1

    # Bracket count should never go negative -- means an extra right bracket was found
    if (active_bracket_cnt < 0):
      return 0

  return 1 if (active_bracket_cnt == 0) else 0

# keep this function call here 
print(BracketMatcher(input()))
