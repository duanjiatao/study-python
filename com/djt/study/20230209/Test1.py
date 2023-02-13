from functools import reduce

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list3 = map(lambda x: x * 2, list1)
print(list(list3))

list4 = map(lambda x, y: x + y, list1, list2)
print(list(list4))

list5 = filter(lambda x: x % 2 == 0, list1)
print(list(list5))

# 这种写法已不支持
# list6 = filter(lambda x, y: (x + y) % 2 == 0, list1, list2)
# print(list(list))

list_c = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
list7 = reduce(lambda x, y: x + y, list_c)
print(list7)


def f(ham: str, egg: str = 'eggs') -> str:
    return ham + "#" + egg


print(f.__annotations__)
print(f("A"))
