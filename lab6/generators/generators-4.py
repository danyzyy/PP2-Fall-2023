def squares(A, B):
    for i in range(A, B+1):
        yield i**2

A=int(input())
B=int(input())
d=squares(A, B)


for square in range(B):
    print(next(d))