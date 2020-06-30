a=[]
answer = 0
for i in range(10):
    num = input()
    num = int(num)
    nameo = num % 42
    if(nameo not in a):
        a.append(nameo)
        answer = answer + 1
print(answer)
