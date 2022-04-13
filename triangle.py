stars = 5
row = 0

while stars > 0:
    print (' ' * row, end="")
    print('* ' * stars)
    stars -= 1
    row   +=2