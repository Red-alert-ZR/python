"""
v1.05
    新增功能
        实现左上角问题提示内容
            font
"""
import pygame
_display = pygame.display
COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_RED = pygame.Color(255,0,0)
version = 'v1.05'
class MainGame():       #主函数类
    # 游戏主窗口对象
    window = None
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 700
    def __init__(self):
        pass
    # 开始游戏方法
    def startGame(self):
        _display.init()   #初始化显示模块
        # 创建窗口加载窗口（借鉴官方文档）
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])   #初始化要显示的窗口或屏幕
        # 设置一下游戏标题
        _display.set_caption("坦克大战" + version)
        # 让窗口持续刷新操作
        while True:
            # 给窗口完成一个填充颜色
            MainGame.window.fill(COLOR_BLACK)
            # 在循环中持续完成事件的获取
            self.getEvent()
            # 将绘制文字得到的小画布，粘贴到窗口中
            MainGame.window.blit(self.getTextSurface("剩余敌方坦克%d辆" %5), (5, 5))
            # 窗口刷新
            _display.update()

    # 左上角文字绘制的功能
    def getTextSurface(self,text):
        # 初始化字体模块
        pygame.font.init()
        # 查看系统支持的所有字体
        # fontList = pygame.font.get_fonts()
        # print(fontList)
        # 选中一个合适的字体
        font = pygame.font.SysFont('微软雅黑', 18, bold = True, italic = False)
        # 使用对应的字符完成相关的内容的绘制
        textSurface = font.render(text, True, COLOR_RED)
        return textSurface

    #获取程序期间所有事件（鼠标事件，键盘事件）
    def getEvent(self):
        # 1、获取所有事件
        eventList = pygame.event.get()
        # 2、对事件进行判断处理（1、点击关闭按钮 2、按下键盘上的某个按钮）
        for event in eventList:
            # 判断 event.type 是否是QUIT，如果是退出，直接调用程序结束方法
            if event.type == pygame.QUIT:
                self.endGame()
            # 判断事件类型是否为按键按下，如果是，继续判断是哪一个按键，来进行对应的处理
            if event.type == pygame.KEYDOWN:
                # 具体是哪一个按键的处理
                if event.key == pygame.K_LEFT:
                    print('坦克向左调头，移动')
                elif event.key == pygame.K_RIGHT:
                    print('坦克向右调头，移动')
                elif event.key == pygame.K_UP:
                    print('坦克向上调头，移动')
                elif event.key == pygame.K_DOWN:
                    print('坦克向下调头，移动')
                elif event.key == pygame.K_SPACE:
                    print('发射子弹')

    # 结束游戏方法
    def endGame(self):
        print('谢谢使用')
        # 结束Python解释器
        exit()
class Tank():       # 坦克类
    def __init__(self):
        pass
    # 坦克移动方法
    def move(self):
        pass
    # 射击方法
    def shot(self):
        pass
    # 展示坦克方法
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
MainGame().startGame()

