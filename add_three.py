def add_three(a, b, c):
    """
    Add three numbers together.

    Args:
        a: First number
        b: Second number
        c: Third number

    Returns:
        The sum of a, b, and c
    """
    return a + b + c


if __name__ == "__main__":
    # Test the function
    result = add_three(1, 2, 3)
    print(f"1 + 2 + 3 = {result}")

    # Test with floats
    result2 = add_three(1.5, 2.5, 3.0)
    print(f"1.5 + 2.5 + 3.0 = {result2}")
