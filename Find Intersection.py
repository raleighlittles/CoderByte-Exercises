def FindIntersection(strArr):

  list_1 = [int(x.strip()) for x in strArr[0].split(",")]
  list_2 = [int(x.strip()) for x in strArr[1].split(",")]
  
  sorted_intersect = sorted(list(set(list_1) & set(list_2)))

  return ",".join([str(x) for x in sorted_intersect]) if (len(sorted_intersect) > 0) else "false"


# keep this function call here 
print(FindIntersection(input()))
