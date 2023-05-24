import numpy as np


def test1():
    # 创建一维数组
    a1 = np.array([1, 2, 3, 4, 5])
    print(type(a1))
    print(a1)

    # 创建二维数组
    a2 = np.array([[1, 2, 3], [4, 5, 6]])
    print(a2)
    print(a2.shape)
    # 索引与切片
    print(a2[0, 0])
    print(a2[1, 2])
    print(a2[:, 1])
    # 数组压平
    print(a2.ravel())

    a3 = np.arange(10)
    print(a3)


def test2():
    """
    数组加减乘除必须同维度且元素个数相同
    :return:
    """
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([6, 7, 8, 9, 10])

    # 数组加法
    c = a + b
    print(c)

    # 数组减法
    d = a - b
    print(d)

    # 数组乘法
    e = a * b
    print(e)

    # 数组除法
    f = a / b
    print(f)

    # 数组取反
    g = -a
    print(g)

    # 数组求和
    h = np.sum(a)
    print(h)

    # 数组求平均值
    i = np.mean(a)
    print(i)


def test3():
    """
    常用方法
    :return:
    """
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print(np.add(a, b))
    print(np.subtract(a, b))
    print(np.multiply(a, b))
    print(np.divide(a, b))
    print(np.power(a, b))
    print(np.sqrt(a))
    print(np.exp(a))
    print(np.sin(a))
    print(np.cos(a))
    print(np.log(a))


def test4():
    print()
    # 元素都是0的数组
    a = np.zeros((2, 3))
    print(a)

    print('=' * 50)
    a = np.zeros((2, 3, 3))
    print(a)

    print('=' * 50)
    # 元素都是1的数组
    a = np.ones((2, 3, 3, 3))
    print(a)

    print('=' * 50)
    # 常量数组
    a = np.full((2, 2), 7)
    print(a)

    print('=' * 50)
    # 单位矩阵
    a = np.eye(2, dtype=int)
    print(a)

    print('=' * 50)
    # 空数组
    a = np.empty((3, 2))
    print(a)

    print('=' * 50)
    a = np.ones((2, 2, 2, 2, 2))
    # 维度数
    print(a.ndim)

    print('=' * 50)
    # 比较大小
    b = np.greater(np.zeros(3), np.ones(3))
    print(b)
