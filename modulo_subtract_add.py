class ModuloSubtractAdd:
    """
    A calculator class that computes (a % b) - c + d
    """

    def __init__(self, a, b, c, d):
        """
        Initialize the calculator with four numbers

        Args:
            a: First number (dividend)
            b: Second number (divisor for modulo)
            c: Third number (subtrahend)
            d: Fourth number (addend)
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def calculate(self):
        """
        Calculate and return (a % b) - c + d

        Returns:
            The result of (a % b) - c + d

        Raises:
            ZeroDivisionError: If b is zero
        """
        if self.b == 0:
            raise ZeroDivisionError("Cannot perform modulo with zero divisor")
        return (self.a % self.b) - self.c + self.d


# Example usage
if __name__ == "__main__":
    print("=== Testing calculate() method ((a % b) - c + d) ===")

    # Test case 1: 10 % 3 - 2 + 5 = 1 - 2 + 5 = 4
    calc1 = ModuloSubtractAdd(10, 3, 2, 5)
    result1 = calc1.calculate()
    print(f"(10 % 3) - 2 + 5 = {result1}")  # Output: 4

    # Test case 2: 17 % 5 - 1 + 8 = 2 - 1 + 8 = 9
    calc2 = ModuloSubtractAdd(17, 5, 1, 8)
    result2 = calc2.calculate()
    print(f"(17 % 5) - 1 + 8 = {result2}")  # Output: 9

    # Test case 3: 20 % 7 - 3 + 10 = 6 - 3 + 10 = 13
    calc3 = ModuloSubtractAdd(20, 7, 3, 10)
    result3 = calc3.calculate()
    print(f"(20 % 7) - 3 + 10 = {result3}")  # Output: 13

    # Test case 4: 15 % 4 - 5 + 2 = 3 - 5 + 2 = 0
    calc4 = ModuloSubtractAdd(15, 4, 5, 2)
    result4 = calc4.calculate()
    print(f"(15 % 4) - 5 + 2 = {result4}")  # Output: 0

    # Test zero division error
    print("\n=== Testing zero division error ===")
    try:
        calc5 = ModuloSubtractAdd(10, 0, 5, 3)
        result5 = calc5.calculate()
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")
