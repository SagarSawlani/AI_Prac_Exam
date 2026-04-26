from collections import deque

def bfs(graph, start, goal):
  visited = set()
  queue = deque([start])
  path = ""
  i = 0
  print(f"\nIteration {i}: Queue: {list(queue)}")
  
  while queue:
    node = queue.popleft()
    if node == goal:
      path += node 
      return path

    path += node + " -> "

    if node not in visited:
      visited.add(node)
      
      for neighbour in graph[node]:
        if neighbour not in visited:
          queue.append(neighbour)
      
      i += 1
      print(f"\nIteration {i}: Queue: {list(queue)}, Visited: {visited}")
  return "Path Not Found"

graph = {}
n = int(input("Enter the number of nodes: "))
for i in range(n):
  node = input("Enter Node Name: ")
  neighbours = input(f"Enter Neighbours of {node} (comma seperated): ").split(",")
  graph[node] = neighbours

start_node = input("Enter the starting node: ")
goal_node = input("Enter goal node: ")

path = bfs(graph, start_node, goal_node)
print(f"\nBFS Traversal Path: {path}")