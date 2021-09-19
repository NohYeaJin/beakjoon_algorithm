import sys
def check(line,password):
    Upper = False
    Lower = False
    digit = False
    issymbol = False
    while(True):
        for i in password:
            if((Upper==True)and(Lower==True)):
                if((digit==True)and(issymbol==True)):
                    return "valid"
            if (i in symbol):
                issymbol = True
            elif (ord(i)<=57 and ord(i)>=48):
                digit = True
            elif (ord(i)<=90 and ord(i)>=65):
                Upper = True
            else:
                Lower = True
        return "invalid"

symbol = "+_)(*&^%$#@!./,;{}"
symbol = list(symbol)
num = sys.stdin.readline()
num = int(num)
for i in range(num):
    line = sys.stdin.readline()
    line = int(line)
    password = sys.stdin.readline()
    if(line>=12):
        print(check(line,password))
    else:
        print("invalid")







