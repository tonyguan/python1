# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter26/LostRoutes/com/zhijieketang/scene/setting_scene.py

"""设置场景"""
import configparser
import logging

import cocos
import cocos.layer
import cocos.scene
import cocos.scenes
import cocos.sprite
import pyglet

from com.zhijieketang.utility import tools

# 资源图片路径
RES_PATH = 'resources/image/setting/'
logger = logging.getLogger(__name__)


class SettingLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(SettingLayer, self).__init__()

        logger.info('初始化设置层')

        # 获得窗口的宽度和高度
        s_width, s_height = cocos.director.director.get_window_size()

        # 创建背景精灵
        background = cocos.sprite.Sprite(RES_PATH + 'bg.png')
        background.position = s_width // 2, s_height // 2
        # 添加背景精灵到HelloWorld层
        self.add(background, 0)

        # 读取配置信息
        self.config = configparser.ConfigParser()
        self.config.read('config.ini', encoding='utf-8')
        # 读取音效状态
        self.soundstatus = self.config.getint('setting', 'sound_status')
        # 读取背景音乐状态
        self.musicstatus = self.config.getint('setting', 'music_status')

        self.check_on_image = pyglet.resource.image(RES_PATH + 'check-on.png')
        self.check_off_image = pyglet.resource.image(RES_PATH + 'check-off.png')

        if self.soundstatus == 0:
            # 音效未开启
            self.soundchk = cocos.sprite.Sprite(self.check_off_image)
        else:
            # 音效开启
            self.soundchk = cocos.sprite.Sprite(self.check_on_image)
        self.soundchk.position = 210, 328
        self.add(self.soundchk, 0)

        if self.musicstatus == 0:
            # 背景音乐未开启
            self.musicchk = cocos.sprite.Sprite(self.check_off_image)
        else:
            # 背景音乐开启
            self.musicchk = cocos.sprite.Sprite(self.check_on_image)
        self.musicchk.position = 210, 270
        self.add(self.musicchk, 0)

    def on_mouse_release(self, x, y, button, modifiers):
        if button == pyglet.window.mouse.LEFT:
            # 音效复选框精灵矩形轮廓
            soundchkrect = self.soundchk.get_rect()
            # 背景音乐复选框精灵矩形轮廓
            musicchkrect = self.musicchk.get_rect()

            # 单击音效复选框精灵
            if soundchkrect.contains(x, y):
                logger.debug('单击音效复选框精灵')
                if self.soundstatus == 0:
                    # 开启音效处理
                    self.soundchk.image = self.check_on_image
                    self.soundstatus = 1
                else:
                    # 关闭音效处理
                    self.soundchk.image = self.check_off_image
                    self.soundstatus = 0
                # 写入音效状态
                self.config['setting']['sound_status'] = str(self.soundstatus)
                with open('config.ini', 'w') as fw:
                    self.config.write(fw)

            # 单击背景音乐复选框精灵
            if musicchkrect.contains(x, y):
                logger.debug('单击音乐复选框精灵')
                if self.musicstatus == 0:
                    # 开启背景音乐处理
                    self.musicchk.image = self.check_on_image
                    self.musicstatus = 1
                else:
                    # 关闭背景音乐处理
                    self.musicchk.image = self.check_off_image
                    self.musicstatus = 0
                # 播放或停止背景音乐
                tools.playmusic('home_bg.ogg', self.musicstatus)
                # 写入背景音乐状态
                self.config['setting']['music_status'] = str(self.musicstatus)
                with open('config.ini', 'w') as fw:
                    self.config.write(fw)


class MainMenu(cocos.menu.Menu):

    def __init__(self):
        super(MainMenu, self).__init__()

        logger.info('初始化MainMenu')

        # 菜单项初始化设置
        self.font_item['font_size'] = 60
        self.font_item['color'] = (180, 200, 255, 255)
        self.font_item_selected['font_size'] = 60        
        self.font_item_selected['color'] = (255, 255, 255, 255)

        ok_item = cocos.menu.ImageMenuItem(RES_PATH + 'button-ok.png',
                                              self.on_item_callback)

        self.create_menu([ok_item],
                         layout_strategy=cocos.menu.fixedPositionMenuLayout(
                             [(210, 50)]))

    def on_item_callback(self):
        cocos.director.director.pop()
        # 播放音效
        tools.playeffect('Blip.wav')

def create_scene():
    """创建设置场景函数"""

    # 创建设置场景
    scene = cocos.scene.Scene(SettingLayer())
    # 添加主菜单
    scene.add(MainMenu())

    return scene
