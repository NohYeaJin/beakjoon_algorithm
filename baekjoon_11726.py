d=[0]*1001
def tile(n):
    if(n==1):
        return 1
    if(n==2):
        return 2
    if(d[n]!=0):
        return d[n]
    d[n] = tile(n-2)+tile(n-1)
    return d[n]%10007

a=int(input())
print(tile(a))


