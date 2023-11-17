import time

n = int(input("Sample Input:\n"))
milsec = int(input())
r = pow(n, 0.5) 
print("Sample Output:")
time.sleep(milsec / 1000)
print("Square root of", n, "after", milsec, "is", r)