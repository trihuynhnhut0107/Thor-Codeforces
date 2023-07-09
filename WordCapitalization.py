s=input()
s1=""
if ord(s[0])>=97:
    s1=chr(ord(s[0])-32)
else:
    s1=s[0]
for i in range(1, len(s)):
    s1=s1+s[i]
print(s1)
