def pascalSolution(m, n, k):
    r = ''
    dig = m / n
    r += str(dig)
    for i in range(1, k + 1):
        if i == 1: r += '.'
        m = (m - n * dig) * 10
        dig = m / n
        r += str(dig)
    return r
    
from decimal import *
m, n, k = map(int, input().split())
#m, n, k = map(int, '10 2 2'.split())

def bigAccuracy(m, n, k):
    getcontext().prec = k + 2
    res = str(Decimal(m) / Decimal(n))

    if '.' not in res: res += '.'    
    spl = res.split('.')
    spl[1] = spl[1][:k]
    
    llen, rlen = len(spl[0]), len(spl[1])
    
    if k > 0:
        zAdd = llen + k + 1
        res = spl[0] + '.' + spl[1]
    else:
        zAdd = llen + k
        res = spl[0]
    
    return res.ljust(zAdd, '0')

print(bigAccuracy(m, n, k))

def test():
    t = (
        (1, 2, 3),
        (1, 3, 26),    
        (5, 289, 10),
        (11, 12, 26),
        (50, 4, 3),
        (18, 111, 7),
        (10, 2, 2),        
        (1, 2, 2),        
        (100, 100, 1000),
        (22, 7, 1000),
    )
    #t = ((10,2,2),)
    for i in t:
        print('m=' + str(i[0]) + ' n=' + str(i[1]) + ' k=' + str(i[2]))
        print('our: ' + bigAccuracy(i[0], i[1], i[2]))
        print('pas: ' + pascalSolution(i[0], i[1], i[2]))
        
test()    