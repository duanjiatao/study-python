import os

print("当前工作目录为:", os.getcwd())

path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(path))
print(os.path.dirname(path))
