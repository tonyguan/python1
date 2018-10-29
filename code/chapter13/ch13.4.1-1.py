# coding=utf-8
# 代码文件：chapter13/ch13.4.1-1.py

import logging

logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.ERROR)

logging.debug('这是DEBUG级别信息。')
logging.info('这是INFO级别信息。')
logging.warning('这是WARNING级别信息。')
logging.error('这是ERROR级别信息。')
logging.critical('这是CRITICAL级别信息。')
