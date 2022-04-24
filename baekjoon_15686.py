import itertools 
N,M = map(int,input().split())
num_list = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]
count = []
chicken = 0
chicken_houses = []
chosen_list = []
human_houses = []
for i in range(len(num_list)):
    for j in range(len(num_list[i])):
        if num_list[i][j] == 2:
            chicken_houses.append([i,j])
        elif num_list[i][j] == 1:
            human_houses.append([i,j])

def cal_dis(temp_list):
    answer = 1000000000000
    answer2 = 0
    for i in human_houses:
        answer = 1000000000000
        #print(x1,y1)
        x1, y1 = i[0],i[1]
        #print(x1,y1)
        for j in temp_list:
            #print(j)
            dis = 0
            x2, y2 = j[0],j[1]
            #print(x2,y2)
            if (x1 - x2) < 0:
                dis += (x2 - x1)
            else:
                dis += (x1 - x2)
            if (y1 - y2) < 0:
                dis += (y2 - y1)
            else:
                dis += (y1 - y2)
            answer = min(answer,dis)
            #print(answer)
        answer2 += answer
    return answer2


def chicken_choice():
  
    result = list(itertools.combinations(chicken_houses, M))

    answer = 10000000000000
    #print(result)

    for i in result:
        #print(i)
        answer = min(answer,cal_dis(i)) 
        #print(answer)

    return answer
print(chicken_choice())

       




