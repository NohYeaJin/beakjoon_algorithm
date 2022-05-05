N,M,K = map(int,input().split())
#M이 가로 N이 세로 k는 이동횟수
#처음에 (1,1) 이동 방향은 동쪽
direction = [(0,1),(1,0),(0,-1),(-1,0)]
#동 남 서 북
dice_map = [list(map(int, input().split())) for _ in range(N)]

origin_dice = [2,4,1,3,5,6]

def dice_change(origin_dice,dice_direction):
    a,b = dice_direction
    #동
    if a == 0 and b == 1:
        return [origin_dice[0],origin_dice[5],origin_dice[1],origin_dice[2],origin_dice[4],origin_dice[3]]
    #남
    if a == 1 and b == 0:
        return [origin_dice[5],origin_dice[1],origin_dice[0],origin_dice[3],origin_dice[2],origin_dice[4]]
    #서
    if a == 0 and b == -1:
        return [origin_dice[0],origin_dice[2],origin_dice[3],origin_dice[5],origin_dice[4],origin_dice[1]]
    #북
    if a == -1 and b == 0:
        return [origin_dice[2],origin_dice[1],origin_dice[4],origin_dice[3],origin_dice[5],origin_dice[0]]

def find_serial_num(x,y):
    #print(x,y,"x")
    num = dice_map[x][y]
    visited = [[0]*M for _ in range(N)]
    visit_list = [(x,y)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited[x][y] = 1
    score = 1
    while visit_list:
        ox,oy = visit_list.pop(0)

        for i in range(4):
            nx = dx[i] + ox
            ny = dy[i] + oy

            if 0<=nx<N and 0<=ny<M:

                if dice_map[nx][ny] == num and visited[nx][ny]==0:

                    score += 1
                    visit_list.append((nx,ny))
                    visited[nx][ny] = 1
    return score * num

#처음 동쪽으로
go = 0
x,y = 0,0
answer = 0
for i in range(K):
    a,b = direction[go]
    n_x, n_y  = x + a, y + b
    #일단 동쪽으로 굴리고, 거리가 없으면 반대로

    if 0 <= n_x < N and 0 <= n_y < M:
        # 굴려서 주사위가 바뀜
        origin_dice = dice_change(origin_dice,(a,b))
    else:
        #방향을 반대로

        go += 2
        if go >= 4:
            go = go - 4
        #굴려서 주사위가 바뀜
        a, b = direction[go]
        n_x,n_y = x + a, y+b
        origin_dice = dice_change(origin_dice,direction[go])

    dice_badak = origin_dice[5]
    score_badak = dice_map[n_x][n_y]
    #점수 계산 부분
    answer += find_serial_num(n_x,n_y)

    if dice_badak > score_badak:
        go += 1
        if go == 4:
            go = 0
    elif dice_badak < score_badak:
        go -= 1
        if go == -1:
            go = 3

    x, y = n_x, n_y

print(answer)










