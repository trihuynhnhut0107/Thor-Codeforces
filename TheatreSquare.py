n,m,a = [int(x) for x in input().split()]
i=n//a
if i*a!=n:
    i=i+1
j=m//a
if j*a!=m:
    j=j+1
print(i*j)



