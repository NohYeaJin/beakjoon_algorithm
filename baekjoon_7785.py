num = int(input())
people = {}
for i in range(num):
    name,el = input().split(' ')
    people[name]=el

for k,v in sorted(people.items(),reverse=True):
    if(v=='enter'):
        print(k)
    
        
