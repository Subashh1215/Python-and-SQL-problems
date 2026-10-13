# Q3. String Analyzer

text = input("Enter a string: ")


reverse = ""

for char in text:
    reverse = char + reverse

print("Loop Reverse:", reverse)



slice_reverse = text[::-1]

print("Slice Reverse:", slice_reverse)


cleaned = ""

for char in text:
    if char != " ":
        cleaned = cleaned + char.lower()

if cleaned == cleaned[::-1]:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")



vowels = 0
consonants = 0
digits = 0

for char in text:

    if char.isdigit():
        digits += 1

    elif char.isalpha():

        if char.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1


print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)