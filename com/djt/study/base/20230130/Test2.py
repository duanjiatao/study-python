# 可变参数 b相当于元组 c相当于字典
def func1(a, *b, **c):
    print("a=", a)
    print("b=", b)
    print("c=", c)


func1("abc")
print("=" * 50)
func1("abc", "def", "saaa")
print("=" * 50)
func1("张三", "李四", "王五", "赵六", houqi="侯七", maba="马八", zhoujiu="周九")

print("=" * 100)


def func2(a, b, c):
    print("a=", a)
    print("b=", b)
    print("c=", c)


p1 = ["a", "b", "c"]
func2(*p1)
print("=" * 50)
p2 = {"a": "a", "b": "b", "c": "c"}
func2(**p2)

print("=" * 100)


def func3(a, *b):
    print("a=", a)
    print("b=", b)


p3 = ["q", "w", "e"]
func3(*p3)
print("=" * 50)
func3("666", *p3)
