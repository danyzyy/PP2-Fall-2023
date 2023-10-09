x,y=[int(i) for i in input().split()]
a=set()
b=set()
for i in range(x):
    a.add(int(input()))
for i in range(y):
    b.add(int(input()))
print(len(a&b))
print(*sorted(a&b))
print(len(a-b))
print(*sorted(a-b))    
print(len(b-a))
print(*sorted(b-a))
