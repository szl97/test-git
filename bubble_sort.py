def bubble_sort(arr):
    """
    冒泡排序算法实现

    参数:
        arr: 需要排序的列表

    返回:
        排序后的列表

    时间复杂度: O(n²)
    空间复杂度: O(1)
    """
    if not arr:
        return arr

    n = len(arr)

    # 外层循环控制排序的轮数
    for i in range(n):
        # 优化：添加标志位，如果一轮循环中没有发生交换，说明已经排序完成
        swapped = False

        # 内层循环进行相邻元素的比较和交换
        # 每一轮会将最大的元素"冒泡"到末尾
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 交换相邻元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # 如果这一轮没有发生交换，说明数组已经有序，可以提前退出
        if not swapped:
            break

    return arr


def bubble_sort_descending(arr):
    """
    冒泡排序算法实现（降序）

    参数:
        arr: 需要排序的列表

    返回:
        降序排序后的列表
    """
    if not arr:
        return arr

    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            # 改变比较条件实现降序排序
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


# 测试代码
if __name__ == "__main__":
    # 测试升序排序
    test_arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_arr1)
    bubble_sort(test_arr1)
    print("升序排序后:", test_arr1)

    # 测试降序排序
    test_arr2 = [64, 34, 25, 12, 22, 11, 90]
    print("\n原始数组:", test_arr2)
    bubble_sort_descending(test_arr2)
    print("降序排序后:", test_arr2)

    # 测试空数组
    test_arr3 = []
    print("\n空数组测试:", bubble_sort(test_arr3))

    # 测试单元素数组
    test_arr4 = [1]
    print("单元素数组测试:", bubble_sort(test_arr4))

    # 测试已排序数组
    test_arr5 = [1, 2, 3, 4, 5]
    print("已排序数组测试:", bubble_sort(test_arr5))
