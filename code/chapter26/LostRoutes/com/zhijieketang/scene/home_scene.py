# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter26/LostRoutes/com/zhijieketang/scene/home_scene.py


"""Home场景"""

import logging

import cocos
import cocos.layer
import cocos.menu
import cocos.scenes
import cocos.sprite

from com.zhijieketang.scene import help_scene, gameplay_scene, setting_scene
from com.zhijieketang.utility import tools

# 资源图片路径
RES_PATH = 'resources/image/home/'
logger = logging.getLogger(__name__)


class HomeLayer(cocos.layer.Layer):

    def __init__(self):
        super(HomeLayer, self).__init__()
        logger.info('初始化Home层')

    def on_enter(self):
        """Home层进入方法"""

        super(HomeLayer, self).on_enter()
        logger.info('进入Home层')

        if len(self.get_children()) != 0:  # 判断是否层已经初始化
            return

        # 获得窗口的宽度和高度
        s_width, s_height = cocos.director.director.get_window_size()
        
        # 创建背景精灵
        background = cocos.sprite.Sprite(RES_PATH + 'bg.png')
        background.position = s_width // 2, s_height // 2
        # 添加背景精灵
        self.add(background, 0)


class MainMenu(cocos.menu.Menu):

    def __init__(self):
        super(MainMenu, self).__init__()

        logger.info('初始化MainMenu')

        # 菜单项初始化设置
        self.font_item['font_size'] = 50
        self.font_item['color'] = (180, 200, 255, 255)
        self.font_item_selected['font_size'] = 50
        self.font_item_selected['color'] = (255, 255, 255, 255)

    def on_enter(self):
        """MainMenu层进入方法"""

        super(MainMenu, self).on_enter()

        logger.info('进入MainMenu')

        if len(self.get_children()) != 0:  # 菜单是否已经初始化
            return

        start_item = cocos.menu.ImageMenuItem(RES_PATH + 'button-start.png',
                                              self.on_start_item_callback)
        setting_item = cocos.menu.ImageMenuItem(RES_PATH + 'button-setting.png',
                                                self.on_setting_item_callback)
        help_item = cocos.menu.ImageMenuItem(RES_PATH + 'button-help.png',
                                             self.on_help_item_callback)

        # 获得窗口的宽度和高度
        s_width, s_height = cocos.director.director.get_window_size()
        # 设置窗口居中位置
        x = s_width // 2
        y = s_height // 2 + 50
        step = 55

        self.create_menu([start_item, setting_item, help_item],
                         layout_strategy=cocos.menu.fixedPositionMenuLayout(
                             [(x, y),
                              (x, y - step),
                              (x, y - 2 * step)]))
        # 播放背景音乐
        tools.playmusic('home_bg.ogg')

    def on_start_item_callback(self):
        next_scene = gameplay_scene.create_scene()
        ts = cocos.scenes.FadeTransition(next_scene, 1.0)
        cocos.director.director.push(ts)
        # 播放音效
        tools.playeffect('Blip.wav')

    def on_setting_item_callback(self):
        next_scene = setting_scene.create_scene()
        ts = cocos.scenes.FadeTransition(next_scene, 1.0)
        cocos.director.director.push(ts)
        # 播放音效
        tools.playeffect('Blip.wav')

    def on_help_item_callback(self):
        next_scene = help_scene.create_scene()
        ts = cocos.scenes.FadeTransition(next_scene, 1.0)
        cocos.director.director.push(ts)
        # 播放音效
        tools.playeffect('Blip.wav')


def create_scene():
    """创建Home场景函数"""

    # 创建Home场景
    scene = cocos.scene.Scene(HomeLayer())
    # 添加主菜单
    scene.add(MainMenu())
    return scene
