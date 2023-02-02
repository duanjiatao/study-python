# 测试递归调用
# 己知有一个数列：f(0) = 1，f(1) = 4，f(n + 2) = 2*f(n+ 1) +f(n)
def func1(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        return 2 * func1(n - 1) + func1(n - 1)


print(func1(10))

# 获取所有全局变量
print(globals())
