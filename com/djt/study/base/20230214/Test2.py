class A:
    __name = '张三'
    age = 18

    def __init__(self, a: str, b: str):
        self.a = a
        self.b = b
        print(f"构造对象A(a={a},b={b})")

    @staticmethod
    def fun1():
        print("静态方法无法访问类属性__name与age")

    @classmethod
    def fun2(cls):
        print(f"类方法可以访问类私有属性__name={cls.__name} age={cls.age}")

    @classmethod
    def func3(cls, a: str, b: str):
        return cls(a, b)


A.fun1()
A.fun2()
A.func3('1', '2')
