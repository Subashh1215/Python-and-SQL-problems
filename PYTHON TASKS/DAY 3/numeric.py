# Q1. Type Casting & Numeric Operations

integer_input = input("Integer: ")
decimal_input = input("Decimal: ")

try:
    integer_value = int(integer_input)
    float_value = float(decimal_input)

    print("Integer Value :", integer_value)
    print("Integer Type :", type(integer_value).__name__)

    print("Float Value :", float_value)
    print("Float Type :", type(float_value).__name__)

    print("Rounded Value :", round(float_value))

    # Numeric operations
    print(f"{integer_value} / {integer_value - 13} = "
          f"{integer_value / (integer_value - 13):.4f}")

    print(f"{integer_value} // {integer_value - 13} = "
          f"{integer_value // (integer_value - 13)}")

    print(f"{integer_value} % {integer_value - 13} = "
          f"{integer_value % (integer_value - 13)}")

    print(f"{integer_value} ** 2 = {integer_value ** 2}")

except ValueError:
    print("Invalid numeric input.")