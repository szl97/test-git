"""
冒泡排序实现
Bubble Sort Implementation
"""


def bubblesort(arr):
    """
    冒泡排序算法

    时间复杂度:
    - 最优: O(n) - 当数组已经有序时
    - 平均: O(n²)
    - 最坏: O(n²)

    空间复杂度: O(1) - 原地排序

    Args:
        arr: 待排序的列表

    Returns:
        排序后的列表
    """
    n = len(arr)
    result = arr.copy()

    for i in range(n):
        # 优化：如果一轮遍历中没有发生交换，说明已经有序
        swapped = False

        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        if not swapped:
            break

    return result


def bubblesort_inplace(arr):
    """
    原地冒泡排序算法（直接修改传入的数组）

    Args:
        arr: 待排序的列表
    """
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


def bubblesort_desc(arr):
    """
    冒泡排序（降序）

    Args:
        arr: 待排序的列表

    Returns:
        降序排序后的列表
    """
    n = len(arr)
    result = arr.copy()

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if result[j] < result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        if not swapped:
            break

    return result


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
        [3, 3, 3, 3],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5]  # 已排序数组
    ]

    print("冒泡排序测试（升序）:")
    print("-" * 50)

    for arr in test_cases:
        original = arr.copy()
        sorted_arr = bubblesort(arr)
        print(f"原始数组: {original}")
        print(f"排序结果: {sorted_arr}")
        print()

    print("\n冒泡排序测试（降序）:")
    print("-" * 50)

    for arr in test_cases:
        original = arr.copy()
        sorted_arr = bubblesort_desc(arr)
        print(f"原始数组: {original}")
        print(f"排序结果: {sorted_arr}")
        print()

    print("\n原地冒泡排序测试:")
    print("-" * 50)

    for arr in test_cases:
        original = arr.copy()
        bubblesort_inplace(arr)
        print(f"原始数组: {original}")
        print(f"排序结果: {arr}")
        print()
