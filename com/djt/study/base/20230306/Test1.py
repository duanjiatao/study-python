class Rect:

    def __init__(self, area):
        self.__area = area

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        self.__area = value

    @area.deleter
    def area(self):
        self.__area = 0

    def __display(self):
        print(f"area={self.__area}")


r1 = Rect(10)
print(r1.area)
r1.area = 20
print(r1.area)
del r1.area
print(r1.area)

# 手动调用私有属性与方法
# print(r1._Rect__area)
# r1._Rect__display()
