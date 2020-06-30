num =list(input())
length = len(num)
numnum = [0]*10
set = 0
biggest = 0
answer = 0
sixnine = 0
for i in range(length):
    numnum[int(num[i])] += 1

for i in range(len(numnum)):
    if((biggest<numnum[i])and(i!=6)and(i!=9)):
        biggest = numnum[i]
if((numnum[6]+numnum[9])%2!=0):
    sixnine = (numnum[6]+numnum[9])/2 + 1
else:
    sixnine = (numnum[6]+numnum[9])/2

if(sixnine<biggest):
    answer = biggest
else:
    answer = sixnine

print(int(answer))



    
