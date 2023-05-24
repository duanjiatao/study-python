# 临时文件/目录

import tempfile

with tempfile.TemporaryFile() as tf:
    print("创建临时文件:", tf.name)
    tf.write("Hello World".encode("utf-8"))
    tf.seek(0)
    print(tf.read().decode('utf-8'))

with tempfile.TemporaryDirectory() as td:
    print('创建临时目录:', td)
