A=set(input().split())
B=set(input().split())

print(*sorted(A.intersection(B), key=int))