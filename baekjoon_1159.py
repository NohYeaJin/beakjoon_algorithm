num = int(input())
names = [0]*26
answer = ""
for i in range(num):
    name = input()
    names[ord(name[0])-97] += 1
for i in range(len(names)):
    if(names[i]>=5):
        answer = answer + chr(i+97)
if(answer == ""):
    print("PREDAJA")
else:
    print(answer)



