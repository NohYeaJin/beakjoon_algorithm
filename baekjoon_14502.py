N,M = map(int,input().split())
num_list = [list(map(int,input().split())) for _ in range(N)]
temp_list = [[0] * M for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]

answer = 0
count = 0
def bfs_and_cal_secure(graph):

    virus_list = []

    visited_list =  [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                virus_list.append((i,j))
              
    temp = graph
    #print(virus_list)
    while len(virus_list)>0:
        x,y = virus_list.pop(0)
        #print(virus_list)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < N and 0 <= ny < M:
                if visited_list[nx][ny]==0 and temp[nx][ny]== 0:
                    temp[nx][ny] = 2
                    visited_list[nx][ny] = 1
                    virus_list.append((nx,ny))
    result = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                result += 1

    return result


            
        
def dfs(cnt):

    global answer

    if cnt == 3:
        for i in range(len(num_list)):
            for j in range(len(num_list[i])):
                temp_list[i][j] = num_list[i][j]

        #print(bfs_and_cal_secure(temp_list))
        answer = max(answer,bfs_and_cal_secure(temp_list))
        return

    for i in range(N):
        for j in range(M):
            if num_list[i][j]==0:
                num_list[i][j] = 1
                cnt += 1
                dfs(cnt)
                num_list[i][j] = 0
                cnt -= 1

dfs(0)
print(answer)
