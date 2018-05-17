# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter26/LostRoutes/com/zhijieketang/particle/big_explosion.py

import cocos.particle_systems
from cocos.euclid import Point2
from cocos.particle import Color


class BigExplosion(cocos.particle_systems.Explosion):
    """玩家或敌人爆炸粒子系统"""

    speed = 100.0  # 粒子移动速度
    life = 0.5  # 粒子生命期
    life_var = 0.2
    size = 5.0  # 粒子大小
    size_var = 1.0  # 粒子大小偏差
    gravity = Point2(0, 0)  # 粒子的重力， (0, 0)不受重力影响
    start_color = Color(0.7, 0.2, 0.5, 1.0)  # 粒子的开始颜色
    start_color_var = Color(0.5, 0.5, 0.7, 0.0)  # 粒子开始颜色偏差
    end_color = Color(0.5, 0.5, 0.5, 0.3)  # 粒子的结束颜色
    end_color_var = Color(0.5, 0.5, 0.5, 0.0)  # 粒子的结束颜色偏差
