import time

import taichi as ti

# 设置 Taichi 运行环境
ti.init()


# 定义斐波那契数列计算函数
@ti.kernel
def fibonacci(n: int) -> int:
    # 初始化前两个数
    a = 0
    b = 1
    # 计算第 n 个数
    for _ in range(1, n):
        c = a + b
        a = b
        b = c
    return a


start = time.perf_counter()
n = 50
for i in range(1, n + 1):
    value = fibonacci(i)
    print(f'{i}={value}')
stop = time.perf_counter()
print(f"耗时:{stop - start}")
