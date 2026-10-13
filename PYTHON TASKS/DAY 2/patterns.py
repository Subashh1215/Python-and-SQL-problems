# Q2. Patterns & Multiplication Grid

N = int(input("Enter N: "))


print("\nRight Triangle")

for i in range(1, N + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()



print("\nPyramid")

for i in range(1, N + 1):

    # Spaces
    for j in range(N - i):
        print(" ", end="")

    # Stars
    for j in range(2 * i - 1):
        print("*", end="")

    print()



print("\nNumber Triangle")

for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


print("\nMultiplication Grid")

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} × {j} = {i * j}", end="    ")
    print()