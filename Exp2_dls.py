def dls(start, graph, limit, goal):
  visited = set()
  stack = [(start, 0)]
  path = ""
  i = 0

  while stack:
    node, depth = stack.pop()
    if node == goal:
      path += node
      return path

    if node not in visited:
      visited.add(node)
      path += node + " -> "

      if depth < limit:
        for neighbour in reversed(graph[node]):
          if neighbour not in visited:
            stack.append((neighbour, depth + 1))
        i += 1
  return "Path Not Found"

graph = {}
n = int(input("Enter the number of nodes: "))
for i in range(n):
  node = input("Enter Node Name: ")
  neighbours = input(f"Enter Neighbours of {node} (comma seperated): ").split(",")
  graph[node] = neighbours

start_node = input("Enter the Starting Node for DLS: ")
limit = int(input("Enter the Depth Limit: "))
goal_node = input("Enter the Goal Node: ")

traversal_order = dls(start_node, graph, limit, goal_node)
print(f"\nDLS Traversal Order: {traversal_order}")
