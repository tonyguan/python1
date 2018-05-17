# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter26/LostRoutes/com/zhijieketang/particle/fighter_fire.py

import cocos.particle_systems
from cocos.particle import Color


class FighterFire(cocos.particle_systems.Smoke):
    """飞机喷射火焰粒子系统"""

    angle = 270.0  # 粒子方向角度
    speed = 50.0  # 粒子移动速度
    life = 1.0  # 粒子生命期
    size = 20.0  # 粒子大小
    size_var = 5.0  # 粒子大小偏差
    start_color = Color(0.1, 0.25, 1.0, 1.0)  # 粒子的开始颜色
    start_color_var = Color(0.0, 0.0, 0.0, 0.0)  # 粒子开始颜色偏差
    end_color = Color(0.0, 0.0, 0.0, 0.0)  # 粒子的结束颜色
    end_color_var = Color(0.0, 0.0, 0.0, 0.0)  # 粒子的结束颜色偏差
