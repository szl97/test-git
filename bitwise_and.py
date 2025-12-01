def bitwise_and(a, b):
    """
    Perform bitwise AND operation on two inputs.

    Args:
        a: First operand (integer)
        b: Second operand (integer)

    Returns:
        Result of a & b (bitwise AND)
    """
    return a & b


if __name__ == "__main__":
    # Example usage
    result = bitwise_and(5, 3)
    print(f"5 & 3 = {result}")  # Output: 1

    result = bitwise_and(12, 10)
    print(f"12 & 10 = {result}")  # Output: 8
