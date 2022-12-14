graph = {
  1 : ["2","3"],
  2 : [4, 5],
  3 : [6,7],
  4 : [8],
  5 : [],
  6 : [9,10],
  7 : [],
  8 : [],
  9 : [],
  10 : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, '5')