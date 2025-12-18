class AbcPlusD:
    """
    A class that calculates abc + d where a, b, c, d are input values.
    """

    def __init__(self, a, b, c, d):
        """
        Initialize the class with four values.

        Args:
            a: First value
            b: Second value
            c: Third value
            d: Fourth value
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def calculate(self):
        """
        Calculate and return abc + d.

        Returns:
            The result of a * b * c + d
        """
        return self.a * self.b * self.c + self.d


# Example usage
if __name__ == "__main__":
    # Example 1
    calc1 = AbcPlusD(2, 3, 4, 5)
    result1 = calc1.calculate()
    print(f"Example 1: a=2, b=3, c=4, d=5 -> abc + d = {result1}")

    # Example 2
    calc2 = AbcPlusD(1, 2, 3, 10)
    result2 = calc2.calculate()
    print(f"Example 2: a=1, b=2, c=3, d=10 -> abc + d = {result2}")

    # Example 3
    calc3 = AbcPlusD(5, 5, 5, 100)
    result3 = calc3.calculate()
    print(f"Example 3: a=5, b=5, c=5, d=100 -> abc + d = {result3}")
