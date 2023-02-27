def CodelandUsernameValidation(strParam):

  str_len = len(strParam)
  invalid_str_msg, valid_str_msg = "false", "true"

  # Rule 1
  if not ((str_len >= 4) and (str_len <= 25)):
    return invalid_str_msg

  # Rule 2
  if not strParam[0].isalpha():
    return invalid_str_msg
  
  # Rule 4
  if strParam.endswith("_"):
    return invalid_str_msg

  # Rule 3
  for ch in strParam:
    if ((not ch.isalnum()) and (ch != "_")):
      return invalid_str_msg

  # Made it to the end so string must be valid
  return valid_str_msg

  


# keep this function call here 
print(CodelandUsernameValidation(input()))
