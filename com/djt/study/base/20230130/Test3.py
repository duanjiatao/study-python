from functools import partial


def func1():
    return "1", "2", "3"


print(func1())
a, b, c = func1()
print(f"a={a}\nb={b}\nc={c}")


# 原函数
def func2(name, age):
    print(f"name={name} age={age}")


# 偏函数
peter_func = partial(func2, name="Peter")
peter_func(age=18)
