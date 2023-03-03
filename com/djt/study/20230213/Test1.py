from types import MethodType


class People:
    # 类属性
    id = "未知"

    def __init__(self, name, age, address):
        # 实例属性
        self.name = name
        self.age = age
        self.address = address

    def say(self, content):
        print(f"{self.name}说:{content}")

    def __str__(self):
        return f"ID:{self.id} 姓名:{self.name} 年龄:{self.age} 住址:{self.address}"

    # 通过方法方法添加实例属性
    def go(self):
        self.weight = 150


# 访问类属性
print(People.id)
# 修改类属性（注意：不能通过对象修改类属性，其操作相当于给对象添加新的实例属性）
People.id = "123"
print(People.id)

# 动态添加类属性
People.money = 100
print(People.money)

# 构造对象
zhang_san = People("张三", 18, "深圳")
print(zhang_san)
zhang_san.say("你好")
zhang_san.money = 100
print(zhang_san.money)
del zhang_san.money


def info(self):
    print("调用info", self)


# 对象动态添加foo函数
zhang_san.foo = info
zhang_san.foo(zhang_san)

# lambda表达式
zhang_san.bar = lambda self: print('lambda 表达式', self)
zhang_san.bar(zhang_san)

# MethodType
zhang_san.info = MethodType(info, zhang_san)
zhang_san.info()

# 提前调用相当于新增了weight属性
# print("体重:", zhang_san.weight)
zhang_san.go()
print("体重:", zhang_san.weight)
