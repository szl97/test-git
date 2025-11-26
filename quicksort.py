def quicksort(arr):
    """
    Sort a list using the quicksort algorithm.

    Quicksort is a divide-and-conquer algorithm that picks an element as pivot
    and partitions the array around the picked pivot. This implementation uses
    the last element as the pivot.

    Time Complexity:
        - Average case: O(n log n)
        - Worst case: O(n^2) - when the array is already sorted
        - Best case: O(n log n)

    Space Complexity: O(log n) due to recursive call stack

    Args:
        arr: List of comparable elements to be sorted

    Returns:
        A new sorted list (does not modify the original list)

    Examples:
        >>> quicksort([3, 6, 8, 10, 1, 2, 1])
        [1, 1, 2, 3, 6, 8, 10]
        >>> quicksort([5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5]
        >>> quicksort([1])
        [1]
        >>> quicksort([])
        []
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    # Choose the middle element as pivot for better average performance
    pivot_idx = len(arr) // 2
    pivot = arr[pivot_idx]

    # Partition: elements less than, equal to, and greater than pivot
    left = [x for i, x in enumerate(arr) if x < pivot]
    middle = [x for i, x in enumerate(arr) if x == pivot]
    right = [x for i, x in enumerate(arr) if x > pivot]

    # Recursively sort the partitions and combine
    return quicksort(left) + middle + quicksort(right)


def quicksort_inplace(arr, low=0, high=None):
    """
    Sort a list in-place using the quicksort algorithm.

    This version modifies the original array instead of creating new arrays,
    which is more memory efficient for large datasets.

    Args:
        arr: List of comparable elements to be sorted (modified in-place)
        low: Starting index of the partition to sort (default: 0)
        high: Ending index of the partition to sort (default: len(arr) - 1)

    Returns:
        None (modifies the input list in-place)

    Examples:
        >>> arr = [3, 6, 8, 10, 1, 2, 1]
        >>> quicksort_inplace(arr)
        >>> arr
        [1, 1, 2, 3, 6, 8, 10]
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Partition the array and get the pivot index
        pivot_idx = _partition(arr, low, high)

        # Recursively sort elements before and after partition
        quicksort_inplace(arr, low, pivot_idx - 1)
        quicksort_inplace(arr, pivot_idx + 1, high)


def _partition(arr, low, high):
    """
    Helper function to partition the array around a pivot.

    Uses the last element as pivot, places it at its correct position
    in sorted array, and places all smaller elements to left of pivot
    and all greater elements to right of pivot.

    Args:
        arr: List to partition
        low: Starting index
        high: Ending index

    Returns:
        Final index of the pivot element
    """
    pivot = arr[high]
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    # Test case 1: Random unsorted array
    test_arr1 = [3, 6, 8, 10, 1, 2, 1]
    print(f"Original array: {test_arr1}")
    sorted_arr1 = quicksort(test_arr1)
    print(f"Sorted array (functional): {sorted_arr1}")

    # Test case 2: In-place sorting
    test_arr2 = [3, 6, 8, 10, 1, 2, 1]
    print(f"\nOriginal array: {test_arr2}")
    quicksort_inplace(test_arr2)
    print(f"Sorted array (in-place): {test_arr2}")

    # Test case 3: Already sorted array
    test_arr3 = [1, 2, 3, 4, 5]
    print(f"\nAlready sorted: {test_arr3}")
    print(f"Result: {quicksort(test_arr3)}")

    # Test case 4: Reverse sorted array
    test_arr4 = [5, 4, 3, 2, 1]
    print(f"\nReverse sorted: {test_arr4}")
    print(f"Result: {quicksort(test_arr4)}")

    # Test case 5: Array with duplicates
    test_arr5 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"\nArray with duplicates: {test_arr5}")
    print(f"Result: {quicksort(test_arr5)}")

    # Test case 6: Single element
    test_arr6 = [42]
    print(f"\nSingle element: {test_arr6}")
    print(f"Result: {quicksort(test_arr6)}")

    # Test case 7: Empty array
    test_arr7 = []
    print(f"\nEmpty array: {test_arr7}")
    print(f"Result: {quicksort(test_arr7)}")

    # Test case 8: Floating point numbers
    test_arr8 = [3.14, 1.41, 2.71, 0.57, 1.73]
    print(f"\nFloating point: {test_arr8}")
    print(f"Result: {quicksort(test_arr8)}")

    # Test case 9: Negative numbers
    test_arr9 = [3, -1, 4, -5, 2, 0, -3]
    print(f"\nNegative numbers: {test_arr9}")
    print(f"Result: {quicksort(test_arr9)}")
