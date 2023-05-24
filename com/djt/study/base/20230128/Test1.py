import numpy as np

my_tuple = ("A", "B", "C")
my_list = [1, 2, 3]
print([x for x in zip(my_tuple, my_list)])

print(list(zip(my_list, my_tuple)))

print(list(reversed(my_list)))

nums = np.random.randint(10, size=10)
print(type(nums))
print("排序前:", list(nums))
print("排序后:", sorted(nums))

a = {6, 2, 4, 9, 0, 1, 3, 7, 5, 8, 6, 6, 6}
print(type(a))
print(a)
