def bitwise_and(a, b):
    """
    计算两个数的按位与操作

    参数:
        a: 第一个整数
        b: 第二个整数

    返回:
        a & b 的结果
    """
    return a & b


if __name__ == "__main__":
    # 测试示例
    print(f"5 & 3 = {bitwise_and(5, 3)}")  # 101 & 011 = 001 = 1
    print(f"12 & 10 = {bitwise_and(12, 10)}")  # 1100 & 1010 = 1000 = 8
    print(f"15 & 7 = {bitwise_and(15, 7)}")  # 1111 & 0111 = 0111 = 7
