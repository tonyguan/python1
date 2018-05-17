# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter21/21.8.4/ch21.8.4.py

from cocos.euclid import Point2
from cocos.sprite import *
from cocos.scene import *
from cocos.layer import *
from cocos.particle_systems import *
from cocos.director import *

# 自定义GameLayer层类
class GameLayer(Layer):

    def __init__(self):
        super(GameLayer, self).__init__()
        # 获得窗口的宽度和高度
        s_width, s_height = director.get_window_size()

        # 创建背景精灵
        background = Sprite('images/zippo.png')
        background.position = s_width // 2, s_height // 2
        # 添加背景精灵
        self.add(background, 0)

        ps = Fire()
        ps.gravity = Point2(45, 500)
        ps.radial_accel = 60
        ps.size = 84
        ps.size_var = 50
        ps.tangential_accel = 20
        ps.tangential_accel_var = 10
        ps.life = 0.79
        ps.life_var = 0.45
        ps.emission_rate = 200
        ps.position = 270, 580

        self.add(ps)


if __name__ == '__main__':
    # 初始化导演，设置窗口的高、宽、标题
    director.init(width=640, height=960, resizable=True, caption='粒子系统示例')

    # 创建主场景，并添加GameLayer对象到主场景
    main_scene = Scene(GameLayer())

    # 开始启动main_scene场景
    director.run(main_scene)
