import sys
def fibo(n):
    if(n==0):
        return 1
    if(n==1 or n==2):
        return n
    else:
        return fibo(n-1)+fibo(n-2)+fibo(n-3)

num = int(sys.stdin.readline())
for i in range(num):
    n = int(sys.stdin.readline())
    print(fibo(n))