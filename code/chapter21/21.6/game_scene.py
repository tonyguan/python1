# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter21/21.6/game_scene.py

from cocos.sprite import *
from cocos.scene import *
from cocos.scenes.transitions import *
from cocos.layer import *
from cocos.menu import *
from cocos.director import *

import setting_scene

# 自定义GameLayer层类
class GameLayer(Layer):

    def __init__(self):
        super(GameLayer, self).__init__()
        # 获得窗口的宽度和高度
        s_width, s_height = director.get_window_size()

        # 创建背景精灵
        background = Sprite('images/game-bg.png')
        background.position = s_width // 2, s_height // 2
        # 添加背景精灵
        self.add(background, 0)


# 自定义主菜单类
class MainMenu(Menu):

    def __init__(self):
        super(MainMenu, self).__init__()
        # 菜单项初始化设置
        self.font_item['font_size'] = 160
        self.font_item['color'] = (255, 255, 255, 255)
        self.font_item_selected['color'] = (230, 230, 230, 255)
        self.font_item_selected['font_size'] = 160

        start_item = ImageMenuItem('images/start-up.png',
                                   self.on_start_item_callback)
        setting_item = ImageMenuItem('images/setting-up.png',
                                     self.on_setting_item_callback)
        help_item = ImageMenuItem('images/help-up.png',
                                  self.on_help_item_callback)

        self.create_menu([start_item, setting_item, help_item],
                         layout_strategy=fixedPositionMenuLayout(
                             [(700, 470), (480, 240), (860, 160)]))

    def on_start_item_callback(self):
        print('on_start_item_callback')

    def on_setting_item_callback(self):
        print('on_setting_item_callback')
        # 直接切换
        # next_scene = setting_scene.create_scene()
        # director.push(next_scene)
        # 切换并有过渡动画
        next_scene = setting_scene.create_scene()
        ts = RotoZoomTransition(next_scene, 1.5) 
        director.push(ts)


    def on_help_item_callback(self):
        print('on_help_item_callback')



if __name__ == '__main__':
    # 初始化导演，设置窗口的高、宽、标题
    director.init(width=1136, height=640, caption='精灵示例')

    # 创建主场景
    main_scene = Scene(GameLayer())
    # GameLayer层
    main_scene.add(MainMenu())

    # 开始启动main_scene场景
    director.run(main_scene)
