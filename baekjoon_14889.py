import sys
from itertools import combinations as c
M = int(sys.stdin.readline())
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
num_list = [ _ for _ in range(M)]
result = 100000000
for r in c(num_list,M//2):
    start,link = 0,0
    r2 = list(set(num_list) - set(r))
    for r3 in c(r2,2):
        start += stat[r3[0]][r3[1]]
        start += stat[r3[1]][r3[0]]

    for r4 in c(r,2):
        link += stat[r4[0]][r4[1]]
        link += stat[r4[1]][r4[0]]
    result = min(result,abs(start-link))
print(result)
