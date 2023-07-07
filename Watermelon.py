w = int(input())
flag = True
 
if w<=2:
    flag = False
 
for i in range(w//2):
    if i%2 == 0:
        if(w-i)%2 !=0:
            flag = False
 
if flag:
    print("YES")
else:
    print("NO")
