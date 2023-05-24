class People:
    def __init__(self, name):
        print("People__init__被调用")
        self.name = name

    def say(self):
        print("我是人，名字为：", self.name)


class Animal:
    def __init__(self, food):
        print("Animal__init__被调用")
        self.food = food

    def display(self):
        print("我是动物,我吃", self.food)


class Person(People, Animal):

    # 自定义构造方法
    def __init__(self, name, food):
        # 调用 People 类的构造方法
        super().__init__(name)
        # super(Person,self).__init__(name) #执行效果和上一行相同
        # People.__init__(self, name)  # 使用未绑定方法调用 People 类构造方法
        # 调用其它父类的构造方法，需手动给 self 传值
        Animal.__init__(self, food)


per = Person("zhangsan", "熟食")
per.say()
per.display()
