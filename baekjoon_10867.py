import sys
num = {}
n = int(sys.stdin.readline())
numnum = sys.stdin.readline().split(' ')
for i in numnum:
    i = int(i.strip())
    num[i] = 0
for key in sorted(num.keys()):
    print(key,end=" ")

