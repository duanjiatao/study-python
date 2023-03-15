# 文件操作
file = open("C:\\Users\\duanjiatao\\Desktop\\test.txt", encoding="utf-8", buffering=10240)
print(file)
print(file.name)
print(file.encoding)

print("=" * 20)
print(file.read(4))
# 将文件指针移动至开头
file.seek(0)

print("=" * 20)
# 读取一行 可指定字符(字节)数
print(file.readline(2))
file.seek(0)

print("=" * 20)
# 读取所有行
print(file.readlines())
file.seek(0)

file.close()

print("=" * 20)
file2 = open("C:\\Users\\duanjiatao\\Desktop\\test2.txt", mode="w", encoding="utf-8", buffering=10240)
# file2.write("写入一行数据")
file2.writelines(["张三", "李四"])
file2.flush()

file2.close()

with open("C:\\Users\\duanjiatao\\Desktop\\test3.txt", mode="w", encoding="utf-8", buffering=10240) as file3:
    file3.writelines(["666", "777"])
