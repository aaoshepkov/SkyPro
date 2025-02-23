def bank(x, y):
    percent = 10.0
    for _ in range(y):
        x *= 1 + percent/100
    print(x)

bank(100, 5)


