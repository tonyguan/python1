# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter26/LostRoutes/com/zhijieketang/sprite/fighter_sprite.py

import cocos.sprite

from com.zhijieketang.particle.fighter_fire import FighterFire


class Fighter(cocos.sprite.Sprite):
    def __init__(self):
        super(Fighter, self).__init__(image='resources/image/gameplay/hero.png')

        # 飞机火焰粒子系统
        ps = FighterFire()
        ps.position = 0, - self.height // 2  # 在飞机的下面
        self.add(ps)
        # 当前的生命值
        self.hit_points = 5

    def move(self, delta):

        # 飞机的当前位置
        fx, fy = self.position

        # 获得飞机新的位置
        dx, dy = delta
        fx += dx
        fy += dy

        # 获得飞机宽度和高度的一半
        width_half = self.width // 2
        height_half = self.height // 2

        # 获得窗口的宽度和高度
        s_width, s_height = cocos.director.director.get_window_size()

        # 设置飞机位置不超出屏幕
        if fx < width_half:
            fx = width_half
        elif fx > (s_width - width_half):
            fx = s_width - width_half

        if fy < height_half:
            fy = height_half
        elif fy > (s_height - height_half):
            fy = s_height - height_half

        self.position = fx, fy
