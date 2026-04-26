import heapq

def a_star(graph, start, heuristic, goal):
  visited = set()
  queue = [(0, start)]
  g_cost = {start: 0}

  path = ""

  while queue:
    h, node = heapq.heappop(queue)
    if node not in visited:
      visited.add(node)

      if node == goal:
        path += goal
        return path

      for neighbour, cost in graph[node]:
        g_new = g_cost[node] + cost

        if neighbour not in visited or g_new < g_cost[neighbour]:
          f = g_new + heuristic[neighbour]
          heapq.heappush(queue, (f, neighbour))
          g_cost[neighbour] = g_new

      path += node + " -> "

  return "No Path Found"

graph = {}
heuristic = {}

n = int(input("Enter the number of nodes: "))
for i in range(n):
  node = input("Enter node name: ")
  neighbours = input(f"Enter neighbours of {node} (Commma Seperated): ").split(',')

  graph[node] = []
  for neighbour in neighbours:
    cost = int(input(f"Enter the cost to reach {neighbour} from {node}: "))
    graph[node].append((neighbour, cost))

  h = int(input(f"Enter the heuristic value of {node}: "))
  heuristic[node] = h

starting_node = input("Enter the starting node: ")
goal_node = input("Enter the goal node: ")

traversal_path = a_star(graph, starting_node, heuristic, goal_node)
print("\nA* Traversal Path: ", traversal_path)
