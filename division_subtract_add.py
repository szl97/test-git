class DivisionSubtractAdd:
    """
    A calculator class that computes (a/b) - c + d
    """

    def __init__(self, a, b, c, d):
        """
        Initialize the calculator with four numbers

        Args:
            a: First number (numerator)
            b: Second number (divisor)
            c: Third number (subtrahend)
            d: Fourth number (addend)
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def calculate(self):
        """
        Calculate and return (a/b) - c + d

        Returns:
            The result of (a/b) - c + d

        Raises:
            ZeroDivisionError: If b is zero
        """
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return (self.a / self.b) - self.c + self.d


# Example usage
if __name__ == "__main__":
    print("=== Testing calculate() method ((a/b) - c + d) ===")

    # Test case 1: 10/2 - 3 + 4 = 5 - 3 + 4 = 6
    calc1 = DivisionSubtractAdd(10, 2, 3, 4)
    result1 = calc1.calculate()
    print(f"(10 / 2) - 3 + 4 = {result1}")  # Output: 6.0

    # Test case 2: 20/4 - 5 + 10 = 5 - 5 + 10 = 10
    calc2 = DivisionSubtractAdd(20, 4, 5, 10)
    result2 = calc2.calculate()
    print(f"(20 / 4) - 5 + 10 = {result2}")  # Output: 10.0

    # Test case 3: 15/3 - 2 + 7 = 5 - 2 + 7 = 10
    calc3 = DivisionSubtractAdd(15, 3, 2, 7)
    result3 = calc3.calculate()
    print(f"(15 / 3) - 2 + 7 = {result3}")  # Output: 10.0

    # Test case 4: 100/10 - 8 + 3 = 10 - 8 + 3 = 5
    calc4 = DivisionSubtractAdd(100, 10, 8, 3)
    result4 = calc4.calculate()
    print(f"(100 / 10) - 8 + 3 = {result4}")  # Output: 5.0

    # Test zero division error
    print("\n=== Testing zero division error ===")
    try:
        calc5 = DivisionSubtractAdd(10, 0, 5, 3)
        result5 = calc5.calculate()
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")
