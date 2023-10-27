def returner(n):
    for i in range(n,-1,-1):
        yield i

n=int(input())

d=returner(n)


for num in d:
    print(num)