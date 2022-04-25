N,M = map(int,input().split())


sky = list(list(map(int,input().split())) for _ in range(N))

dx = [-100,0,-1,-1,-1,0,1,1,1]
dy = [-100,-1,-1,0,1,1,1,0,-1]

check_x = [-1,-1,1,1]
check_y = [-1,1,-1,1]

clouds = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]
cloud_check = list([0]*N for _ in range(N))

for i in range(M):

    direc, amount = map(int,input().split())
    cloud_check = list([0]*N for _ in range(N))


    if amount > N:
        amount = amount % N

    #print(sky)

    # 1단계

    for i in range(len(clouds)):

        x,y = clouds[i]
        nx = x + (dx[direc] * amount)
        ny = y + (dy[direc] * amount)

        if nx < 0:
            nx = N + nx
        if nx >= N:
            nx = nx - N
        if ny < 0:
            ny = N + ny
        if ny >= N:
            ny = ny - N

        #print(sky)

        # 2단계
        clouds[i] = (nx,ny)
        sky[nx][ny] += 1

        cloud_check[nx][ny] = -1
    for i in range(len(clouds)):
        for j in range(4):
            nx,ny = clouds[i]
            nx2 = nx + check_x[j]
            ny2 = ny + check_y[j]

            if nx2>=0 and nx2<N and ny2>=0 and ny2<N:
                if sky[nx2][ny2] > 0:
                    sky[nx][ny] += 1
    #print(sky)
    clouds = []
    for k in range(N):
        for m in range(len(sky[k])):
            if cloud_check[k][m] != -1 and sky[k][m] >= 2:
                sky[k][m] -= 2
                clouds.append((k,m))
    #print(sky)
total = 0
for k in range(N):
    for m in range(len(sky[k])):
        total += sky[k][m]
print(total)





            






