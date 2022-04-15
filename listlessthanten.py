a = [1, 1, 2, 3, 5, 8, 13, 21, 55, 89]
b = int(input("Give me a number: "))
c = []
d = []
for i in a:
    if i < 5:
        c.append(i)
print(c)

for x in a:
    if x < b:
        d.append(x)
print(d)