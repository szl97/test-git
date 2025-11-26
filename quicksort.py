"""
快速排序实现
Quick Sort Implementation
"""


def quicksort(arr):
    """
    快速排序算法

    时间复杂度:
    - 最优: O(n log n)
    - 平均: O(n log n)
    - 最坏: O(n²)

    空间复杂度: O(log n) - 递归调用栈

    Args:
        arr: 待排序的列表

    Returns:
        排序后的列表
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


def quicksort_inplace(arr, low=0, high=None):
    """
    原地快速排序算法（更高效的版本）

    Args:
        arr: 待排序的列表
        low: 起始索引
        high: 结束索引
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort_inplace(arr, low, pivot_index - 1)
        quicksort_inplace(arr, pivot_index + 1, high)


def partition(arr, low, high):
    """
    分区函数，将数组分为小于pivot和大于pivot的两部分

    Args:
        arr: 数组
        low: 起始索引
        high: 结束索引

    Returns:
        pivot的最终位置
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
        [3, 3, 3, 3],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]

    print("快速排序测试:")
    print("-" * 50)

    for arr in test_cases:
        original = arr.copy()
        sorted_arr = quicksort(arr)
        print(f"原始数组: {original}")
        print(f"排序结果: {sorted_arr}")
        print()

    print("\n原地快速排序测试:")
    print("-" * 50)

    for arr in test_cases:
        original = arr.copy()
        quicksort_inplace(arr)
        print(f"原始数组: {original}")
        print(f"排序结果: {arr}")
        print()
