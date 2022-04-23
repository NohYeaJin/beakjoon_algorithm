N,K = map(int,input().split())
can_list = list(map(int,input().split()))

#찾았다
find_dangye = False
dangye = 1

#첫번째 로봇 올리기
robot_pos = []
num2 = 0
while find_dangye==False:
    
    #1단계
    can_list = [can_list.pop()] + can_list

    if len(robot_pos)>=1:
        
        for j in range(len(robot_pos)):
            robot_pos[j] += 1
        if robot_pos[0] >= (N-1):
            robot_pos = robot_pos[1:]


    #2단계
    for j in range(len(robot_pos)):
        if can_list[robot_pos[j]+1] != 0 and robot_pos[j]+1 not in robot_pos:
            can_list[robot_pos[j]+1]-= 1
            if can_list[robot_pos[j]+1] == 0:
                num2 += 1
            robot_pos[j] += 1

    if len(robot_pos)>=1:
        if robot_pos[0] >= (N-1):
            robot_pos = robot_pos[1:]

    #3단계
    if can_list[0]>=1:
        robot_pos.append(0)
        can_list[0] -= 1
        if can_list[0] == 0:
            num2 += 1

    if num2 >= K:
        print(dangye)
        find_dangye = True

    dangye += 1
    



