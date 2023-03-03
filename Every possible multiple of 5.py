range = 1000
x = 3
while x < range:
    z = 2 ** x
    b = z - 3
    if b % 5 == 0:
        print(x)
    x += 1
