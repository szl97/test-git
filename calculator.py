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


# Example usage
if __name__ == "__main__":
    # Test case 1
    calc = Calculator(2, 3, 4, 5)
    result = calc.calculate()
    print(f"2 * 3 + 4 * 5 = {result}")  # Output: 26

    # Test case 2
    calc2 = Calculator(10, 5, 3, 7)
    result2 = calc2.calculate()
    print(f"10 * 5 + 3 * 7 = {result2}")  # Output: 71
