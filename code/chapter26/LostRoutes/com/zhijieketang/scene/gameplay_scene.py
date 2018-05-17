# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter26/LostRoutes/com/zhijieketang/scene/gameplay_scene.py

"""游戏场景"""
import logging

import cocos
import cocos.actions
import cocos.layer
import cocos.particle_systems
import cocos.scene
import cocos.scenes
import cocos.sprite
import pyglet

from com.zhijieketang.particle.big_explosion import BigExplosion
from com.zhijieketang.scene import gameover_scene, home_scene
from com.zhijieketang.sprite.bullet_sprite import Bullet
from com.zhijieketang.sprite.enemy_sprite import Enemy, EnemyType, EnemyScore
from com.zhijieketang.sprite.fighter_sprite import Fighter
from com.zhijieketang.utility import tools

# 资源图片路径
RES_PATH = 'resources/image/gameplay/'
logger = logging.getLogger(__name__)


class GamePlayLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        super(GamePlayLayer, self).__init__()

        logger.info("初始化游戏场景")

        # 播放游戏场景背景音乐
        tools.playmusic('game_bg.ogg')

        # 获得窗口的宽度和高度
        self.s_width, self.s_height = cocos.director.director.get_window_size()

        # 初始化背景
        self.init_bg()

        # 初始化状态栏
        self.init_statusbar()

        # 初始化游戏精灵
        self.init_gamesprite()

    def init_bg(self):
        """初始化背景"""

        # 创建游戏场景背景
        background = cocos.sprite.Sprite(RES_PATH + 'bg.png')
        background.position = self.s_width // 2, self.s_height // 2
        # 添加游戏场景背景
        self.add(background, 0)

        # 添加背景精灵1.
        sprite1 = cocos.sprite.Sprite(RES_PATH + 'bgsprite1.png')
        self.add(sprite1, 0)
        sprite1.position = 5, 5
        ac1 = cocos.actions.MoveTo((340, 500), 20)
        ac2 = cocos.actions.MoveTo((5, 5), 20)
        ac3 = ac1 + ac2
        action = cocos.actions.Repeat(ac3)
        sprite1.do(action)

        # 添加背景精灵2
        sprite2 = cocos.sprite.Sprite(RES_PATH + 'bgsprite2.png')
        self.add(sprite2, 0)
        sprite2.position = 340, 5
        ac1 = cocos.actions.MoveTo((0, 500), 20)
        ac2 = cocos.actions.MoveTo((340, 5), 20)
        ac3 = ac1 + ac2
        action = cocos.actions.Repeat(ac3)
        sprite2.do(action)

    def init_statusbar(self):
        """初始化状态栏"""

        # 初始化暂停按钮
        self.pausebutton = cocos.sprite.Sprite(RES_PATH + 'button.pause.png')
        self.add(self.pausebutton, 2)
        self.pausebutton.position = 30, self.s_height - 28

        # 初始化返回主菜单按钮
        self.backbutton = cocos.sprite.Sprite(RES_PATH + 'button.back.png')
        self.add(self.backbutton, 2)
        self.backbutton.position = self.s_width // 2, self.s_height // 2 - 28
        self.backbutton.visible = False

        # 初始化继续游戏菜单按钮
        self.resumebutton = cocos.sprite.Sprite(RES_PATH + 'button.resume.png')
        self.add(self.resumebutton, 2)
        self.resumebutton.position = self.s_width // 2, self.s_height // 2 + 28
        self.resumebutton.visible = False

        # 在状态栏中设置玩家的生命值
        fg = cocos.sprite.Sprite(RES_PATH + 'life.png')
        fg.position = self.s_width - 60, self.s_height - 28
        self.add(fg, 0)

        self.lifelabel = cocos.text.Label(
            font_name='Harlow Solid Italic',
            font_size=18,
            anchor_x='center', anchor_y='center')
        self.lifelabel.position = fg.position[0] + 30, fg.position[1]
        self.add(self.lifelabel, 0)

        # 在状态栏中显示得分
        self.scorelabel = cocos.text.Label(
            font_name='Harlow Solid Italic',
            font_size=18,
            anchor_x='center', anchor_y='center')
        self.scorelabel.position = self.s_width // 2, self.s_height - 28
        self.add(self.scorelabel, 0)

        # 累计得分
        self.score = 0
        # 累计得分，每次获得1000分数，生命值加一，scoreplaceholder恢复为0
        self.scoreplaceholder = 0

        # 1暂停 0继续
        self.pause_status = 0

    def init_gamesprite(self):
        """初始化游戏精灵"""

        # 初始化陨石
        self.stone = Enemy(EnemyType.Stone)
        self.add(self.stone, 1, 'enemy1')

        # 初始化行星
        self.planet = Enemy(EnemyType.Planet)
        self.add(self.planet, 1, 'enemy2')

        # 初始化敌机1
        self.enemyfighter1 = Enemy(EnemyType.Fighter1)
        self.add(self.enemyfighter1, 1, 'enemy3')

        # 初始化敌机2
        self.enemyfighter2 = Enemy(EnemyType.Fighter2)
        self.add(self.enemyfighter2, 1, 'enemy4')

        # 产生敌人精灵
        for i in range(1, 5):
            name = 'enemy{0}'.format(i)
            enemy = self.get(name)
            enemy.spawn()

        # 初始化玩家
        self.player = Fighter()
        self.player.position = self.s_width // 2, 50
        self.add(self.player, 1)

        # 游戏调度时间间隔累计
        self.elapsedtime = 0

        # 开始游戏调度
        self.schedule(self.update)

    def on_mouse_release(self, x, y, button, modifiers):
        """鼠标释放"""
        if button == pyglet.window.mouse.LEFT:

            pausebuttonrect = self.pausebutton.get_rect()

            # 单击暂停按钮
            if pausebuttonrect.contains(x, y) and self.pause_status == 0:
                logger.debug('单击暂停按钮')
                self.resumebutton.visible = True
                self.backbutton.visible = True
                self.pausebutton.visible = False
                # 播放音效
                tools.playeffect('Blip.wav')
                self.pause_status = 1
                # 暂停
                for i in range(1, 5):
                    name = 'enemy{0}'.format(i)
                    enemy = self.get(name)
                    enemy.pause_enemy()

                self.unschedule(self.update)

            resumebuttonrect = self.resumebutton.get_rect()
            # 单击继续游戏菜单按钮
            if resumebuttonrect.contains(x, y) and self.pause_status == 1:
                logger.debug('单击继续游戏菜单按钮')
                self.resumebutton.visible = False
                self.backbutton.visible = False
                self.pausebutton.visible = True

                # 播放音效
                tools.playeffect('Blip.wav')
                self.pause_status = 0

                # 继续
                for i in range(1, 5):
                    name = 'enemy{0}'.format(i)
                    enemy = self.get(name)
                    enemy.resume_enemy()

                self.schedule(self.update)

            backbuttonrect = self.backbutton.get_rect()
            # 单击返回主菜单按钮
            if backbuttonrect.contains(x, y) and self.pause_status == 1:
                logger.debug('单击返回主菜单按钮')
                # 切换场景
                next_scene = home_scene.create_scene()
                ts = cocos.scenes.FadeTransition(next_scene, 1.0)
                cocos.director.director.push(ts)
                # 播放音效
                tools.playeffect('Blip.wav')
                # 更换播放背景音乐
                tools.playmusic('home_bg.ogg')

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        """鼠标拖曳"""

        if self.pause_status == 0:  # 继续状态下可以拖曳鼠标
            self.player.move((dx, dy))

    def update(self, dt):
        """游戏调度"""

        self.elapsedtime += dt
        if self.elapsedtime > 0.2:  # 每0.2秒发射1发子弹
            self.elapsedtime = 0
            if self.player.visible:
                bullet = Bullet()
                self.add(bullet, 2)
                bullet.shoot_bullet(self.player)

        for node in self.get_children():
            # 移除不可见子弹精灵，释放内存
            if not node.visible and isinstance(node, Bullet):
                self.remove(node)

        # 检测碰撞
        self.test_collision()
        # 更新状态栏
        self.updatestatusbar()

    def test_collision(self):
        """检测碰撞"""

        # 检测子弹与敌人的碰撞
        for node in self.get_children():

            if isinstance(node, Bullet) and node.visible:

                bulletrect = node.get_rect()
                if bulletrect.intersect(self.stone.get_rect()):  # 检测到与陨石敌人碰撞
                    self.handle_bullet_enemy_collision(self.stone)
                    node.visible = False
                    continue

                if bulletrect.intersect(self.enemyfighter1.get_rect()):  # 检测到与敌机1碰撞
                    self.handle_bullet_enemy_collision(self.enemyfighter1)
                    node.visible = False
                    continue

                if bulletrect.intersect(self.enemyfighter2.get_rect()):  # 检测到与敌机2碰撞
                    self.handle_bullet_enemy_collision(self.enemyfighter2)
                    node.visible = False
                    continue

                if bulletrect.intersect(self.planet.get_rect()):  # 检测到与行星碰撞
                    self.handle_bullet_enemy_collision(self.planet)
                    node.visible = False
                    continue

        # 检测玩家与敌人的碰撞
        if self.player.visible:

            playerrect = self.player.get_rect()

            if playerrect.intersect(self.stone.get_rect()):  # 玩家飞机与陨石发生碰撞
                self.handle_player_enemy_collision(self.stone)
                return

            if playerrect.intersect(self.enemyfighter1.get_rect()): # 玩家飞机与敌机1发生碰撞
                self.handle_player_enemy_collision(self.enemyfighter1)
                return

            if playerrect.intersect(self.enemyfighter2.get_rect()): # 玩家飞机与敌机2发生碰撞
                self.handle_player_enemy_collision(self.enemyfighter2)
                return

            if playerrect.intersect(self.planet.get_rect()): # 玩家飞机与行星发生碰撞
                self.handle_player_enemy_collision(self.planet)
                return

    def handle_player_enemy_collision(self, enemy):
        """处理玩家与敌人的碰撞检测"""

        # 设置敌人消失
        enemy.visible = False
        enemy.spawn()

        # 处理爆炸
        self.doexplosion(enemy.position)

        # 设置玩家消失
        self.player.visible = False
        self.player.hit_points -= 1

        if self.player.hit_points <= 0:

            logger.info('GameOver')
            next_scene = gameover_scene.create_scene(self.score)
            ts = cocos.scenes.FadeTransition(next_scene, 1.0)
            cocos.director.director.push(ts)

        else:
            ac1 = cocos.actions.Place((self.s_width // 2, 50))
            ac2 = cocos.actions.Show()
            ac3 = cocos.actions.FadeIn(0.8)
            action = ac1 + ac2 + ac3
            self.player.do(action)

    def handle_bullet_enemy_collision(self, enemy):
        """处理子弹与敌人的碰撞检测"""

        enemy.hit_points -= 1
        if enemy.hit_points <= 0:

            # 处理爆炸
            self.doexplosion(enemy.position)

            # 设置敌人消失
            enemy.visible = False
            enemy.spawn()

            # 计分
            if enemy.type == EnemyType.Stone:
                self.score += EnemyScore[EnemyType.Stone]
                self.scoreplaceholder += EnemyScore[EnemyType.Stone]
            elif enemy.type == EnemyType.Fighter1:
                self.score += EnemyScore[EnemyType.Fighter1]
                self.scoreplaceholder += EnemyScore[EnemyType.Fighter1]
            elif enemy.type == EnemyType.Fighter2:
                self.score += EnemyScore[EnemyType.Fighter2]
                self.scoreplaceholder += EnemyScore[EnemyType.Fighter2]
            elif enemy.type == EnemyType.Planet:
                self.score += EnemyScore[EnemyType.Planet]
                self.scoreplaceholder += EnemyScore[EnemyType.Planet]

            # 每次获得1000分数，生命值加一，scoreplaceholder恢复0
            if self.scoreplaceholder >= 1000:
                self.player.hit_points += 1
                self.scoreplaceholder -= 1000

    def doexplosion(self, p):
        """处理爆炸"""

        # 爆炸
        for node in self.get_children():
            if isinstance(node, BigExplosion):
                self.remove(node)
                break

        sp = BigExplosion()
        sp.position = p
        self.add(sp, 2)
        # 播放音效
        tools.playeffect('Explosion.wav')

    def updatestatusbar(self):
        """更新状态栏"""

        # 添加生命值 x 5
        self.lifelabel.element.text = 'x' + str(self.player.hit_points)
        self.scorelabel.element.text = str(self.score)


def create_scene():
    """创建游戏场景函数"""

    # 创建游戏场景
    scene = cocos.scene.Scene(GamePlayLayer())
    return scene
