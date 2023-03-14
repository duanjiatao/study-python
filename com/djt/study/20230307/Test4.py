# 装饰器

def funcA(func):
    print("执行funcA")
    func()
    return "funcA返回值"


@funcA
def funcB():
    print("执行funcB")


print(funcB)
print("=" * 20)


def funcC(func):
    def say(arc):
        print("say:", arc)
        func(arc)

    return say


@funcC
def funcD(a):
    print("funcD:", a)


funcD("python")
print("=" * 20)


def funcE(func):
    def say(*args, **kwargs):
        print("funcE say:", args, kwargs)
        func(*args, **kwargs)

    return say


@funcE
def funcF(a):
    print("funcF:", a)


@funcE
def funcG(a, b):
    print("funcG:", a, b)


funcF("666")
funcG("张三", "李四")
