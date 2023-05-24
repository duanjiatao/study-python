import time

import taichi as ti

ti.init(arch=ti.cpu)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@ti.func
def fibonacci2(n):
    n1, n2 = 0, 1
    count = 0
    if n <= 1:
        return n
    else:
        while count < n:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return n1


@ti.kernel
def run():
    start = time.perf_counter()
    n = 50

    stop = time.perf_counter()
    print(f"n={n} value={fibonacci2(50)} 耗时:{stop - start}")


run()
