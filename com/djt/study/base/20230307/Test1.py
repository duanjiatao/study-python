# 自定义序列类 重载部分运算符
class MyDict:
    def __init__(self):
        self.__dict = {}

    def __len__(self):
        return self.__dict.__len__()

    def __getitem__(self, key):
        if key in self.__dict.keys():
            return self.__dict[key]

        return None

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise TypeError("value must be int")
        self.__dict[key] = value

    def __delitem__(self, key):
        if key in self.__dict.keys():
            del self.__dict[key]


dic = MyDict()
dic["a"] = 1
dic["b"] = 2
print(len(dic))

dic["c"] = 3
print(dic["c"])

# print("=" * 20)
# dd = {"a": 1, "b": 2, "c": 3}
# for k, v in dd.items():
#     print(f"{k} = {v}")

print("=" * 20)
del dic["a"]
print(dic["a"])
