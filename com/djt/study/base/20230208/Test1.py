from typing import Dict

name = "zhangsan"


def func1():
    name = "lisi"
    print(name)


def func2():
    global name
    name = "lisi"
    print(name)


func1()
print(name)
func2()
print(name)

func3 = func2
func3()


def my_def(a, b, dis):
    return dis(a, b)


def add(a, b):
    return a + b


print(my_def(2, 3, add))

