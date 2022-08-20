# 范围在 [-5, 256] 之间的小整数
int1 = -5
int2 = -5
print("[-5, 256] 情况下的两个变量：", id(int1), id(int2))
# bool 类型
bool1 = True
bool2 = True
print("bool 类型情况下的两个变量：", id(bool1), id(bool2))
# 对于字符串
s1 = "3344"
s2 = "3344"
print("字符串情况下的两个交量", id(s1), id(s2))
# 大于 256 的整数
int3 = 257
int4 = 257
print("大于 256 的整数情况下的两个变量", id(int3), id(int4))
# 大于 0 的浮点数
f1 = 256.4
f2 = 256.4
print("大于 0 的浮点数情况下的两个变量", id(f1), id(f2))
# 小于 0 的浮点数
f3 = -2.45
f4 = -2.45
print("小于 0 的浮点数情况下的两个变量", id(f3), id(f4))
# 小于 -5 的整数
n1 = -6
n2 = -6
print("小于 -5 的整数情况下的两个变量", id(n1), id(n2))

print("===========================")


def fun():
    # [-5,256]
    int1 = -5
    print("fun 中 -5 的存储状态", id(int1), id(int2))
    # bool 类型
    bool3 = True
    print("fun 中 bool 类型的存储状态", id(bool3), id(bool2))
    # 字符串类型
    s1 = "3344"
    print("fun 中 3344 字符串的存储状态", id(s1), id(s2))
    # 大于 256
    int3 = 257
    print("fun 中 257 的存储状态", id(int3), id(int4))
    # 浮点类型
    f1 = 256.4
    print("fun 中 256.4 的存储状态", id(f1), id(f2))
    # 小于 -5
    n1 = -6
    print("fun 中 -6 的存储状态", id(n1), id(n2))


fun()
