from enum import Enum, unique


# 枚举类
@unique  # 该注解可保证枚举的value必须唯一 否则报错
class Color(Enum):
    red = 1
    green = 2
    blue = 3
    yellow = "y"


print(type(Color.red))
print(Color.green)
print(Color(3))
print(Color.yellow.value)

# 遍历所有成员
for name, member in Color.__members__.items():
    print(name, "->", member)

# 创建枚举类
Sex = Enum("Sex", ('male', 'female'))
print(Sex.male)
print(Sex(2))

print("=" * 20)
for s in Sex:
    print(s)
