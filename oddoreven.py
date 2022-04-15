num = int(input("Write any number you want: "))
check = int(input("Write a number to divide by:"))

if num % 2 == 0:
    if num % 2 == 0 and num % 4 == 0:
        print("Your number is even and it is a multiple of 4")
    else:
        print("Your number is even")
elif num % 2 > 0:
    print("Your number is odd")
else:
    print("Your number can't be negative")

if num % check == 0:
    print("Your number divides evenly with second number")
else:
    print("Your number isn't dividing evenly with second number")