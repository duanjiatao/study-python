# 1. 导入 AndroidBotMain 类
from AiBot import AndroidBotMain


# 2. 自定义一个脚本类，继承 AndroidBotMain
class CustomAndroidScript(AndroidBotMain):
    # 3. 设置等待参数
    # 3.1 设置等待时间
    wait_timeout = 3
    # 3.2 设置重试间隔时长
    interval_timeout = 0.5

    # 4. 设置日志等级
    log_level = "INFO"  # "DEBUG"

    # 5. 设置方法超时是否抛出异常
    raise_err = False  # True

    # 6. 重写方法，编写脚本
    # 注意：此方法是脚本执行入口
    def script_main(self):
        # 6.1 API 演示
        # 注意：Python 版本支持的 Api 与 Nodejs 基本相同
        # 教程中仅演示部分 Api，更多 Api 请自行探索，所有 Api 均包含详细的参数要求和返回值，请自行查看。

        # 截图
        # self.save_screenshot("xxx.png")
        # 获取坐标点颜色
        # self.get_color((100, 100))
        # 查找图片
        # p = self.find_image("xxx.png")
        # 点击坐标
        # self.click((100, 100))
        # self.click(p)
        # 滑动
        # self.swipe((100, 100), (200, 200), 3)
        print("启动微信")
        self.start_app("com.tencent.mm")


# 7. 执行脚本，Pycharm 中，直接右键执行
if __name__ == '__main__':
    # 注意：此处监听的端口号，必须和手机端的脚本端口号一致；
    # 监听 16678 号端口
    CustomAndroidScript.execute(16678)
