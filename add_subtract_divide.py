def add_subtract_divide(a, b):
    """
    Calculate a + b - (a / b)

    Args:
        a: First number (used in addition and as dividend)
        b: Second number (used in addition and as divisor)

    Returns:
        The result of a + b - (a / b)

    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a + b - (a / b)


if __name__ == "__main__":
    # Test the function
    print("=== Testing add_subtract_divide(a, b) = a + b - (a / b) ===")

    # Test case 1: 10 + 2 - (10 / 2) = 10 + 2 - 5 = 7
    result1 = add_subtract_divide(10, 2)
    print(f"10 + 2 - (10 / 2) = {result1}")

    # Test case 2: 15 + 3 - (15 / 3) = 15 + 3 - 5 = 13
    result2 = add_subtract_divide(15, 3)
    print(f"15 + 3 - (15 / 3) = {result2}")

    # Test case 3: 7 + 4 - (7 / 4) = 7 + 4 - 1.75 = 9.25
    result3 = add_subtract_divide(7, 4)
    print(f"7 + 4 - (7 / 4) = {result3}")

    # Test case 4: -10 + 5 - (-10 / 5) = -10 + 5 - (-2) = -3
    result4 = add_subtract_divide(-10, 5)
    print(f"-10 + 5 - (-10 / 5) = {result4}")

    # Test zero division error
    print("\n=== Testing zero division error ===")
    try:
        result5 = add_subtract_divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")
