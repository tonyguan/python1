# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter21/21.7/ch21.7.2.py

from cocos.sprite import *
from cocos.scene import *
from cocos.actions import *
from cocos.layer import *
from cocos.menu import *
from cocos.layer.util_layers import ColorLayer

# 定义全局变量hero
hero = None


# 自定义GameLayer层类
class GameLayer(ColorLayer):

    def __init__(self):
        super(GameLayer, self).__init__(255, 255, 255, 255)
        # 声明全局变量hero
        global hero
        # 创建hero精灵
        hero = Sprite('images/hero.png')
        hero.position = 560, 320
        self.add(hero)


# 自定义主菜单类
class MainMenu(Menu):

    def __init__(self):
        super(MainMenu, self).__init__()
        # 菜单项初始化设置
        self.font_item['font_size'] = 20
        self.font_item['color'] = (0, 0, 0, 255)
        self.font_item_selected['color'] = (0, 0, 0, 255)
        self.font_item_selected['font_size'] = 26

        item1 = MenuItem('MoveBy', self.on_callback1)
        item2 = MenuItem('MoveTo', self.on_callback2)
        item3 = MenuItem('JumpBy', self.on_callback3)
        item4 = MenuItem('JumpTo', self.on_callback4)
        item5 = MenuItem('ScaleBy', self.on_callback5)
        item6 = MenuItem('ScaleTo', self.on_callback6)
        item7 = MenuItem('RotateBy', self.on_callback7)
        item8 = MenuItem('RotateTo', self.on_callback8)
        item9 = MenuItem('FadeTo', self.on_callback9)
        item10 = MenuItem('FadeIn', self.on_callback10)
        item11 = MenuItem('FadeOut', self.on_callback11)

        x = 120
        y = 560
        step = 45

        self.create_menu(
            [item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11],
            layout_strategy=fixedPositionMenuLayout(
                [(x, y), (x, y - step), (x, y - 2 * step), (x, y - 3 * step), (x, y - 4 * step),
                 (x, y - 5 * step), (x, y - 6 * step), (x, y - 7 * step), (x, y - 8 * step),
                 (x, y - 9 * step), (x, y - 10 * step)]))

    def on_callback1(self): # MoveBy
        hero.do(MoveBy((100, 100), duration=2))

    def on_callback2(self): # MoveTo
        hero.do(MoveTo((560, 320), duration=2))

    def on_callback3(self): # JumpBy
        action = JumpBy((200, 200), height=30, jumps=5, duration=2)
        hero.do(action)

    def on_callback4(self): # JumpTo
        action = JumpTo((850, 450), height=30, jumps=5, duration=2)
        hero.do(action)

    def on_callback5(self): # ScaleBy
        action = ScaleBy(0.5, duration=2)
        hero.do(action)

    def on_callback6(self): # ScaleTo
        action = ScaleTo(2, duration=2)
        hero.do(action)

    def on_callback7(self): # RotateBy
        action = RotateBy(-180, duration=2)
        hero.do(action)

    def on_callback8(self): # RotateTo
        action = RotateTo(180, duration=2)
        hero.do(action)

    def on_callback9(self): # FadeTo
        hero.do(FadeTo(80, 2))

    def on_callback10(self): # FadeIn
        hero.do(FadeIn(3))

    def on_callback11(self): # FadeOut
        hero.do(FadeOut(3))


if __name__ == '__main__':
    # 初始化导演，设置窗口的高、宽、标题
    director.init(width=1136, height=640, caption='间隔动作示例')

    # 创建主场景，并添加GameLayer到场景
    main_scene = Scene(GameLayer())
    # 添加主菜单到场景
    main_scene.add(MainMenu())

    # 开始启动main_scene场景
    director.run(main_scene)
