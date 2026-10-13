# Q1. Prime, Factorial, Fibonacci, Digit Sum & Reverse

N = int(input("Enter N: "))
number = int(input("Enter number: "))



print("Primes:", end=" ")

for num in range(2, N + 1):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

print()



factorial = 1

for i in range(1, N + 1):
    factorial = factorial * i

print("Factorial:", factorial)


a = 0
b = 1

print("Fibonacci:", end=" ")

for i in range(N):
    print(a, end=" ")

    c = a + b
    a = b
    b = c

print()


temp = abs(number)
digit_sum = 0

while temp > 0:
    digit = temp % 10
    digit_sum = digit_sum + digit
    temp = temp // 10

print("Digit Sum:", digit_sum)


temp = abs(number)
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if number < 0:
    reverse = -reverse

print("Reverse:", reverse)