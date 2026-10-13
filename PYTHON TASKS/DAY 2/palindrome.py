# Q9. Palindrome Number

x = int(input("Enter an integer: "))

if x < 0:
    print(False)

else:
    original = x
    reverse = 0

    while x > 0:
        digit = x % 10
        reverse = reverse * 10 + digit
        x = x // 10

    if original == reverse:
        print(True)
    else:
        print(False)