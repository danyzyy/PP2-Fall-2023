def solve(num_heads, num_legs):
    for chickens in range(num_heads + 1):
        rabbits = num_heads - chickens
        if 2 * chickens + 4 * rabbits == num_legs:
            return chickens, rabbits
    return None 


num_heads = 35
num_legs = 94
solution = solve(num_heads, num_legs)

if solution:
    chickens, rabbits = solution
    print(f"Chickens: {chickens}")
    print(f"Rabbits: {rabbits}")
else:
    print("No solution found.")
    