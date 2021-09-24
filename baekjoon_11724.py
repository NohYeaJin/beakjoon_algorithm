import sys
sys.setrecursionlimit(10000)
#연결 요소를 묻는 문제인데 점 하나로 있는 것들도
# 넣어줘야 하는 것이 애매
#문제에도 connected component라고 쓰여 있음
def dfs(graph,start_node):
      visit = list()
      stack = list()
      stack.append(start_node)
      while stack:
          node = stack.pop()
          if node not in visit:
              visit.append(node)
              stack = stack + (graph[node])
      return visit
num,vertex = sys.stdin.readline().split(' ')
num,vertex = int(num),int(vertex)
graph = [[] for i in range(num+1)]
s1 = set([])
node_list = {}
visit_list = []
answer = 0
for i in range(vertex):
    a,b = sys.stdin.readline().split()
    a ,b= int(a),int(b)
    graph[a].append(b)
    graph[b].append(a)
    s1.add(a)
    s1.add(b)
#visit_list = set(visit_list)
if(num>len(s1)):
    answer += (num-len(s1))
til = True
while(til):
    a_list = s1 - set(visit_list)
    if(len(a_list)>0):
        b_list = list(a_list)
        visit_list += dfs(graph,b_list[0])
        answer += 1
    else:
        til = False

print(answer)