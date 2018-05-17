# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter21/ch21.8.3.py

from cocos.scene import *
from cocos.layer import *
from cocos.menu import *
from cocos.particle_systems import *

# 定义全局变量game_layer
game_layer = None


# 自定义GameLayer层类
class GameLayer(Layer):

    def __init__(self):
        super(GameLayer, self).__init__()
        # 创建初始的粒子系统
        sp = Spiral()
        sp.position = 560, 320
        self.add(sp, name='particle')


# 自定义主菜单类
class MainMenu(Menu):

    def __init__(self):
        super(MainMenu, self).__init__()
        # 菜单项初始化设置
        self.font_item['font_size'] = 20
        self.font_item_selected['font_size'] = 26

        item1 = MenuItem('Fireworks', self.on_callback1)
        item2 = MenuItem('Spiral', self.on_callback2)
        item3 = MenuItem('Meteor', self.on_callback3)
        item4 = MenuItem('Sun', self.on_callback4)
        item5 = MenuItem('Fire', self.on_callback5)
        item6 = MenuItem('Galaxy', self.on_callback6)
        item7 = MenuItem('Flower', self.on_callback7)
        item8 = MenuItem('Explosion', self.on_callback8)
        item9 = MenuItem('Smoke', self.on_callback9)

        x = 120
        y = 560
        step = 45

        self.create_menu(
            [item1, item2, item3, item4, item5, item6, item7, item8, item9],
            layout_strategy=fixedPositionMenuLayout(
                [(x, y), (x, y - step), (x, y - 2 * step), (x, y - 3 * step), (x, y - 4 * step),
                 (x, y - 5 * step), (x, y - 6 * step), (x, y - 7 * step), (x, y - 8 * step)]))

    def on_callback1(self):  # Fireworks
        # 通过节点名，从层中删除节点
        game_layer.remove('particle')
        sp = Fireworks()
        sp.position = 560, 320
        game_layer.add(sp, name='particle')

    def on_callback2(self):  # Spiral
        game_layer.remove('particle')
        sp = Spiral()
        sp.position = 560, 320
        game_layer.add(sp, name='particle')

    def on_callback3(self):  # Meteor
        game_layer.remove('particle')
        sp = Meteor()
        sp.position = 560, 320
        game_layer.add(sp, name='particle')

    def on_callback4(self):  # Sun
        game_layer.remove('particle')
        sp = Sun()
        sp.position = 560, 320
        game_layer.add(sp, name='particle')

    def on_callback5(self):  # Fire
        game_layer.remove('particle')
        sp = Fire()
        sp.position = 560, 320
        game_layer.add(sp, name='particle')

    def on_callback6(self):  # Galaxy
        game_layer.remove('particle')
        sp = Galaxy()
        sp.position = 560, 320
        game_layer.add(sp, name='particle')

    def on_callback7(self):  # Flower
        game_layer.remove('particle')
        sp = Flower()
        sp.position = 560, 320
        game_layer.add(sp, name='particle')

    def on_callback8(self):  # Explosion
        game_layer.remove('particle')
        sp = Explosion()
        sp.position = 560, 320
        game_layer.add(sp, name='particle')

    def on_callback9(self):  # Smoke
        game_layer.remove('particle')
        sp = Smoke()
        sp.position = 560, 320
        game_layer.add(sp, name='particle')


if __name__ == '__main__':
    # 初始化导演，设置窗口的高、宽、标题
    director.init(width=1136, height=640, caption='组合动作示例')

    game_layer = GameLayer()
    # 创建主场景，并添加GameLayer到场景
    main_scene = Scene(game_layer)
    # 添加主菜单到场景
    main_scene.add(MainMenu())

    # 开始启动main_scene场景
    director.run(main_scene)
