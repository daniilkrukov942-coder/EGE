for n in range(1, 1000):
    a = bin(n)[2:]  
    if n % 3 == 0:
        if len(a) >= 3:
            a = a + a[-1] + a[-2] + a[-3]
        else:
            a = a + a
    else:
        c = n % 3
        x = bin(c)[2:]
        a = a + x
    b = int(a, 2)
    if b < 76:
        print(n)