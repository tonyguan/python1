# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter21/21.9/setting_scene.py

from cocos.sprite import *
from cocos.scene import *
from cocos.layer import *
from cocos.menu import *
from cocos.director import *

from cocos.audio.effect import Effect

# 自定义SettingLayer层类
class SettingLayer(Layer):

    def __init__(self):
        super(SettingLayer, self).__init__()
        # 获得窗口的宽度和高度
        s_width, s_height = director.get_window_size()

        # 创建背景精灵
        background = Sprite('images/setting-bg.png')
        background.position = s_width // 2, s_height // 2
        # 加背景精灵
        self.add(background, 0)

        on = Sprite('images/on.png', position=(818, 280))
        self.add(on, 0)
        on = Sprite('images/on.png', position=(818, 420))
        self.add(on, 0)


# 自定义主菜单类
class MainMenu(Menu):

    def __init__(self):
        super(MainMenu, self).__init__()
        # 菜单项初始化设置
        self.font_item['font_size'] = 160
        self.font_item['color'] = (255, 255, 255, 255)
        self.font_item_selected['color'] = (230, 230, 230, 255)
        self.font_item_selected['font_size'] = 160

        ok_item = ImageMenuItem('images/ok-up.png',
                                self.on_ok_item_callback)

        self.create_menu([ok_item],
                         layout_strategy=fixedPositionMenuLayout(
                             [(560, 130)]))

    def on_ok_item_callback(self):
        effect = Effect('sound/Blip.wav')
        effect.play()
        director.pop()

# 创建场景函数
def create_scene():
    # 创建场景
    scene = Scene(SettingLayer())
    # 添加主菜单
    scene.add(MainMenu())
    return scene
