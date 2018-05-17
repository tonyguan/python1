# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter21/21.7/ch21.7.1.py

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

        item1 = MenuItem('Hide', self.on_callback1)
        item2 = MenuItem('Show', self.on_callback2)
        item3 = MenuItem('ToggleVisibility', self.on_callback3)
        item4 = MenuItem('Place', self.on_callback4)

        x = 120
        y = 560
        step = 50

        self.create_menu([item1, item2, item3, item4],
                         layout_strategy=fixedPositionMenuLayout(
                             [(x, y), (x, y - step),
                              (x, y - 2 * step),
                              (x, y - 3 * step)]))

    def on_callback1(self):
        hero.do(Hide())

    def on_callback2(self):
        hero.do(Show())

    def on_callback3(self):
        hero.do(ToggleVisibility())

    def on_callback4(self):
        hero.do(Place((800, 500)))

if __name__ == '__main__':
    # 初始化导演，设置窗口的高、宽、标题
    director.init(width=1136, height=640, caption='瞬时动作示例')

    # 创建主场景，并添加GameLayer到场景
    main_scene = Scene(GameLayer())
    # 添加主菜单到场景
    main_scene.add(MainMenu())

    # 开始启动main_scene场景
    director.run(main_scene)
