ds=[]
for i in range(0,5):
    a=input()
    a=list(map(int,a.split()))
    ds.append(a)
t=False
for i in range(5):
    for j in range (5):
        if ds[i][j]==1:
            t=True
            break
    if t==True:
        break
print(abs(i-2)+abs(j-2))



