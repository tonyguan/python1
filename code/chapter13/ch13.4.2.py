# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter13/ch13.4.2.py

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(threadName)s - '
                           '%(name)s - %(funcName)s - %(levelname)s - %(message)s')

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