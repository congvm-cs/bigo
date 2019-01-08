n = int(input())
if n == 1:
    print(15000)
elif n >= 2 and n <= 5:
    print(15000 + (n-1)*13500)
else:
    if n < 12:
        print((15000 + 13500*4 + (n-5)*11000))
    else:
        print(int(0.9*(15000 + 13500*4 + (n-5)*11000)))
