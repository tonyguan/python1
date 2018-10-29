# coding=utf-8
# 代码文件：chapter13/ch13.4.3.py

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(threadName)s - '
                           '%(name)s - %(funcName)s - %(levelname)s - %(message)s',
                    filename='test.log')

logger = logging.getLogger(__name__)


logger.debug('这是DEBUG级别信息。')
logger.info('这是INFO级别信息。')
logger.warning('这是WARNING级别信息。')
logger.error('这是ERROR级别信息。')
logger.critical('这是CRITICAL级别信息。')

def funlog():
    logger.info('进入funlog函数。')

logger.info('调用funlog函数。')
funlog()