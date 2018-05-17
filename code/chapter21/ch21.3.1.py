# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter21/20.3.1/ch21.3.1.py

from cocos.menu import *
from cocos.scene import *
from cocos.layer import *


# 自定义主菜单类
class MainMenu(Menu):

    def __init__(self):
        super(MainMenu, self).__init__()

        self.font_item['font_size'] = 32
        self.font_item_selected['font_size'] = 40

        item1 = MenuItem('开始', self.on_item1_callback)
        item2 = ToggleMenuItem('音效', self.on_item2_callback, False)
        
        self.create_menu([item1, item2],
                         selected_effect=shake(),
                         unselected_effect=shake_back())

    def on_item1_callback(self):
        print('调用MenuItem')

    def on_item2_callback(self, value):
        print('调用ToggleMenuItem', value)


if __name__ == "__main__":
    # 初始化导演
    director.init(caption="菜单示例")
    # 创建主菜单
    main_menu = MainMenu()
    # 创建主场景
    main_scene = Scene(main_menu)
    # 开始启动场景
    director.run(main_scene)
