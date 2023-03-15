# while 与 for 循环
ss = "123456"
aa = 123
print(type(ss))
print(type(aa))
print("#" * 100)
num = 0
while num <= 10:
    print(num)
    num += 1

print("#" * 100)
i = 0
while i < len(ss):
    print(ss[i])
    i += 1

print("#" * 100)
for c in ss:
    print(c, end="")
else:
    print()

print("#" * 100)
ret = 0
for x in range(101):
    ret += x
else:
    print()

print("#" * 100)
my_list = [1, 2, 3, 4, 5, 6]
for x in my_list:
    print(x, end="")
else:
    print()

print("#" * 100)
my_dict = {"a": 1, "b": 2, "c": 3}
for x in my_dict:
    print(x)
for x in my_dict.items():
    print(x)
