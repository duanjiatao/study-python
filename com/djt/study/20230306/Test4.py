class A:
    def __init__(self):
        print("A", end=" ")
        super().__init__()


class B:
    def __init__(self):
        print("B", end=" ")
        super().__init__()


class C(A, B):
    def __init__(self):
        print("C", end=" ")
        # super().__init__()
        A.__init__(self)
        B.__init__(self)


print("MRO:", [x.__name__ for x in C.__mro__])
C()


# 限制给实例对象动态添加属性或方法
class CLanguage:
    # 限制属性或方法名
    __slots__ = ("name", "add", "info")


def func1(self, value):
    print("调用func1:", self.name, value)


# 动态为实例对象添加属性和方法
c = CLanguage()
c.name = "c"
c.info = func1
c.info(c, "ccc")
