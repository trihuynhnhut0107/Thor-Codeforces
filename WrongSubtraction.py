n,k=[int(x) for x in input().split()]
n=str(n)
for i in range (k):
    a=int(n[len(n)-1])
    n=n[:-1]
    if a!=0:
        a-=1
        n+=str(a)
print(n)
