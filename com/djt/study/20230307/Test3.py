# 生成器
def intNum():
    print("开始执行")
    for n in range(5):
        yield n
        print("继续执行")


# print(list(intNum()))

num = intNum()

print(next(num))
print(num.__next__())
for i in num:
    print(i)

# 此时已经生成完所有数值
print(list(num))
