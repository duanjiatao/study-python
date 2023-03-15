class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('__name', '__age', '__gender')

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    # 访问器 - getter方法
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    # 访问器 - getter方法
    @property
    def age(self):
        return self.__age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self.__age = age

    # 访问器 - getter方法
    @property
    def gender(self):
        return self.__gender

    def show(self):
        print('姓名: %s 性别: %s 年龄: %s' % (self.__name, self.__gender, self.__age))

    @staticmethod
    def is_adult(cls):
        if cls.age >= 18:
            print('%s 是成年人' % cls.name)
            return True
        else:
            print('%s 是未成年' % cls.name)
            return False


def main():
    person = Person('张三', 12, '男')
    person.show()
    Person.is_adult(person)
    person.name = '李四'
    person.show()
    person.age = 22
    person.show()


if __name__ == '__main__':
    main()
