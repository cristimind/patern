stars = 9
row = 0

while row < 5:
    print ('  ' * row, end="")
    print('* ' * stars)
    stars -= 2
    row   +=1