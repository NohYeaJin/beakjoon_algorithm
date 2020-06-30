num = input()
num = int(num)
for i in range(num):
    answer = 0
    quiz = input()
    quiz = list(quiz)
    point = 0
    for i in range(len(quiz)):
        if(i==0):
            if(quiz[0]=='O'):
                point = 1
                answer = answer + point
        else:
            if(quiz[i]=='O'):
                if(quiz[i-1]=='O'):
                    point = point + 1
                    answer = answer + point
                else:
                    point = 1
                    answer = answer + point
    print(answer)

        


