"""
1.游戏引擎的安装：
    安装的方式有两种：
        1.pip安装
            pip install pygame == 版本号
        2.pycharm
            File --> setting --> project --> project Interpreter -->
            右侧 + install --> 搜索框输入pygame --> 下方installPackage
    验证pygame是否好用
        import pygame

2.明白需求（基于面向对象的分析）：
    1、有那些类组成： 2、不同的类所具备的一些功能：
        1、主逻辑类
            开始游戏
            结束游戏
        2、坦克类（1、我方坦克 2、敌方坦克）
            移动
            射击
            展示坦克
        3、子弹类
            移动
            展示子弹
        4、爆炸效果类
            展示爆炸效果
        5、墙壁类
            属性： 是否可以通过
        6、音效类
            播放音乐
3、坦克大战项目框架的搭建
    涉及到的类，用代码简单的实现
"""
import pygame
class MainGame():       #主函数类
    def __init__(self):
        pass
    #开始游戏方法
    def startGame(self):
        pass
    #结束游戏方法
    def endGame(self):
        pass
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
    # 展示爆炸效果类
    def display(self):
        pass
class Wall ():       # 墙壁类
    def __init__(self):
        pass
    # 展示墙壁方法
    def display(self):
        pass
class Music():      #音效类
    def __init__(self):
        pass
    # 开始播放音乐
    def play(self):
        pass

