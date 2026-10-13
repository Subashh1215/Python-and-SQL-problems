# Q10. Happy Number

n = int(input("Enter a positive integer: "))

seen = set()

while n != 1 and n not in seen:

    seen.add(n)

    total = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        total += digit ** 2
        temp //= 10

    n = total


if n == 1:
    print(True)
else:
    print(False)