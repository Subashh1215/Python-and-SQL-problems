# Q4. Number System Converter + GCD/LCM

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))


def convert_base(number, base):

    digits = "0123456789ABCDEF"

    if number == 0:
        return "0"

    result = ""

    while number > 0:
        remainder = number % base
        result = digits[remainder] + result
        number //= base

    return result


# GCD using Euclidean algorithm

a = num1
b = num2

while b != 0:
    remainder = a % b
    a = b
    b = remainder

gcd = a


# LCM

lcm = (num1 * num2) // gcd


print("Binary :", convert_base(num1, 2))
print("Octal :", convert_base(num1, 8))
print("Hexadecimal :", convert_base(num1, 16))
print("GCD :", gcd)
print("LCM :", lcm)