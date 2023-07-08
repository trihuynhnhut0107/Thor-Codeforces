n,k = input().split()
n = int(n)
k = int(k)

a = input()
a_list = a.split()

dem = int(0)
for i in range(n):
    a_list[i] = int(a_list[i])
    if(a_list[i] == 0):
        break
    if (a_list[i]>=int(a_list[k-1])):
        dem+=1
    else:
        break
print(dem)