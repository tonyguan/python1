# coding=utf-8
# 代码文件：chapter13/ch13.4.1-2.py

import logging

logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.ERROR)

logger = logging.getLogger(__name__)

logger.debug('这是DEBUG级别信息。')
logger.info('这是INFO级别信息。')
logger.warning('这是WARNING级别信息。')
logger.error('这是ERROR级别信息。')
logger.critical('这是CRITICAL级别信息。')
