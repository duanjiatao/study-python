list1 = ['1', '2', '3']
print(type(list1))
print(len("123"))
print(len(list1))

for v in list1:
    print(v)

print(range(len(list1)))

list2 = []
print(type(list2))
list2.append("a")
list2.append(3)
list2.append(2)

for v in list2:
    print(v)

print(list2.count('b'))

list3 = [4, 8, 2, 6, 3, 0, 1]
# list3.sort()
list3.reverse()
print(list3)

list4 = list()
list4.append('张')
list4.append('三')
list4.append('李')
list4.append('四')
print(list4)
