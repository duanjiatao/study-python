map1 = {1: 'a', 2: 'b', 3: 'c'}
print(f'类型: {type(map1)} 内容: {map1}')

print(map1.get(1))
print(map1.get(5, '默认值'))
print(map1[2])
for k, v in map1.items():
    print(f'{k}:{v}')

print(str(map1))

print(map1.setdefault(1, 'AAA'))
print(map1)
