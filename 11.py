'''
var
n,m,k,i,dig:integer;

begin
  read(n,m,k);
  dig:=n div m;
  write(dig);
  for i:=1 to k do
  begin
      if i=1 then write('.');
      n:=(n-m*dig)*10;
      dig:=n div m;
      write(dig);
  end;
  writeln;
end.
'''


#m, n, k = map(int, input().split())
m, n, k = map(int, '5 289 10'.split())

res = str(m / float(n))
spl = res.split('.')
spl[1] = spl[1][:k]

llen, rlen = len(spl[0]), len(spl[1])

if k > 0:
    add = llen + 1 + k
    res = spl[0] + '.' + spl[1]
else:
    add = llen + k
    res = spl[0]

print(res.ljust(add, '0'))