"""
测试loguru
"""

from loguru import logger

# 按天滚动 保留近3天日志文件 滚动文件压缩成zip格式
logger.add('./logs/runtime.log', rotation='00:00', retention=3, compression='zip', backtrace=True)


def nested(c):
    try:
        return 5 / c
    except ZeroDivisionError:
        logger.exception("计算错误!")


if __name__ == '__main__':
    logger.debug('hello word!')
    logger.info('hello word!')
    logger.warning('hello word!')
    logger.error('hello word!')
    nested(0)
