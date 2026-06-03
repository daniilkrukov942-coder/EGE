from itertools import*
k=0
for x in product('СОЙКА',repeat=5):
    s=''.join(x)
    k+=1
    if s.count('О')==1:
        print(k,s)
