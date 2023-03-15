dic = {'a': "A"}
print(dic.keys())
exec("b = \"B\"", dic)
print(dic.keys())

a = 10
b = 20
c = 30
g = {'a': 6, 'b': 8}
t = {'b': 100, 'c': 10}
print(eval("a+b+c", g, t))
