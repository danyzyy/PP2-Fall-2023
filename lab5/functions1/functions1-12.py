def histogram(number):
    for i in number:
        for j in range(i):
             print("*", end="")
        print()
    
    
number=list(map(int, input().split()))
histogram(number)