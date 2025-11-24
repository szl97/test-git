def divide(a, b):
    """
    Divide two numbers.

    Args:
        a: Numerator (dividend)
        b: Denominator (divisor)

    Returns:
        The quotient of a divided by b

    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    # Test the function
    result = divide(10, 2)
    print(f"10 / 2 = {result}")

    # Test with float
    result2 = divide(7, 3)
    print(f"7 / 3 = {result2}")

    # Test error handling
    try:
        divide(5, 0)
    except ZeroDivisionError as e:
        print(f"Error: {e}")
