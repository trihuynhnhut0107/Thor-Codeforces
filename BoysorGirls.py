s=input()
s1=""
for i in range(len(s)):
    t=False
    for j in range(len(s1)):
        if s1[j]==s[i]:
            t=True
            break
    if t==False:
        s1=s1+s[i]
if len(s1)%2!=0:
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')