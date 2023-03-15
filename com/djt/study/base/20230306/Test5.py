# 定义一个实例方法
def say(self):
    print("我要学 Python！", self.name)


# 使用 type() 函数创建类
CLanguage = type("CLanguage", (object,), dict(say=say, name="C 语言中文网"))
# 创建一个 CLanguage 实例对象
clangs = CLanguage()
# 调用 say() 方法和 name 属性
clangs.say()
print(clangs.name)
