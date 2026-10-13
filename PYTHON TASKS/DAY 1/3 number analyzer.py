a, b, c = map(int, input("Enter three numbers: ").split())

largest = max(a, b, c)
smallest = min(a, b, c)
average = (a + b + c) / 3

print("Largest:", largest)
print("Smallest:", smallest)
print(f"Average: {average:.2f}")

num = int(input("Enter a number to classify: "))

if num > 0:
    if num % 2 == 0:
        print("Classification: Positive and Even")
    else:
        print("Classification: Positive and Odd")

elif num < 0:
    if num % 2 == 0:
        print("Classification: Negative and Even")
    else:
        print("Classification: Negative and Odd")

else:
    print("Classification: Zero")