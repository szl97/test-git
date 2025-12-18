class Calculator:
    """
    A calculator class that computes a*b + c*d
    """

    def __init__(self, a, b, c, d):
        """
        Initialize the calculator with four numbers

        Args:
            a: First number
            b: Second number
            c: Third number
            d: Fourth number
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def calculate(self):
        """
        Calculate and return a*b + c*d

        Returns:
            The result of a*b + c*d
        """
        return self.a * self.b + self.c * self.d

    def calculate_division(self):
        """
        Calculate and return a/b + c/d

        Returns:
            The result of a/b + c/d

        Raises:
            ZeroDivisionError: If b or d is zero
        """
        if self.b == 0 or self.d == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.a / self.b + self.c / self.d


# Example usage
if __name__ == "__main__":
    # Test multiplication method
    print("=== Testing calculate() method (a*b + c*d) ===")
    calc = Calculator(2, 3, 4, 5)
    result = calc.calculate()
    print(f"2 * 3 + 4 * 5 = {result}")  # Output: 26

    calc2 = Calculator(10, 5, 3, 7)
    result2 = calc2.calculate()
    print(f"10 * 5 + 3 * 7 = {result2}")  # Output: 71

    # Test division method
    print("\n=== Testing calculate_division() method (a/b + c/d) ===")
    calc3 = Calculator(10, 2, 15, 3)
    result3 = calc3.calculate_division()
    print(f"10 / 2 + 15 / 3 = {result3}")  # Output: 10.0

    calc4 = Calculator(20, 4, 30, 6)
    result4 = calc4.calculate_division()
    print(f"20 / 4 + 30 / 6 = {result4}")  # Output: 10.0

    # Test zero division error
    print("\n=== Testing zero division error ===")
    try:
        calc5 = Calculator(10, 0, 15, 3)
        result5 = calc5.calculate_division()
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")
