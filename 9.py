from functools import reduce
from itertools import permutations
n = int(input())

def getCountAndSmallest(n):
   if n == 0:
       return (0, 0)
   elif n == 1:
       return (10, 0)
           
   valid, res = (), ()
   if n in (2, 3):
       interval, z, prefix = range(0, 99), 2, (n-2) * '1'
   else:
       interval, z, prefix = range(0, 999), 3, (n-3) * '1'
       
   for i in interval:
       t = tuple(map(int, prefix + str(i).zfill(z)))
       if 0 in t:
           continue
       s = sum(t)
       m = reduce(lambda x, y: x * y, t)
       if s == m:            
           valid += (t,)

   for i in valid:
       if i not in res:
           res += tuple(set(permutations(i)))

   return(len(res), reduce(lambda rst, d: rst * 10 + d, min(res)))    
   
res = getCountAndSmallest(n)
print(res[0], res[1])