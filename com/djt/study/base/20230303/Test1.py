# 描述符类
class Score:

    def __int__(self):
        self.__score = 0

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Score must be integer")
        if not 0 <= value <= 100:
            raise ValueError("Valid value must be in [0, 100]")
        self.__score = value

    def __get__(self, instance, owner):
        return self.__score

    def __delete__(self, instance):
        del self.__score


# 普通类
class Student:
    math = Score()
    chinese = Score()
    english = Score()

    def __init__(self, name, math, chinese, english):
        self.name = name
        self.math = math
        self.chinese = chinese
        self.english = english
        self.__age = 18

    def __repr__(self):
        return "<Student: {}, math:{}, chinese: {}, english:{}>".format(
            self.name, self.math, self.chinese, self.english)


xiao_ming = Student("小明", 76, 87, 80)
print(xiao_ming)
xiao_ming.name = "小王"
print(xiao_ming)
