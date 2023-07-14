n=input()
dem=0
t=True
for i in range (len(n)):
    if n[i]=='4'or n[i]=='7':
        dem+=1
dem=str(dem)
for i in range(len(dem)):
    if dem[i]!='4' and dem[i]!='7':
        t=False
        print('NO')
        break
if t==True:
    print('YES')

