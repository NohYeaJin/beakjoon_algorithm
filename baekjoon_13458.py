import sys
num = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
a,b = map(int,sys.stdin.readline().split())
total = 0
for i in num_list:
    if i>a:
        if ((i-a)/b)- ((i-a)//b) > 0:
            total += ((i-a)//b + 1)
        else:
            total += (i-a)//b
print(total+len(num_list))