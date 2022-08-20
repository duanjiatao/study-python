import copy

list1 = [1, 2, 3]
list2 = copy.copy(list1)
print("list1=", list1)
print("list2=", list2)

s = "http://c.biancheng.net/shell/"
s_str = str(s)
s_repr = repr(s)
print(type(s_str))
print(s_str)
print(type(s_repr))
print(s_repr)

str1 = "人生苦短，我用 Python"
print(len(str1))
print(len(str1.encode('gbk')))
print(len(str1.encode('utf-8')))
print(len(str1.encode('gb2312')))

str2 = "C 语言中文网 >>>\n### c.biancheng.net"
print(str2)
print(str2.split())

S = 'http://c.biancheng.net/python/'
print(S.ljust(35, '#'))

print(dir(S))
print(help(S.lower))
