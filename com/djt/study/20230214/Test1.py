class People:
    # 类属性
    name = "xxx"
    age = 0

    def __init__(self):
        # 实例属性
        self.name = "无名"
        self.age = "1"

    # 实例方法
    def say(self):
        # 实例属性
        self.height = 180

    # 实例方法
    def hello(self):
        print(f"{self.name} 调用了hello")

    # 类方法
    @classmethod
    def info(cls):
        print("正在调用info方法", cls)

    # 静态方法
    @staticmethod
    def func(name):
        print("正在调用func方法", name)


zhangsan = People()
zhangsan.name = "张三"
zhangsan.age = 25
print(zhangsan.name)
print(zhangsan.age)

print("=" * 10)
lisi = People()
print(lisi.name)
print(lisi.age)

print("=" * 10)
print(People.name)
print(People.age)

# 通过对象调用实例方法
zhangsan.hello()

print("=" * 10)
# 通过类名调用实例方法(需要手动传入实例对象)
People.hello(zhangsan)

print("=" * 10)

# 通过类名调用类方法(对象也能调用，但是不推荐)
People.info()

# 调用静态方法
People.func("666")

print(People.hello(lisi))
