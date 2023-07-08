n = int(input())    
dem = int(0)

for i in range(n):
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if (a+b+c)>1:
        dem+=1
print(dem)