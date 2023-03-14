# 日志模块

import logging

# 禁用日志
# logging.disable(logging.CRITICAL)

# 基本配置 输出到文件需配置 filename="./ppp.txt",
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


def func():
    for i in range(10):
        logging.info(i)


func()

logging.disable(logging.DEBUG)
logging.info("6666666666666")
