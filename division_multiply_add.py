class DivisionMultiplyAdd:
    """
    A calculator class that computes (a/b) * c + d
    """

    def __init__(self, a, b, c, d):
        """
        Initialize the calculator with four numbers

        Args:
            a: First number (numerator)
            b: Second number (divisor)
            c: Third number (multiplier)
            d: Fourth number (addend)
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def calculate(self):
        """
        Calculate and return (a/b) * c + d

        Returns:
            The result of (a/b) * c + d

        Raises:
            ZeroDivisionError: If b is zero
        """
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return (self.a / self.b) * self.c + self.d

    def calculate_subtract(self):
        """
        Calculate and return (a/b) * c - d

        Returns:
            The result of (a/b) * c - d

        Raises:
            ZeroDivisionError: If b is zero
        """
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return (self.a / self.b) * self.c - self.d


# Example usage
if __name__ == "__main__":
    print("=== Testing calculate() method ((a/b) * c + d) ===")

    # Test case 1: 10/2 * 3 + 4 = 5 * 3 + 4 = 19
    calc1 = DivisionMultiplyAdd(10, 2, 3, 4)
    result1 = calc1.calculate()
    print(f"(10 / 2) * 3 + 4 = {result1}")  # Output: 19.0

    # Test case 2: 20/4 * 5 + 10 = 5 * 5 + 10 = 35
    calc2 = DivisionMultiplyAdd(20, 4, 5, 10)
    result2 = calc2.calculate()
    print(f"(20 / 4) * 5 + 10 = {result2}")  # Output: 35.0

    # Test case 3: 15/3 * 2 + 7 = 5 * 2 + 7 = 17
    calc3 = DivisionMultiplyAdd(15, 3, 2, 7)
    result3 = calc3.calculate()
    print(f"(15 / 3) * 2 + 7 = {result3}")  # Output: 17.0

    # Test zero division error
    print("\n=== Testing zero division error ===")
    try:
        calc4 = DivisionMultiplyAdd(10, 0, 5, 3)
        result4 = calc4.calculate()
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")

    # Test calculate_subtract method
    print("\n=== Testing calculate_subtract() method ((a/b) * c - d) ===")

    # Test case 1: 10/2 * 3 - 4 = 5 * 3 - 4 = 11
    calc5 = DivisionMultiplyAdd(10, 2, 3, 4)
    result5 = calc5.calculate_subtract()
    print(f"(10 / 2) * 3 - 4 = {result5}")  # Output: 11.0

    # Test case 2: 20/4 * 5 - 10 = 5 * 5 - 10 = 15
    calc6 = DivisionMultiplyAdd(20, 4, 5, 10)
    result6 = calc6.calculate_subtract()
    print(f"(20 / 4) * 5 - 10 = {result6}")  # Output: 15.0

    # Test case 3: 15/3 * 2 - 7 = 5 * 2 - 7 = 3
    calc7 = DivisionMultiplyAdd(15, 3, 2, 7)
    result7 = calc7.calculate_subtract()
    print(f"(15 / 3) * 2 - 7 = {result7}")  # Output: 3.0
