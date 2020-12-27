import sys
a,b = map(int, input().split())
a=int(a)
b = int(b)
numnum = [0]
for i in range(1,50):
    for j in range(i):
        numnum.append(i)
total = 0
for i in range(a,b+1):
    total = total + numnum[i]

print(total)