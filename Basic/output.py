Colors = ["Red", "Orange", "Yellow", "Green", "Blue"]
for Item in Colors:
    print(Item.rjust(8), sep='/n')
print(*Colors, sep='\n')
print('\n'.join(Colors))
print('First: {0}\nSecond: {1}'.format(*Colors))
