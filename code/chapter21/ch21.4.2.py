# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter21/ch21.4.2.py

import cocos
import pyglet


# 自定义HelloWorld层类
class HelloWorld(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(HelloWorld, self).__init__()
        # 创建标签
        self.label = cocos.text.Label('Hello, World!',
                                      font_name='Times New Roman',
                                      font_size=32,
                                      anchor_x='center', anchor_y='center')

        # 获得窗口的宽度和高度
        width, height = cocos.director.director.get_window_size()
        # 设置标签的位置
        self.label.position = width // 2, height // 2

        # 添加标签到HelloWorld层
        self.add(self.label)

    def on_mouse_press(self, x, y, button, modifiers):
        print('on_mouse_press', button, modifiers)
        if button == pyglet.window.mouse.LEFT:
            self.label.element.text = '鼠标左键按下'

    def on_mouse_release(self, x, y, button, modifiers):
        print('on_mouse_release', button, modifiers)
        if button == pyglet.window.mouse.LEFT:
            self.label.element.text = '鼠标左键释放'

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        print('on_mouse_drag', buttons, modifiers)
        print(x, y, dx, dy)
        if modifiers & pyglet.window.key.MOD_CTRL:
            self.label.element.text = 'Ctrl键+鼠标拖曳中...'


if __name__ == "__main__":
    # 初始化导演，设置窗口的高、宽、标题
    cocos.director.director.init(width=640, height=480, caption="键盘事件")

    # 创建HelloWorld层实例
    hello_layer = HelloWorld()

    # 创建一个场景，并将HelloWorld层实例添加到场景中
    main_scene = cocos.scene.Scene(hello_layer)

    # 开始启动main_scene场景
    cocos.director.director.run(main_scene)
