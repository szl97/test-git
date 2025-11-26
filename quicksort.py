def quicksort(arr):
    """
    Sort an array using the quicksort algorithm.

    Args:
        arr: List of comparable elements to sort

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

    # Recursively sort and combine
    return quicksort(left) + middle + quicksort(right)


def quicksort_inplace(arr, low=0, high=None):
    """
    Sort an array in-place using the quicksort algorithm.

    Args:
        arr: List of comparable elements to sort
        low: Starting index (default: 0)
        high: Ending index (default: len(arr) - 1)

    Returns:
        None (sorts the array in-place)
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quicksort_inplace(arr, low, pivot_index - 1)
        quicksort_inplace(arr, pivot_index + 1, high)


def partition(arr, low, high):
    """
    Partition helper function for in-place quicksort.

    Args:
        arr: List to partition
        low: Starting index
        high: Ending index

    Returns:
        The final position of the pivot element
    """
    # Choose the rightmost element as pivot
    pivot = arr[high]
    i = low - 1

    # Move all elements smaller than pivot to the left
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    # Test the function
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {test_array}")

    # Test the functional version
    sorted_array = quicksort(test_array.copy())
    print(f"Sorted array (functional): {sorted_array}")

    # Test the in-place version
    test_array_inplace = test_array.copy()
    quicksort_inplace(test_array_inplace)
    print(f"Sorted array (in-place): {test_array_inplace}")

    # Test with edge cases
    print(f"\nEdge cases:")
    print(f"Empty array: {quicksort([])}")
    print(f"Single element: {quicksort([5])}")
    print(f"Already sorted: {quicksort([1, 2, 3, 4, 5])}")
    print(f"Reverse sorted: {quicksort([5, 4, 3, 2, 1])}")
    print(f"Duplicates: {quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5])}")
