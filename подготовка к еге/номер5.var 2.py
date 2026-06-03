for n in range(1,10000):
    a = bin(n)[2:]
    if n % 2 == 0:
        a = a + a[-2]
        r = a
    else:
        a = '1' + a + '0'
        r = a
    x = int(r, 2)
    if x < 100:
        print(x)