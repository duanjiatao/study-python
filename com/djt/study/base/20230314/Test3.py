# 基于类的上下文管理器
class FkResource:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"{self.name}执行__enter__方法")
        return "Enter:" + self.name

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.name}执行__exit__方法")
        if exc_tb is None:
            print(f"{self.name}无异常关闭")
        else:
            print(f"{self.name}有异常关闭")
        return None




if __name__ == "__main__":
    with FkResource("张三") as zs:
        print(zs)

    print("=" * 20)

    with FkResource("李四")  as ls:
        print("发生异常前的代码")
        raise Exception
        print("发生异常后的代码")
