def dfs(graph):
      visit = list()
      stack = list()
      stack.append(1)
      num = 0
      #print(stack,"eee")
      while stack:
          node = stack.pop()
          if node not in visit:
              visit.append(node)
              num += 1
              stack= stack + (graph[node])
      return num-1

num = int(input())
vertex = int(input())
graph = [[] for i in range(num+1)]
for i in range(vertex):
    #print(graph)
    a,b = input().split()
    a ,b= int(a),int(b)
    graph[a].append(b)
    graph[b].append(a)
print(dfs(graph))

