import sys
num = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
op = list(map(int,sys.stdin.readline().split()))
max_num, min_num = -1e9, 1e9
def dfs(depth,total,plus,minus,multi,divide):
    global min_num, max_num
    if depth == num:
        min_num = min(min_num,total)
        max_num = max(max_num,total)
        return
    if plus:
        dfs(depth+1,total+num_list[depth],plus-1,minus,multi,divide)
    if minus:
        dfs(depth+1,total-num_list[depth],plus,minus-1,multi,divide)
    if multi:
        dfs(depth+1,total*num_list[depth],plus,minus,multi-1,divide)
    if divide:
        dfs(depth+1,int(total/num_list[depth]),plus,minus,multi,divide-1)

dfs(1,num_list[0],op[0],op[1],op[2],op[3])
print(max_num)
print(min_num)



