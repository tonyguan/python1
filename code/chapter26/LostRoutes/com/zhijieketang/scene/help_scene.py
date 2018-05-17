# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter26/LostRoutes/com/zhijieketang/scene/help_scene.py

"""帮助场景"""
import logging

import cocos.layer
import cocos.scene
import cocos.scenes
import cocos.sprite

from com.zhijieketang.utility import tools

# 资源图片路径
RES_PATH = 'resources/image/help/'
logger = logging.getLogger(__name__)


class HelpLayer(cocos.layer.Layer):

    def __init__(self):
        super(HelpLayer, self).__init__()

        logger.info('初始化帮助层')

        # 获得窗口的宽度和高度
        s_width, s_height = cocos.director.director.get_window_size()
        # 创建背景精灵
        background = cocos.sprite.Sprite(RES_PATH + 'bg.png')
        background.position = s_width // 2, s_height // 2
        # 添加背景精灵到HelloWorld层
        self.add(background, 0)


class MainMenu(cocos.menu.Menu):

    def __init__(self):
        super(MainMenu, self).__init__()

        logger.info('初始化MainMenu')

        # 菜单项初始化设置
        self.font_item['font_size'] = 60
        self.font_item['color'] = (180, 200, 255, 255)
        self.font_item_selected['color'] = (255, 255, 255, 255)
        self.font_item_selected['font_size'] = 60

        ok_item = cocos.menu.ImageMenuItem(RES_PATH + 'button-ok.png',
                                              self.on_item_callback)

        self.create_menu([ok_item],
                         layout_strategy=cocos.menu.fixedPositionMenuLayout(
                             [(210, 50)]))

    def on_item_callback(self):
        cocos.director.director.pop()
        # 播放音效
        tools.playeffect('Blip.wav')


# 创建场景函数
def create_scene():
    # 创建场景
    scene = cocos.scene.Scene(HelpLayer())
    # 添加主菜单
    scene.add(MainMenu())
    return scene
