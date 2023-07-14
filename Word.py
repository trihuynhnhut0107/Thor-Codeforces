s=input()
demthuong=0
demhoa=0
for i in range(len(s)):
    if ord(s[i])<97:
        demhoa+=1
    else:
        demthuong+=1
if demthuong>=demhoa:
    print(s.lower())
else:
    print(s.upper())
