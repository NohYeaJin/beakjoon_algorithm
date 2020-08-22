b=[]
for j in range(5):
    total = 0
    a=input().split(' ')
    for i in range(4):
        total = total + int(a[i])
    b.append(total)
max = b[0]
for i in range(5):
    if(b[i]>max):
        max = b[i]
        max_index = i+1

print(max_index,max)
