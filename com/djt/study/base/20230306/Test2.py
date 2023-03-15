# 类的继承

class People:
    def say(self):
        print("我是一个人，名字叫：", self.name)


class Animal:
    def display(self):
        print("人也是高级动物")


class Person(People, Animal):
    pass


zhangsan = Person()
zhangsan.name = "张三"
zhangsan.say()
zhangsan.display()
print(Person.mro())
