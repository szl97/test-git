def quicksort(arr):
    """
    Sort an array using the quicksort algorithm.

    Args:
        arr: A list of comparable elements to sort

    Returns:
        A new sorted list in ascending order
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    # Choose the middle element as pivot
    pivot = arr[len(arr) // 2]

    # Partition the array into three parts
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort left and right partitions
    return quicksort(left) + middle + quicksort(right)


if __name__ == "__main__":
    # Test the function with various inputs
    test_cases = [
        [3, 6, 8, 10, 1, 2, 1],
        [5, 2, 9, 1, 5, 6],
        [1],
        [],
        [3, 3, 3, 3],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]

    for test in test_cases:
        result = quicksort(test)
        print(f"Input:  {test}")
        print(f"Output: {result}")
        print()
