# Q8. Reverse Integer

x = int(input("Enter an integer: "))

sign = 1

if x < 0:
    sign = -1
    x = -x


reverse = 0

while x > 0:
    digit = x % 10
    reverse = reverse * 10 + digit
    x = x // 10


reverse = reverse * sign

print("Reversed Integer:", reverse)