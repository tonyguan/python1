# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter26/LostRoutes/game_main.py

import logging

import cocos

from com.zhijieketang.scene.loading_scene import create_scene

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(threadName)s - '
                           '%(name)s - %(funcName)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    # 初始化导演，设置窗口的高、宽、标题
    cocos.director.director.init(width=320, height=480, caption='迷失航线', audio_backend='sdl')

    # 创建主场景
    main_scene = cocos.scene.Scene(create_scene())

    logger.info("开始启动main_scene场景")

    # cocos.director.director.show_FPS = True

    # 开始启动main_scene场景
    cocos.director.director.run(main_scene)
