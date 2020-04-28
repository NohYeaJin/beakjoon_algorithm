a,b= input().split(' ')
a= int(a)
b = int(b)
num = input()
def blackjack(a,b,num):
    numnum = []
    total = 0
    minus = 0
    result = 0
    minus2 = 300000
    numnum = num.split(' ')
    for i in range(a):
        numnum[i] = int(numnum[i])
    numnum.sort()
    for i in range(1,a-1):
        center = numnum[i]
        start = 0
        end = a - 1
        while((i!=end)and(start!=i)):
            total = numnum[start]+numnum[end]+numnum[i]

            if(total==b):
                return total
            elif(total>b):
                end = end - 1
            else:
                minus = b - total
                if (minus2>minus):
                    minus2 = minus
                    result = total
                start = start + 1
    return result
result = blackjack(a,b,num)
print(result)







