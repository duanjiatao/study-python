from datetime import datetime

name = "Python"
print("hello {0} 今天是: {1}".format(name, datetime.now()))
print(f"hello {name} 今天是: {datetime.now()}")
print(datetime.now().strftime("YYYY-MM-DD HH:MM:SS"))

n1 = 3.1415926
n2 = 0.31415
print(n1)
print(f"{n1:.2f}")
print(f"{n2:.2%}")

n3 = 21
print('左边补零：{:0>4}'.format(n3))
print('右边补x：{:x<5}'.format(n3))

print("123".isdigit())
print("abc".isalpha())
print("abc123".isalnum())

s1 = 'lemon'
print(isinstance(s1, str))
# 判断是否是指定类型中的某一中
print(isinstance(s1, (str, int)))
print(isinstance(666, (str, int)))

print('#'.join(['A', 'B', 'C']))
print(str.join('@', ['A', 'B', 'C']))
