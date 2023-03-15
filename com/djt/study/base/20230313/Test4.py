import string as ss

for x in dir(ss):
    print(x)

print("=" * 20)
for x in ss.__all__:
    print(x)

# print("=" * 20)
# for x in dir(ss):
#     print("-" * 30)
#     print(help(x))


print("=" * 20)
print(ss.__file__)

# Python 中目前有哪些模块（包括标准模块和第三方模块） 相当于 pip list
help('modules')
