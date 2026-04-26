import heapq

def gbfs(graph, start, heuristic, goal):
  visited = set()
  queue = [(heuristic[start], start)] # Priority Queue
  i = 0
  path = ""

  while queue:
    h, node = heapq.heappop(queue)
    if node == goal:
      path += node
      return path

    if node not in visited:
      visited.add(node)

      for neighbour in graph[node]:
        if neighbour not in visited:
          heapq.heappush(queue, (heuristic[neighbour], neighbour))
      
      path += node + " -> "

  return "No Path Found"

graph = {}
heuristic = {}

n = int(input("Enter the number of nodes: "))
for i in range(n):
  node = input("Enter node name: ")
  neighbours = input(f"Enter neighbours of {node} (comma seperated): ").split(',')
  h = int(input(f"Enter the heuristic value of {node}: "))

  graph[node] = neighbours
  heuristic[node] = h

start_node = input("Enter start node: ")
goal_node = input ("Enter goal node: ")

traversal_order = gbfs(graph, start_node, heuristic, goal_node)
print(f"\nGreedy BFS Traversal Order: {traversal_order}")
