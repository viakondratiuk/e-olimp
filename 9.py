from functools import reduce
n, count, smallest = int(4), 0, None

if n == 1:
    interval = range(0, 10 ** n)
else:
    interval = range(10 ** (n - 1), 10 ** n)
    
for i in interval:
    l = list(map(int, str(i)))
    if 0 in l:
        continue
    s = sum(l)
    m = reduce(lambda x, y: x * y, l)

    if s == m:
        count += 1
        print i
        if smallest is None:
            smallest = i

print(count, smallest)

'''
10
11
12
13

1 + 2 + 2(5) = 1 * 2 * 2(4)
1 + 2 + 3(6) = 1 * 2 * 3(6)
1 + 2 + 4(7) = 1 * 2 * 4(8)
1 + 2 + 5(8) = 1 * 2 * 5(10)
2 + 5 + 4(11) = 2 * 5 * 4(40)
2 + 5 + 5(12) = 2 * 5 * 5(50)
'''