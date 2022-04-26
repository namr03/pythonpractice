from random import randint
a = []
b = []
c = []

for i in range(14):
    a.append(randint(0,40))
for i in range(14):
    b.append(randint(0,40))

for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)