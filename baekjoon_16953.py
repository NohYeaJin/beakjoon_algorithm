start,end = map(int,input().split())
def solution(start,end):

    num_list = [start]
    answer = 0
    while num_list:

        answer += 1
        num_list2 = []
        for i in num_list:
            
            if i*2 == end or (i*10+1) == end:
                return answer+1
            else:
                if i < end:
                    num_list2.append(i*10+1)
                    num_list2.append(i*2)
        num_list = num_list2
    return -1
print(solution(start,end))

        

