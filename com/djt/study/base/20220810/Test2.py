import sys

s2 = 'It took me six months to write this Python tutorial. \
Please give me more support. \
I will keep it updated.'
print(s2)

longstr = '''
  It took me 6 months to write this Python tutorial.
  Please give me a to 'thumb' to keep it updated.
  The Python tutorial is available at http://c.biancheng.net/python/.
'''
print(longstr)

print(sys.getdefaultencoding())

print("==================")
print(ord('Q'))
print(chr(81))
print(ord("段"))
print(chr(27573))

print("==================")
name = "张三"
name_bytes = name.encode("GBK")
print(name_bytes)
name_bytes = bytes(name, "GBK")
print(name_bytes.decode("GBK"))
