def quicksort(arr):
    """
    使用快速排序算法对数组进行排序。

    快速排序是一种高效的分治排序算法，通过选择一个基准元素，
    将数组分为小于和大于基准的两部分，然后递归排序这两部分。

    时间复杂度：
        - 最优/平均情况: O(n log n)
        - 最坏情况: O(n²) (当数组已经排序或逆序时)

    空间复杂度：O(log n) - 递归调用栈的深度

    Args:
        arr: 需要排序的数字列表

    Returns:
        排序后的新列表（不修改原数组）

    Examples:
        >>> quicksort([3, 6, 8, 10, 1, 2, 1])
        [1, 1, 2, 3, 6, 8, 10]

        >>> quicksort([5, 2, 9, 1, 7, 6, 3])
        [1, 2, 3, 5, 6, 7, 9]
    """
    # 基础情况：空数组或单元素数组已经是有序的
    if len(arr) <= 1:
        return arr

    # 选择中间元素作为基准（pivot）
    # 这种选择方式可以减少在已排序数组上的性能退化
    pivot = arr[len(arr) // 2]

    # 将数组分为三部分：
    # 1. 小于基准的元素
    # 2. 等于基准的元素（处理重复元素）
    # 3. 大于基准的元素
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # 递归排序左右两部分，然后合并结果
    return quicksort(left) + middle + quicksort(right)


def quicksort_inplace(arr, low=0, high=None):
    """
    原地快速排序实现（不创建新数组，直接修改输入数组）。

    这个版本的空间复杂度更优，因为不需要额外的数组空间。

    Args:
        arr: 需要排序的数字列表（会被直接修改）
        low: 排序范围的起始索引（默认为0）
        high: 排序范围的结束索引（默认为数组长度-1）

    Returns:
        None（直接修改输入数组）

    Examples:
        >>> arr = [3, 6, 8, 10, 1, 2, 1]
        >>> quicksort_inplace(arr)
        >>> arr
        [1, 1, 2, 3, 6, 8, 10]
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        # 分区操作，返回基准元素的最终位置
        pivot_index = partition(arr, low, high)

        # 递归排序基准左右两侧的子数组
        quicksort_inplace(arr, low, pivot_index - 1)
        quicksort_inplace(arr, pivot_index + 1, high)


def partition(arr, low, high):
    """
    分区辅助函数，用于原地快速排序。

    选择最右边的元素作为基准，将小于基准的元素移到左边，
    大于基准的元素移到右边。

    Args:
        arr: 数组
        low: 分区范围的起始索引
        high: 分区范围的结束索引

    Returns:
        基准元素的最终位置索引
    """
    # 选择最右边的元素作为基准
    pivot = arr[high]

    # i 指向小于基准的区域的最后一个元素
    i = low - 1

    # 遍历 low 到 high-1 的所有元素
    for j in range(low, high):
        # 如果当前元素小于等于基准
        if arr[j] <= pivot:
            i += 1
            # 交换元素，将小的元素移到左边
            arr[i], arr[j] = arr[j], arr[i]

    # 将基准元素放到正确的位置（i+1）
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


if __name__ == "__main__":
    # 测试用例1：常规无序数组
    test_arr1 = [3, 6, 8, 10, 1, 2, 1]
    print(f"原始数组: {test_arr1}")
    sorted_arr1 = quicksort(test_arr1)
    print(f"快速排序后: {sorted_arr1}")
    print()

    # 测试用例2：另一个无序数组
    test_arr2 = [5, 2, 9, 1, 7, 6, 3]
    print(f"原始数组: {test_arr2}")
    sorted_arr2 = quicksort(test_arr2)
    print(f"快速排序后: {sorted_arr2}")
    print()

    # 测试用例3：已排序数组
    test_arr3 = [1, 2, 3, 4, 5]
    print(f"已排序数组: {test_arr3}")
    sorted_arr3 = quicksort(test_arr3)
    print(f"快速排序后: {sorted_arr3}")
    print()

    # 测试用例4：逆序数组
    test_arr4 = [5, 4, 3, 2, 1]
    print(f"逆序数组: {test_arr4}")
    sorted_arr4 = quicksort(test_arr4)
    print(f"快速排序后: {sorted_arr4}")
    print()

    # 测试用例5：包含重复元素的数组
    test_arr5 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"包含重复元素: {test_arr5}")
    sorted_arr5 = quicksort(test_arr5)
    print(f"快速排序后: {sorted_arr5}")
    print()

    # 测试用例6：原地排序
    test_arr6 = [3, 6, 8, 10, 1, 2, 1]
    print(f"原地排序测试 - 原始数组: {test_arr6}")
    quicksort_inplace(test_arr6)
    print(f"原地快速排序后: {test_arr6}")
    print()

    # 测试用例7：边界情况 - 空数组
    test_arr7 = []
    print(f"空数组: {test_arr7}")
    sorted_arr7 = quicksort(test_arr7)
    print(f"快速排序后: {sorted_arr7}")
    print()

    # 测试用例8：边界情况 - 单元素数组
    test_arr8 = [42]
    print(f"单元素数组: {test_arr8}")
    sorted_arr8 = quicksort(test_arr8)
    print(f"快速排序后: {sorted_arr8}")
