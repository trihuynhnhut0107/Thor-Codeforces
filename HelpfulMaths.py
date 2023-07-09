s=input()
s1=""
for i in range(len(s)):
    if i==0:
        s1=s1+s[i]
        l=r=int(s[i])
    else:
        if i%2==0:
            if int(s[i])>=r:
                s1=s1+'+'+s[i]
                r=int(s[i])
            elif int(s[i])<=l:
                s1=s[i]+'+'+s1
                l=int(s[i])
            else:
                s2=""
                for k in range(len(s1)):
                    if k%2==0 and int(s[i])<int(s1[k]):
                        s2=s2+s[i]+'+'
                        for j in range(k,len(s1)):
                            s2+=s1[j]
                        break
                    s2=s2+s1[k]
                s1=s2
print(s1)
