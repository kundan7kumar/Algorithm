def abc1():
    x = 1
    for i in range(1, 5):
        if x <= 250:
            x = x + 1
        else:
            x = x - 1
    print(x)
