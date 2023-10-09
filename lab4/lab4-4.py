A=input().split()
N=set()
for i in range(len(A)): 
    if A[i] in A[:i]:
        print("YES")
    else:
        print("NO")
        N.add(i)
