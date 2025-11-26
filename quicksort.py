"""
快速排序实现

快速排序是一种高效的排序算法，采用分治策略。
时间复杂度：平均 O(n log n)，最坏 O(n²)
空间复杂度：O(log n)
"""


def quicksort(arr):
    """
    快速排序函数

    Args:
        arr: 待排序的数组

    Returns:
        排序后的新数组
    """
    if len(arr) <= 1:
        return arr

    # 选择中间元素作为基准值
    pivot = arr[len(arr) // 2]

    # 分区：小于基准值的元素
    left = [x for x in arr if x < pivot]

    # 等于基准值的元素
    middle = [x for x in arr if x == pivot]

    # 大于基准值的元素
    right = [x for x in arr if x > pivot]

    # 递归排序并合并
    return quicksort(left) + middle + quicksort(right)


def quicksort_inplace(arr, low=0, high=None):
    """
    原地快速排序（不使用额外空间）

    Args:
        arr: 待排序的数组
        low: 起始索引
        high: 结束索引
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        # 分区操作
        pivot_index = partition(arr, low, high)

        # 递归排序左右子数组
        quicksort_inplace(arr, low, pivot_index - 1)
        quicksort_inplace(arr, pivot_index + 1, high)


def partition(arr, low, high):
    """
    分区函数，返回基准值的最终位置

    Args:
        arr: 数组
        low: 起始索引
        high: 结束索引

    Returns:
        基准值的索引位置
    """
    # 选择最右边的元素作为基准值
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # 将基准值放到正确的位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    # 测试用例
    test_array = [64, 34, 25, 12, 22, 11, 90]

    print("原始数组:", test_array)

    # 测试函数式快排
    sorted_array = quicksort(test_array.copy())
    print("快排结果:", sorted_array)

    # 测试原地快排
    inplace_array = test_array.copy()
    quicksort_inplace(inplace_array)
    print("原地快排结果:", inplace_array)

    # 边界测试
    print("\n边界测试:")
    print("空数组:", quicksort([]))
    print("单元素:", quicksort([1]))
    print("已排序:", quicksort([1, 2, 3, 4, 5]))
    print("逆序:", quicksort([5, 4, 3, 2, 1]))
    print("重复元素:", quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5]))
