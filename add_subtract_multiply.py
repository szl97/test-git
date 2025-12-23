def add_subtract_multiply(a, b):
    """
    Calculate a + b - (a * b).

    Args:
        a: First number
        b: Second number

    Returns:
        The result of a + b - (a * b)
    """
    return a + b - (a * b)


if __name__ == "__main__":
    # Test the function with various inputs
    test_cases = [
        (3, 5),
        (10, 2),
        (0, 5),
        (4, 4),
        (-2, 3),
    ]

    for a, b in test_cases:
        result = add_subtract_multiply(a, b)
        print(f"{a} + {b} - ({a} * {b}) = {result}")
