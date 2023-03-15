# 基于生成器的上下文管理器

from contextlib import contextmanager


@contextmanager
def file_manager(name, mode):
    try:
        f = open(name, mode)
        yield f
        print("执行yield之后的代码")
    finally:
        f.close()


if __name__ == "__main__":
    with file_manager("C:\\Users\\duanjiatao\\Desktop\\test4.txt", "w") as f:
        f.write("hello world")
