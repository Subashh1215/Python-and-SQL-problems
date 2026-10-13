# Q9. Add Binary

a = input("a = ")
b = input("b = ")

i = len(a) - 1
j = len(b) - 1

carry = 0
result = ""


while i >= 0 or j >= 0 or carry:

    if i >= 0:
        bit_a = int(a[i])
        i -= 1
    else:
        bit_a = 0

    if j >= 0:
        bit_b = int(b[j])
        j -= 1
    else:
        bit_b = 0

    total = bit_a + bit_b + carry

    result = str(total % 2) + result

    carry = total // 2


print(result)