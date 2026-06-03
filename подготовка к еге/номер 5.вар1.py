for n in range(1, 1000):
    a = bin(n)[2:]
    if n % 2 == 0:
        a = a + '10'
    else:
        a = '1' + a + '01'
    r = int(a, 2)
    if n <= 8:
        print(r)