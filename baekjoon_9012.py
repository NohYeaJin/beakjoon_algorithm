num = int(input())
for i in range(num):
    parens = input()
    stack = []
    for i in parens:
        if(len(stack)>=1):
            if (i=="("):
                stack.append(i)
            else:
                if(stack[len(stack)-1]=="("):
                    stack.pop()
                else:
                    stack.append(i)
        else:
            stack.append(i)
    if(len(stack)>0):
        print("NO")
    else:
        print("YES")



