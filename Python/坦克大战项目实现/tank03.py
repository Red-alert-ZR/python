"""
v1.03
    新增功能
    创建游戏窗口
    用到游戏引擎中的功能模块
    官方开发文档
"""
import pygame
_display = pygame.display
COLOR_BLACK = pygame.Color(0,0,0)
class MainGame():       #主函数类
    #游戏主窗口对象
    window = None
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 700
    def __init__(self):
        pass
    #开始游戏方法
    def startGame(self):
        _display.init()   #初始化显示模块
        #创建窗口加载窗口（借鉴官方文档）
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])   #初始化要显示的窗口或屏幕
        #设置一下游戏标题
        _display.set_caption("坦克大战v1.03")
        #让窗口持续刷新操作
        while True:

            #给窗口完成一个填充颜色
            MainGame.window.fill(COLOR_BLACK)
            _display.update()

    #结束游戏方法
    def endGame(self):
        print('谢谢使用')
        #结束Python解释器
        exit()
class Tank():       # 坦克类
    def __init__(self):
        pass
    #坦克移动方法
    def move(self):
        pass
    #射击方法
    def shot(self):
        pass
    #展示坦克方法
    def displayTank(self):
        pass
class MyTank(Tank):     # 我方坦克类
    def __init__(self):
        pass
class EnemyTank(Tank):      # 敌方坦克类
    def __init__(self):
        pass
class Bullet():     # 子弹类
    def __init__(self):
        pass
    # 子弹移动方法
    def move(self):
        pass
    # 子弹展示方法
    def display(self):
        pass
class Explode():        # 爆炸效果类
    def __init__(self):
        pass
    #展示爆炸效果类
    def display(self):
        pass
class Wall ():       # 墙壁类
    def __init__(self):
        pass
    #展示墙壁方法
    def display(self):
        pass
class Music():      #音效类
    def __init__(self):
        pass
    #开始播放音乐
    def play(self):
        pass
MainGame().startGame()

