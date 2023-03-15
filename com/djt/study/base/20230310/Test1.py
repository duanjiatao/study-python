# 装饰器用于输出函数执行时间
import functools
import time


def log_exec_time(func):
    """
    打印函数执行时间
    :param func:待执行函数
    :return:返回值
    """

    @functools.wraps(func)
    def warpper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {(end - start) * 1000} ms")
        return res

    return warpper


@log_exec_time
def hello():
    time.sleep(3)
    print("Hello World")


hello()

