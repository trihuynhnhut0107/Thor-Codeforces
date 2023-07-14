n=int(input())
s=input()
d=0
for i in range(n-1):
    if s[i]==s[i+1]:
        d=d+1
print(d)
