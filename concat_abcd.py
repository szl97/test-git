class ABCDConcatenator:
    """Concatenate four values into a single string."""

    def concatenate(self, a, b, c, d):
        return f"{a}{b}{c}{d}"


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 5:
        raise SystemExit("Usage: python concat_abcd.py a b c d")

    concatenator = ABCDConcatenator()
    result = concatenator.concatenate(*sys.argv[1:])
    print(result)
