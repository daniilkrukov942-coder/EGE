def perevod(chislo, sys):
    N = chislo
    s = ''
    while N > 0:
        s = str(N % sys) + s
        N = N // sys
    return s
for n in range(1, 1000):
    a = perevod(n, 3)
    if n % 3 == 0:
        b = '1' + a + a[-2:]
    else:
        sum_cifr = sum(int(digit) for digit in a)
        x = sum_cifr * 5
        m = perevod(x, 3)
        b = a + m
    r = int(b, 3)
    print(r)
# ответ:1002



