a = input("Give me a string: ").lower()
b = a[len(a)::-1]
print(a)
print(b)
if a == b:
    print("Your word is palindrome")
else:
    print("Your word isn't palindrome")