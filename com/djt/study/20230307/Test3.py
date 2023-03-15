# 生成器
def intNum():
    print("开始执行")
    for n in range(5):
        yield n
        print(f"继续执行:{n}")


# print(list(intNum()))

num = intNum()
print(type(num))
print("=" * 20)

print(next(num))
print(num.__next__())
for i in num:
    print(i)

# 此时已经生成完所有数值
print(list(num))

print("=" * 20)


def num2():
    yield 666
    print("num2执行完成")


n = num2()
print(type(n))
print(n.__next__())
for i in num:
    print(n)
