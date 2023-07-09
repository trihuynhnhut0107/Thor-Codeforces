a=input()
b=input()
c=""
d=""
for i in a:
    if ord(i)<97:
        c=c+chr(ord(i)+32)
    else:
        c=c+i
for i in b:
    if ord(i)<97:
        d=d+chr(ord(i)+32)
    else:
        d=d+i
if c==d:
    print('0')
elif c>d:
    print('1')
else:
    print('-1')

