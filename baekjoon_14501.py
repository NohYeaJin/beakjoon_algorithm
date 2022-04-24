num = int(input())
T = [0]*(num+1)
P = [0]*(num+1)

max_list = [0]*(num+1)

for i in range(1,num+1):
    t,p = map(int,input().split())
    T[i] = t
    P[i] = p
   
for i in range(1,num+1):
    if max_list[i] <= max_list[i-1]:
        max_list[i] = max_list[i-1] 
    if (i + T[i] - 1) <= num:
        if (max_list[i-1]+P[i]) >= max_list[i+T[i]-1]:
            max_list[i+T[i]-1] = max_list[i-1]+P[i]
    
   
    
print(max(max_list))