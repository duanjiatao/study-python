# 列表推导式
a_range = range(10)
a_list = [num ** 2 for num in a_range]
print(a_list)

a_list = [num ** 2 for num in a_range if num % 2 == 0]
print(a_list)

b_list = [(i, j) for i in range(2) for j in range(3)]
print(b_list)

b_list = [(i, j) for i in range(5) for j in range(6) if i == j]
print(b_list)

# 元组推导式
a_tup = (i for i in range(5))
# 生成器对象
print(a_tup)
for i in a_tup:
    print(i, end="")
else:
    print()
# 遍历后 对象为空
print(tuple(a_tup))

# 字典推导式
a_dict = {x: x ** 2 for x in range(6)}
print(a_dict)
