import random

a=random.randint(0, 10)
b=random.randint(0, 10)
c=a+b
print(a,'+',b,'=?')
d=int(input("輸入:"))
if c==d:
    print('YES')
else:
    print('NO')
    