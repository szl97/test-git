def quicksort(arr):
    """
    Sort an array using the quicksort algorithm.

    Args:
        arr: List of comparable elements to sort

    Returns:
        A new sorted list
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

    # Recursively sort and combine
    return quicksort(left) + middle + quicksort(right)


if __name__ == "__main__":
    # Test the function
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {test_array}")

    sorted_array = quicksort(test_array)
    print(f"Sorted array: {sorted_array}")

    # Additional test cases
    print("\nAdditional tests:")
    print(f"Empty array: {quicksort([])}")
    print(f"Single element: {quicksort([42])}")
    print(f"Already sorted: {quicksort([1, 2, 3, 4, 5])}")
    print(f"Reverse sorted: {quicksort([5, 4, 3, 2, 1])}")
    print(f"With duplicates: {quicksort([3, 1, 4, 1, 5, 9, 2, 6])}")
