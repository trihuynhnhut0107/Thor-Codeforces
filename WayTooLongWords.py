a = list()
n = int(input())
for i in range(n):
    a.append(input())
for i in range(n):
    if len(a[i]) > 10:
        print(a[i][0],len(a[i])-2,a[i][len(a[i])-1], sep = '')
    else:
        print(a[i])
