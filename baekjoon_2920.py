def scale(a):    
    for i in range(len(a)):
        a[i] = int(a[i])
    if(a[0]==1):
        for i in range(len(a)-1):
            if((a[i]+1)!=(a[i+1])):
                return "mixed"
        return "ascending"
    else:
        for i in range(len(a)-1):
            if((a[i]-1)!=(a[i+1])):
                return "mixed"
        return "descending"
a=input().split(' ')
print(scale(a))


