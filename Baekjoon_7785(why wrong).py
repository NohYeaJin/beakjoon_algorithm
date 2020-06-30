import sys
num = int(input())
person={}
for i in range(num):
    find,cond = sys.stdin.readline().split()
    if(cond=='enter'):
        person.update({find:True})
    else:
        person[find]=False
res = sorted(person.items(),reverse=True)
for i in person:
    if(person[i]==True):
        print(i)