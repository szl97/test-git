class SubtractSubtractDivision:
    """
    A calculator class that computes a - b - (a / b)
    """

    def __init__(self, a, b):
        """
        Initialize the calculator with two numbers

        Args:
            a: First number (numerator and minuend)
            b: Second number (divisor and subtrahend)
        """
        self.a = a
        self.b = b

    def calculate(self):
        """
        Calculate and return a - b - (a / b)

        Returns:
            The result of a - b - (a / b)

        Raises:
            ZeroDivisionError: If b is zero
        """
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.a - self.b - (self.a / self.b)


# Example usage
if __name__ == "__main__":
    print("=== Testing calculate() method (a - b - (a / b)) ===")

    # Test case 1: 10 - 2 - (10 / 2) = 10 - 2 - 5 = 3
    calc1 = SubtractSubtractDivision(10, 2)
    result1 = calc1.calculate()
    print(f"10 - 2 - (10 / 2) = {result1}")  # Output: 3.0

    # Test case 2: 20 - 4 - (20 / 4) = 20 - 4 - 5 = 11
    calc2 = SubtractSubtractDivision(20, 4)
    result2 = calc2.calculate()
    print(f"20 - 4 - (20 / 4) = {result2}")  # Output: 11.0

    # Test case 3: 15 - 3 - (15 / 3) = 15 - 3 - 5 = 7
    calc3 = SubtractSubtractDivision(15, 3)
    result3 = calc3.calculate()
    print(f"15 - 3 - (15 / 3) = {result3}")  # Output: 7.0

    # Test case 4: 100 - 10 - (100 / 10) = 100 - 10 - 10 = 80
    calc4 = SubtractSubtractDivision(100, 10)
    result4 = calc4.calculate()
    print(f"100 - 10 - (100 / 10) = {result4}")  # Output: 80.0

    # Test zero division error
    print("\n=== Testing zero division error ===")
    try:
        calc5 = SubtractSubtractDivision(10, 0)
        result5 = calc5.calculate()
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")
