import sys
num,problem = sys.stdin.readline().split(' ')
num , problem = int(num),int(problem)
poketmon_list=[]
poketmon_dic = {}
poketmon_list.append("null")
for i in range(num):
    poketmon = sys.stdin.readline().rstrip()
    poketmon_dic[poketmon] = i
    poketmon_list.append(poketmon)
answer = []
for i in range(problem):
    problems = sys.stdin.readline().rstrip()
    if(ord(problems[0])>=65):
        answer.append(poketmon_dic[problems]+1)
    else:
        answer.append(poketmon_list[int(problems)])
for i in answer:
    print(i)
