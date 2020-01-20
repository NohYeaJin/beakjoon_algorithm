class list:
    def __init__(self):
        self.items = []
        self.size = 0

    def enter(self,val):
        self.items.append(val)
        self.size += 1

    def leave(self,val):
        for i in range(self.size):
                if val == self.items[i]:
                    a = self.items[i]
                    del self.items[i]
                    self.size = self.size - 1
                    return a
                   

a = input()
a = int(a)
if a > 1000000:
    a = 0
chultwae = list()
for i in range(a):
    b,c = input().split()
    if c == 'enter':
        chultwae.enter(b)
    else:
        chultwae.leave(b)

for i in range(chultwae.size):
    print(chultwae.items[i])


        
