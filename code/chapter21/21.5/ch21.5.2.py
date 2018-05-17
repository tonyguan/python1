# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter21/21.5/ch21.5.2.py

from cocos.sprite import *
from cocos.scene import *
from cocos.layer import *


# 自定义HelloWorld层类
class HelloWorld(Layer):

    def __init__(self):
        super(HelloWorld, self).__init__()

        # 获得窗口的宽度和高度
        self.s_width, self.s_height = director.get_window_size()

        # 创建背景精灵
        background = Sprite('images/background.png')
        background.position = self.s_width // 2, self.s_height // 2
        # 添加背景精灵到HelloWorld层
        self.add(background, -1)

        # 创建山1精灵
        mountain1 = Sprite('images/mountain1.png', position=(360, 500), scale=0.6)
        # 添加山1精灵到层
        self.add(mountain1, 1)

        # 创建山2树精灵
        mountain2 = Sprite('images/mountain2.png', position=(800, 500), scale=0.6)
        # 添加山2精灵到层
        self.add(mountain2, 1)

        # 创建树精灵
        tree = Sprite('images/tree.png', position=(360, 260), scale=0.6)
        # 添加树精灵到层
        self.add(tree, 1)

        # 创建英雄精灵
        hero = Sprite('images/hero.png', position=(800, 160), scale=0.6)
        # 添加英雄精灵到层
        self.add(hero, 1)


if __name__ == '__main__':
    # 初始化导演，设置窗口的高、宽、标题
    director.init(width=1136, height=640, caption='精灵示例')

    # 创建HelloWorld层实例
    hello_layer = HelloWorld()

    # 创建一个场景，并将HelloWorld层实例添加到场景中
    main_scene = Scene(hello_layer)

    # 开始启动main_scene场景
    director.run(main_scene)
