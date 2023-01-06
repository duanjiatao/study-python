import time

import taichi as ti

ti.init(arch=ti.cpu)


# Checks if a positive integer is a prime number
@ti.func
def is_prime(n: int):
    result = True
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            result = False
            break
    return result


# Traverses the range between 2 and n
# Counts the primes according to the return of is_prime()
@ti.kernel
def count_primes(n: int) -> int:
    count = 0
    for k in range(2, n):
        if is_prime(k):
            count += 1

    return count


start = time.perf_counter()
nums = count_primes(1000000)
end = time.perf_counter()
print(f"素数个数:{nums} 耗时:{end - start} s")
# 未使用taichi输出：素数个数:78498 耗时:4.0905916 s
# 使用taichi-cpu输出：素数个数:78498 耗时:0.1334423 s
