# Q3. Number Analyzer

start = int(input("Start: "))
end = int(input("End: "))


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def is_perfect(n):
    if n <= 1:
        return False

    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n


def is_armstrong(n):
    if n < 0:
        return False

    temp = n
    digits = 0

    if n == 0:
        digits = 1
    else:
        while temp > 0:
            digits += 1
            temp //= 10

    temp = n
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == n


def is_palindrome(n):
    if n < 0:
        return False

    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10

    return original == reverse


def digit_sum(n):
    n = abs(n)
    total = 0

    if n == 0:
        return 0

    while n > 0:
        total += n % 10
        n //= 10

    return total


def digit_count(n):
    n = abs(n)

    if n == 0:
        return 1

    count = 0

    while n > 0:
        count += 1
        n //= 10

    return count


def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary = ""

    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n //= 2

    return binary


print()
print(f"{'Number':<8}{'Prime':<8}{'Perfect':<10}"
      f"{'Armstrong':<12}{'Palindrome':<12}"
      f"{'Digit Sum':<12}{'Digits':<8}{'Binary'}")

for number in range(start, end + 1):

    prime = "Yes" if is_prime(number) else "No"
    perfect = "Yes" if is_perfect(number) else "No"
    armstrong = "Yes" if is_armstrong(number) else "No"
    palindrome = "Yes" if is_palindrome(number) else "No"

    print(
        f"{number:<8}"
        f"{prime:<8}"
        f"{perfect:<10}"
        f"{armstrong:<12}"
        f"{palindrome:<12}"
        f"{digit_sum(number):<12}"
        f"{digit_count(number):<8}"
        f"{decimal_to_binary(number)}"
    )