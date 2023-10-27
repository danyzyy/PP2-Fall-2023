def evengen(b):
    for a in range(0, b + 1, 2):
        yield a

b = int(input("number: "))

even_num = evengen(b)
r = ", ".join(map(str, even_num))

print("even numbers between 0 and", b, "in comma form:")
print(r)
