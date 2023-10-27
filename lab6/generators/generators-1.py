def gen_square(N):
    for i in range(1, N + 1):
        yield i ** 2

N = int(input())
f = gen_square(N)

for square in f:
    print(square)