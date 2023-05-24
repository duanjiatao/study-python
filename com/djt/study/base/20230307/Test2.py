# 通过迭代器实现字符串逆序输出
class Reverse:

    def __init__(self, content):
        self.__content = content
        self.__index = len(content)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index == 0:
            raise StopIteration
        self.__index -= 1
        return self.__content[self.__index]


string = Reverse("abcdefg")
for c in string:
    print(c, end=" ")
