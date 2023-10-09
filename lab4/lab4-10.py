N, K = [int(i) for i in input().split()]
X = set()
for i in range(K):
    ai, bi = [int(j) for j in input().split()]
    for j in range(ai, N+1, bi):
        if j%7 == 6 or j%7 == 0:
            continue
        X.add(j)
print(len(X))
