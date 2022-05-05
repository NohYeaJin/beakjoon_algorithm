import sys
import collections
T = int(sys.stdin.readline())

def reverse(num_list):
    num = len(num_list)-1
    middle = num // 2
    for i in range(middle):
        num_list[i],num_list[num-i] = num_list[num-i],num_list[i]
    return num_list

def docmd(num_list,cmd):
    rev = 0
    for i in cmd:
        if i == "R":
            rev += 1
        else:
            if len(num_list) == 0:
                return "error"
            else:
                if rev % 2 == 0:
                    num_list.popleft()
                else:
                    num_list.pop()

    if rev % 2 != 0:
        num_list.reverse()
    return num_list

for i in range(T):
    cmd = sys.stdin.readline()
    cmd = cmd.strip()
    num = int(sys.stdin.readline())
    arr = collections.deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    if arr[0] == '':
        arr.pop()
    answer = docmd(arr, cmd)

    if answer == "error":
        print(answer)
    else:
        print("[" + ",".join(answer) + "]")




