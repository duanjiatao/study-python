"""
这是第一个自定义模块
"""

name = "呲呲"
add = "www.fscici.xyz"
print(f"name={name} add={add}")


def say():
    print("这是模块中的say方法")


class CLanguage:
    def __init__(self, name, add):
        self.name = name
        self.add = add

    def say(self):
        print(self.name, self.add)


if __name__ == "__main__":
    say()
    c = CLanguage("百度", "www.baidu.com")
    c.say()

# 当使用 from xxx import * 导入模块时，限定可被导入的成员
__all__ = ["add", "say", "CLanguage"]
