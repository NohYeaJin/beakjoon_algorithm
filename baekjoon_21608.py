num = int(input())
student_num = num ** 2

total_student_list = [list(map(int,input().split())) for _ in range(student_num)]

seat = [(-1,0),(0,-1),(0,1),(1,0)]
check = list([0]*num for _ in range(num))
seated = list([0]*num for _ in range(num))
#print(seated)

student_list_proxy = total_student_list
like_list = [[0]*4 for _ in range(student_num+1)]

for i in range(student_num):
    #print(seated)
    like_student = student_list_proxy[i]
    student_seat = like_student.pop(0)
    like_list[student_seat][0] = like_student[0]
    like_list[student_seat][1] = like_student[1]
    like_list[student_seat][2] = like_student[2]
    like_list[student_seat][3] = like_student[3]
    index = (-1,-1)
    best_seat_friends = -1
    best_seat_empty = -1
    for i in range(num):
        for j in range(num):
            if seated[i][j] == 0:
                empty_seat = 0
                like_friends = 0
                for k in range(4):
                    a,b = seat[k]
                    if 0 <= a + i < num and 0 <= b + j < num:
                        #print(seated[a+i][b+j])
                        #좋아하는 학생이 옆에 있다면
                        if seated[a+i][b+j] == like_student[0] or seated[a+i][b+j] == like_student[1] or seated[a+i][b+j] == like_student[2] or seated[a+i][b+j] == like_student[3]:
                            like_friends += 1
                        #비어 있는 자리라면
                        else:
                            if seated[a+i][b+j] == 0:
                                empty_seat += 1
                #지금 이자리가 가장 좋은 후보군인지
                #좋아하는 친구 수가 더 많다면
                if best_seat_friends < like_friends:
                    best_seat_friends = like_friends
                    best_seat_empty = empty_seat
                    index = (i,j)
                # 좋아하는 친구수는 같지만 빈자리가 더 많다면
                elif best_seat_friends == like_friends:
                    if best_seat_empty < empty_seat:
                        best_seat_empty = empty_seat
                        index = (i,j)
    x,y = index
    seated[x][y] = student_seat

score = 0
for i in range(num):
    for j in range(num):
        like_friends = 0
        student_num = seated[i][j]
        like_student = like_list[student_num]

        for k in range(4):
            a, b = seat[k]
            if 0 <= a + i < num and 0 <= b + j < num:
                if seated[a + i][b + j] == like_student[0] or seated[a + i][b + j] == like_student[1] or seated[a + i][b + j] == like_student[2] or seated[a + i][b + j] == like_student[3]:
                    like_friends += 1
        if like_friends == 1:
            score += 1
        elif like_friends == 2:
            score += 10
        elif like_friends == 3:
            score += 100
        elif like_friends == 4:
            score += 1000
print(score)




