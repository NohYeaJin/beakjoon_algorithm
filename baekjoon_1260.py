vertex,line,start = input().split(' ')
vertex,line,start = int(vertex),int(line),int(start)
graph = dict()

for i in range(line):
    a,b = input().split()
    a,b = int(a),int(b)
    if(a not in graph):
        graph[a] = [b]
    else:
        graph[a] += [b]
    if(b not in graph):
        graph[b] = [a]
    else:
        graph[b] += [a]
#print(graph)
for i in graph:
    lista = graph[i]
    lista.sort()
    graph[i] = lista
#print(graph)
def dfs(graph, start_node):
      visit = list()
      stack = list()
 
      stack.append(start_node)
 
      while stack:
          node = stack.pop(0)
          if node not in visit:
              visit.append(node)
              print(node,end=' ')
              if(node in graph):
                stack = graph[node]+stack
      return visit

def bfs(graph, start_node):
    visit = list()
    queue = list()
    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            print(node,end=' ')
            if(node in graph):
                queue = queue+graph[node]
    return visit
#print(graph)
dfs(graph,start)
print()

bfs(graph,start)
