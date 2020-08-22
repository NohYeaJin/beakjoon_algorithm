import sys
num = int(sys.stdin.readline())
stack = []
for i in range(num):
    num2 = int(sys.stdin.readline())
    if(num2==0):
        stack.pop()
    else:
        stack.append(num2)
total = 0
for i in stack:
    total += i
print(total)