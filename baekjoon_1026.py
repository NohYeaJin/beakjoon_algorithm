num = input()
num = int(num)
A=input().split(' ')
B = input().split(' ')
for i in range(num):
    A[i] = int(A[i])
    B[i] = int(B[i])
A.sort()
B.sort(reverse=True)
total = 0
for i in range(num):
    total +=A[i]*B[i]
print(total)