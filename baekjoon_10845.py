import sys
class Queue:
    def __init__(self):
        self.items = []
        self.front_index = 0
        self.back_index = -1

    def enqueue(self,val):
        self.items.append(val)
        self.back_index += 1

    def dequeue(self):
        if len(self.items) == 0 or self.front_index == len(self.items):
            print("-1")
        else:
            x = self.items[self.front_index]
            self.front_index += 1
            print(x)

    def back(self):
        if len(self.items) == 0 or self.front_index == len(self.items):
            print("-1")
        else:
            print(self.items[self.back_index])


    def front(self):
        if len(self.items) == 0 or self.front_index == len(self.items):
            print("-1")
        else:
            print(self.items[self.front_index])

    def __len__(self):
        return len(self.items)-self.front_index

    def isEmpty(self):
        if len(self.items) == 0 or self.front_index == len(self.items):
            print("1")
        else:
            print("0")

def directions(result,input,val=None):
    result = Queue()
    if input == 'push':
        Q.enqueue(val)

    if input == 'front':
        Q.front()

    if input == 'pop':
        Q.dequeue()

    if input == 'empty':
        Q.isEmpty()

    if input == 'size':
        print(len(Q))

    if input == 'back':
        Q.back()


Q = Queue()
num = input()
num = int(num)
for i in range(num):
    a = sys.stdin.readline().split()

    if a[0] == 'push':
        directions(Q,a[0],a[1])
    else:
        directions(Q,a[0])

