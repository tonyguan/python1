# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter26/LostRoutes/com/zhijieketang/scene/loading_scene.py
#

"""Loading场景"""
import logging
import threading
import time

import cocos.layer
import cocos.scene
import cocos.scenes
import cocos.sprite
import pyglet.image

from com.zhijieketang.scene import home_scene

# 资源图片路径
RES_PATH = 'resources/image/loading/'
logger = logging.getLogger(__name__)


class LoadingLayer(cocos.layer.Layer):

    def __init__(self):
        super(LoadingLayer, self).__init__()

        logger.info("启动Loading场景")

        # 获得窗口的宽度和高度
        s_width, s_height = cocos.director.director.get_window_size()

        # 创建背景精灵
        background = cocos.sprite.Sprite(RES_PATH + 'bg.png')
        background.position = s_width // 2, s_height // 2
        # 添加背景精灵
        self.add(background, 0)

        # 动画帧序列
        frames = [pyglet.resource.image(RES_PATH + 'loading1.png'),
                  pyglet.resource.image(RES_PATH + 'loading2.png'),
                  pyglet.resource.image(RES_PATH + 'loading3.png'),
                  pyglet.resource.image(RES_PATH + 'loading4.png')]
        # 创建动画图片对象
        animimage = pyglet.image.Animation.from_image_sequence(frames, 0.3, True)
        # 创建动画精灵对象
        loading = cocos.sprite.Sprite(animimage)

        # 设置窗口居中位置
        loading.position = s_width // 2, s_height // 2 - 60

        self.add(loading, 0)

        # 创建一个子线程加载资源
        loadingthread = threading.Thread(target=self.thread_body)
        # 启动线程
        loadingthread.start()

    def thread_body(self):
        """线程体函数"""

        logger.info("资源加载中...")
        time.sleep(3)  # 模拟资源加载
        logger.info("资源加载结束。")

        # 场景切换
        next_scene = home_scene.create_scene()
        ts = cocos.scenes.FadeTransition(next_scene, 1.0)
        cocos.director.director.push(ts)


def create_scene():
    """创建Loading场景函数"""

    # 创建Loading场景
    scene = cocos.scene.Scene(LoadingLayer())
    return scene
