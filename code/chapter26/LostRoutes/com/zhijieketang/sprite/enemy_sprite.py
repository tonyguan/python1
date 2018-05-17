# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter26/LostRoutes/com/zhijieketang/sprite/enemy_sprite.py

"""敌人精灵"""
import enum
import random

import cocos.actions
import cocos.sprite
import pyglet.image

# 资源图片路径
RES_PATH = 'resources/image/gameplay/'


# 定义敌人类型枚举类
class EnemyType(enum.Enum):
    Stone = 1  # 陨石
    Fighter1 = 2  # 敌机1
    Fighter2 = 3  # 敌机2
    Planet = 4  # 行星


# 敌人生命值
EnemyHitPoint = {EnemyType.Stone: 3,
                 EnemyType.Fighter1: 8,
                 EnemyType.Fighter2: 10,
                 EnemyType.Planet: 15}

# 击毁敌人获得分数
EnemyScore = {EnemyType.Stone: 5,
              EnemyType.Fighter1: 10,
              EnemyType.Fighter2: 15,
              EnemyType.Planet: 20}

# 敌人速度
EnemyVelocity = {EnemyType.Stone: -95,
                 EnemyType.Fighter1: -70,
                 EnemyType.Fighter2: -90,
                 EnemyType.Planet: -40}


class Enemy(cocos.sprite.Sprite):

    def __init__(self, type=EnemyType.Fighter1):  # 默认值是Fighter1

        super(Enemy, self).__init__(RES_PATH + 'fighter1.png')

        # 敌人类型
        self.type = type
        # 速度
        self.velocity = EnemyVelocity[EnemyType.Fighter1]
        # 初始的生命值
        self.initial_hit_points = EnemyHitPoint[EnemyType.Fighter1]
        # 当前的生命值
        self.hit_points = self.initial_hit_points

        if type == EnemyType.Stone:
            self.image = pyglet.resource.image(RES_PATH + 'stone.png')
            self.initial_hit_points = EnemyHitPoint[EnemyType.Stone]
            self.velocity = EnemyVelocity[EnemyType.Stone]

        elif type == EnemyType.Planet:
            self.image = pyglet.resource.image(RES_PATH + 'planet.png')
            self.initial_hit_points = EnemyHitPoint[EnemyType.Planet]
            self.velocity = EnemyVelocity[EnemyType.Planet]

        elif type == EnemyType.Fighter2:
            self.image = pyglet.resource.image(RES_PATH + 'fighter2.png')
            self.initial_hit_points = EnemyHitPoint[EnemyType.Fighter2]
            self.velocity = EnemyVelocity[EnemyType.Fighter2]

        # 默认情况下敌人是隐藏的
        self.visible = False
        self.spawn()
        # 开始游戏调度
        self.schedule(self.update)

    def pause_enemy(self):
        # 暂停游戏调度
        self.pause_scheduler()

    def resume_enemy(self):
        # 继续游戏调度
        self.resume_scheduler()

    def update(self, dt):
        """游戏调度"""

        if self.type == EnemyType.Planet:
            # 设置行星旋转
            self.rotation += 1
        posx, posy = self.position
        posy = posy + self.velocity * dt
        self.do(cocos.actions.Place((posx, posy)))

        if posy + self.height // 2 < 0:
            self.spawn()

    def spawn(self):
        """产生敌人精灵"""

        # 获得窗口的宽度和高度
        s_width, s_height = cocos.director.director.get_window_size()

        # 敌人宽度一半
        e_width_half = self.width // 2
        # 敌人高度一半
        e_height_half = self.height // 2

        posy = s_height + e_height_half
        posx = random.randint(e_width_half, s_width - e_width_half)

        # 改变位置
        self.do(cocos.actions.Place((posx, posy)))

        self.hit_points = self.initial_hit_points

        self.visible = True
