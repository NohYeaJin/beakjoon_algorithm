from sys import stdin
num = input()
num = int(num)
Matrix = [[None] for i in range(100)]


for i in range(num):
    j = 0
    word = input()
    if (Matrix[len(word)][0]==None):
        Matrix[len(word)][0]= word
    else:
        if(word not in Matrix[len(word)]):
            Matrix[len(word)].append(word)

for i in range(55):
    if(Matrix[i][0]!=None):
        Matrix[i].sort()


for i in range(55):
    if(Matrix[i][0]!=None):
        for j in Matrix[i]:
            print(j)





