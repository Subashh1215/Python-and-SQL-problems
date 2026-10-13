# Q8. String to Integer (atoi)

s = input("Enter string: ")

i = 0
n = len(s)

# Skip leading spaces

while i < n and s[i] == " ":
    i += 1


# Determine sign

sign = 1

if i < n and s[i] == '+':
    i += 1

elif i < n and s[i] == '-':
    sign = -1
    i += 1


# Convert digits

number = 0

while i < n and '0' <= s[i] <= '9':

    digit = ord(s[i]) - ord('0')

    number = number * 10 + digit

    i += 1


number = number * sign

print(number)