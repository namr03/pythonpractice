x = int(input("Give me a number from 1 to 10000: "))


if x > 10000:
    print("It's higher than range")
    quit()

y = range(1,10000)
z = []


for i in y:
    if x % i == 0:
        z.append(i)
    i += 1
print("All divisors of", x , "are: " , "\n" , z)