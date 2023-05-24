list1 = [x + 1 for x in range(0, 10)]
print(list1)

list2 = [x + y for x in range(5) for y in range(10, 13)]
print(f'长度:{len(list2)} 列表: {list2}')

list3 = [x if x % 2 == 0 else x + 1 for x in range(10)]
print(list3)

list4 = [x for x in range(10) if x % 2 == 0 if x % 3 == 0]
print(list4)
