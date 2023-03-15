# 空函数 无实际意义
def func_pass():
    pass


# 获取字符串长度函数
def get_str_len(str):
    """
    获取字符串长度
    :param str: 字符串
    :return: 长度
    """
    length = 0
    for _ in str:
        length += 1
    return length


func_pass()
print(get_str_len("123"))
print(get_str_len("123456"))


# help(get_str_len)

def test_param(obj):
    obj += obj
    print("形参值:", obj)


print("-------值传递-------")
a = "Hello Python "
print("原值:", a)
test_param(a)
print("实参值:", a)

print("-------引用传递-------")
b = [1, 2, 3]
print("原值:", b)
test_param(b)
print("实参值:", b)
