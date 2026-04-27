def dfs(graph, start, goal):
  visited = set()
  stack = [start]
  path = ""

  while stack:
    node = stack.pop()

    if node == goal:
      path += goal
      return path
    else: 
      path += node + ' -> '

    if node not in visited:
      visited.add(node)

      for neighbour in reversed(graph[node]):
        if neighbour not in visited:
          stack.append(neighbour)

  return 'No Path Found'
graph = {}
n = int(input("Enter total nodes: "))
for i in range(n):
  node = input("Enter name of node: ")
  neighbours = input(f"Enter neighbours of {node} (comma separated): ").split(',')
  graph[node] = neighbours

start_node = input("Enter Start Node: ")
goal_node = input("Enter Goal Node: ")
path = dfs(graph, start_node, goal_node)
print(f"DFS Traversal Path: {path}")
