def TreeConstructor(strArr):

  # Use a dictionary to represent the tree. Key is the parent node,
  # values are child nodes.
  tree = dict()
  # For the convenience of counting root nodes, create a list of child nodes
  child_nodes = []

  for pair in strArr:
    child, parent = [x.strip(",()") for x in pair.split(",")]
    
    if parent in tree:
      if (len(tree[parent]) == 2):
        # If there's already 2 children, you can't add another, as that wouldn't make
        # it a proper binary tree
        return "false"

      tree[parent].append(child)

    else:
      # Key doesn't exist, so add it
      tree[parent] = [child]

    child_nodes.append(child)

  root_count = 0
  # Count the number of root nodes -- the nodes who do not have a parent (and thus don't appear
  # in the list of childs)
  for node in tree:
    if node not in child_nodes:
      root_count += 1
  
  return "true" if (root_count == 1) else "false"

# keep this function call here 
print(TreeConstructor(input()))
