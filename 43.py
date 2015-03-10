from fractions import Fraction
k, n, m, d = map(int, input().split(' '))

s = Fraction(d, (Fraction(1, 1) - Fraction(1, k) - Fraction(1, m) - Fraction(1, n)))

if s % k or s % m or s % n:
    print(-1)
else:
    print(s)
