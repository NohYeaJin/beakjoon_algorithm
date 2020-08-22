import sys
def factorial(n):
    if(n==0):
        return 1
    elif(n==1):
        return 1
    return factorial(n-1)*n
num = int(sys.stdin.readline())
print(factorial(num))