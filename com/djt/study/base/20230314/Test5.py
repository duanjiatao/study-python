# pickle模块 对象序列化与反序列化 持久化存储
import pickle as pk

tup1 = ("Hello World", {1, 2, 3}, None)
p1 = pk.dumps(tup1)
print(p1)

t2 = pk.loads(p1)
print(t2)

fileName = "C:\\Users\\duanjiatao\\Desktop\\test5.txt"
with open(fileName, "wb") as f1:
    pk.dump(t2, f1)

with open(fileName, "rb") as f2:
    t3 = pk.load(f2)
    print(t3)
