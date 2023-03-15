# 异常处理
import sys
import traceback


def test_exception():
    try:
        a = int(input("输入a:"))
        b = int(input("输入b:"))
        print(f"a/b={a / b}")
    except Exception as e:
        print(str(e))
        print(sys.exc_info())
        print(traceback.print_exc())
    else:
        print("计算完成，未发生异常")
    finally:
        print("执行finally代码块")


test_exception()


# 自定义异常类
class MyException(Exception):
    pass
