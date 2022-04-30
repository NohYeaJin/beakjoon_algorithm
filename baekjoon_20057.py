
n = int(input())
sand = list([list(map(int,input().split())) for _ in range(n)])
middle = n // 2
fly_sand_percent = []
fly_sand_direction = []

s_x = middle
s_y = middle
#왼 아 오 위 순서대로 모래에 일어나는일
directions = [(0,-1) ,(1,0), (0,1) ,(-1,0)]
answer = 0
num = 1

go_left = [(-2,0,0.02),(2,0,0.02),(-1,0,0.07),(1,0,0.07),(1,1,0.01),(-1,1,0.01),(-1,-1,0.1),(1,-1,0.1),(0,-2,0.05),(0,-1,0)]
go_right = [(x, -y, z) for x, y, z in go_left]
go_down = [(-y, x, z) for x, y, z in go_left]
go_up = [(y, x, z) for x, y, z in go_left]

def fly_sand(a, b, x, y):
    global fly_away_sand
    sand_amount = sand[x][y]
    total = 0

    if a == 0 and b == -1:
        for i in range(10):
            p, j, z = go_left[i]
            if 0 <= (x + p) < n and 0 <= (y + j) < n:
                if z == 0:
                    sand[x + p][y + j] += sand_amount - total
                else:
                    sand[x + p][y + j] += int(sand_amount * z)
                    total += int(sand_amount * z)
            else:
                if z == 0:
                    fly_away_sand += sand_amount - total
                else:
                    fly_away_sand += int(sand_amount * z)
                    total += int(sand_amount * z)
    if a == 1 and b == 0:

        for i in range(10):
            p, j, z = go_down[i]
            if 0 <= (x + p) < n and 0 <= (y + j) < n:
                if z == 0:
                    sand[x + p][y + j] += sand_amount - total
                else:
                    sand[x + p][y + j] += int(sand_amount * z)
                    total += int(sand_amount * z)
            else:
                if z == 0:
                    fly_away_sand += sand_amount - total
                else:
                    fly_away_sand += int(sand_amount * z)
                    total += int(sand_amount * z)
    if a == 0 and b == 1:
        for i in range(10):
            p, j, z = go_right[i]
            if 0 <= (x + p) < n and 0 <= (y + j) < n:
                if z == 0:
                    sand[x + p][y + j] += sand_amount - total
                else:
                    sand[x + p][y + j] += int(sand_amount * z)
                    total += int(sand_amount * z)
            else:
                if z == 0:
                    fly_away_sand += sand_amount - total
                else:
                    fly_away_sand += int(sand_amount * z)
                    total += int(sand_amount * z)
    if a == -1 and b == 0:
        for i in range(10):
            p, j, z = go_up[i]
            if 0 <= (x + p) < n and 0 <= (y + j) < n:
                if z == 0:
                    sand[x + p][y + j] += sand_amount - total
                else:
                    sand[x + p][y + j] += int(sand_amount * z)
                    total += int(sand_amount * z)
            else:
                if z == 0:
                    fly_away_sand += sand_amount - total
                else:
                    fly_away_sand += int(sand_amount * z)
                    total += int(sand_amount * z)

    return fly_away_sand

fly_away_sand = 0
while s_x!=0 or s_y!=0:
    for i in range(num):
        a,b = directions[0]

        s_x, s_y = s_x + a, s_y + b
        answer += fly_sand(a, b, s_x, s_y)
        #print(s_x, s_y)
    for i in range(num):
        c,d = directions[1]

        s_x, s_y = s_x + c, s_y + d
        answer += fly_sand(c, d, s_x, s_y)
        #print(s_x, s_y)
    for i in range(num+1):
        a, b = directions[2]

        s_x, s_y = s_x + a, s_y + b
        answer += fly_sand(a, b, s_x, s_y)
        #print(s_x, s_y)

    for i in range(num+1):
        c, d = directions[3]

        s_x, s_y = s_x + c, s_y + d
        answer += fly_sand(c, d, s_x, s_y)
        #print(s_x, s_y)

    num += 2
    if s_x == 0:
        a, b = directions[0]
        for k in range(n-1):

            s_x,s_y = s_x + a, s_y + b
            fly_sand(a,b,s_x,s_y)




            # 모래 비율대로 날리기

print(fly_away_sand)










