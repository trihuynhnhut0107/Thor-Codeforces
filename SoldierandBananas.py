k,n,w=[int(x) for x in input().split()]
s=0
for i in range(1,w+1):
    s=s+i
s=s*k
a=s-n
if (a<0):
    print(0)
else:
    print(a)

