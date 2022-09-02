"""
v1.11
    完善功能：
        1、完善子弹类的封装

"""
import pygame, time, random

_display = pygame.display
COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_RED = pygame.Color(255, 0, 0)
version = 'v1.11'


class MainGame():  # 主函数类
    # 游戏主窗口对象
    window = None
    SCREEN_WIDTH = 1000  # 1720
    SCREEN_HEIGHT = 800  # 1000
    # 创建我方坦克
    TANK_P1 = None
    # 存储所有地方坦克
    EnemyTank_list = []
    # 要创建的敌方坦克的数量
    EnemyTank_count = 5

    def __init__(self):
        pass

    # 开始游戏方法
    def startGame(self):
        _display.init()  # 初始化显示模块
        # 创建窗口加载窗口（借鉴官方文档）
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])  # 初始化要显示的窗口或屏幕
        # 创建我方坦克
        MainGame.TANK_P1 = Tank(500, 700)
        # 创建敌方坦克
        self.creatEnemyTank()
        # 设置一下游戏标题
        _display.set_caption("坦克大战" + version)
        # 让窗口持续刷新操作
        while True:
            # 给窗口完成一个填充颜色
            MainGame.window.fill(COLOR_BLACK)
            # 在循环中持续完成事件的获取
            self.getEvent()
            # 设置重复点击效果
            # pygame.key.set_repeat(pygame.KEYDOWN,50)
            # 将绘制文字得到的小画布，粘贴到窗口中
            MainGame.window.blit(self.getTextSurface("剩余敌方坦克%d辆" % len(MainGame.EnemyTank_list)), (5, 5))
            # 将我方坦克加入到窗口中
            MainGame.TANK_P1.displayTank()
            # 循环展示敌方坦克
            self.blitEnemyTank()
            # 根据坦克的开关状态调用坦克的移动方法
            if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
                MainGame.TANK_P1.move()
            time.sleep(0.02)
            # 窗口刷新
            _display.update()

    # 创建敌方坦克
    def creatEnemyTank(self):
        speed = random.uniform(1.0, 2.0)
        for i in range(MainGame.EnemyTank_count):
            left = random.randint(0, 9)
            top = random.randint(0, 6)
            eTank = EnemyTank(left * 100, top * 100, speed)
            MainGame.EnemyTank_list.append(eTank)

    # 将坦克加入到窗口中
    def blitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            eTank.displayTank()
            # 调用坦克的移动方法
            eTank.randMove()

    # 左上角文字绘制的功能
    def getTextSurface(self, text):
        # 初始化字体模块
        pygame.font.init()
        # 查看系统支持的所有字体
        # fontList = pygame.font.get_fonts()
        # print(fontList)
        # 选中一个合适的字体
        font = pygame.font.SysFont('微软雅黑', 18, bold=True, italic=False)
        # 使用对应的字符完成相关的内容的绘制
        textSurface = font.render(text, True, COLOR_RED)
        return textSurface

    # 获取程序期间所有事件（鼠标事件，键盘事件）
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
                    # 修改坦克方向
                    MainGame.TANK_P1.direction = 'L'
                    # 完成移动操作（调用坦克的移动方法）
                    # MainGame.TANK_P1.move()
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_RIGHT:
                    print('坦克向右调头，移动')
                    # 修改坦克方向
                    MainGame.TANK_P1.direction = 'R'
                    # MainGame.TANK_P1.move()
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_UP:
                    print('坦克向上调头，移动')
                    # 修改坦克方向
                    MainGame.TANK_P1.direction = 'U'
                    # MainGame.TANK_P1.move()
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_DOWN:
                    print('坦克向下调头，移动')
                    # 修改坦克方向
                    MainGame.TANK_P1.direction = 'D'
                    # MainGame.TANK_P1.move()
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_SPACE:
                    print('发射子弹')
            if event.type == pygame.KEYUP:
                # 松开的是方向键，才更改移动开关状态
                if event.key == pygame.K_LEFT or event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == pygame.K_RIGHT:
                    # 修改坦克移动状态
                    MainGame.TANK_P1.stop = True

    # 结束游戏方法
    def endGame(self):
        print('谢谢使用')
        # 结束Python解释器
        exit()


class Tank():  # 坦克类
    def __init__(self, left, top):
        self.images = {
            'U': pygame.image.load('TankWar-master/image/p1tankU.png'),
            'D': pygame.image.load('TankWar-master/image/p1tankD.png'),
            'L': pygame.image.load('TankWar-master/image/p1tankL.png'),
            'R': pygame.image.load('TankWar-master/image/p1tankR.png')
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        # 坦克所在的区域 Rect ->
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置 分别距x轴，y轴的位置
        self.rect.left = left
        self.rect.top = top
        # 新增速度属性
        self.speed = 5
        # 新增属性： 坦克的移动开关
        self.stop = True

    # 坦克移动方法
    def move(self):
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < MainGame.SCREEN_WIDTH:
                self.rect.left += self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < MainGame.SCREEN_HEIGHT:
                self.rect.top += self.speed

    # 射击方法
    def shot(self):
        pass

    # 展示坦克方法（将坦克这个surface绘制到窗口中 bilt()）
    def displayTank(self):
        # 1、重新设置坦克的图片
        self.image = self.images[self.direction]
        # 2、将坦克加入到窗口中
        MainGame.window.blit(self.image, self.rect)


class MyTank(Tank):  # 我方坦克类
    def __init__(self):
        pass


class EnemyTank(Tank):  # 敌方坦克类
    def __init__(self, left, top, speed):
        self.images = {
            'U': pygame.image.load('TankWar-master/image/p2tankU.png'),
            'D': pygame.image.load('TankWar-master/image/p2tankD.png'),
            'L': pygame.image.load('TankWar-master/image/p2tankL.png'),
            'R': pygame.image.load('TankWar-master/image/p2tankR.png')
        }
        self.direction = self.randDirection()
        self.image = self.images[self.direction]
        # 坦克所在的区域 Rect ->
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置 分别距x轴，y轴的位置
        self.rect.left = left
        self.rect.top = top
        # 新增速度属性
        self.speed = 5
        # 新增属性： 坦克的移动开关
        self.stop = True
        # 新增步数属性，用来控制敌方坦克随机移动
        self.step = 50

    # 敌方坦克随机方向选择
    def randDirection(self):
        tempDirection = None
        num = random.randint(1, 4)
        if num == 1:
            tempDirection = 'U'
        elif num == 2:
            tempDirection = 'D'
        elif num == 3:
            tempDirection = 'L'
        elif num == 4:
            tempDirection = 'R'
        return tempDirection

    # 随机移动
    def randMove(self):
        if self.step <= 0:
            self.direction = self.randDirection()
            self.step = 50
        else:
            self.move()
            self.step -= 1

    # def displayEnemyTank(self):
    # super().displayTank()


class Bullet():  # 子弹类
    def __init__(self, tank):
        #图片
        self.image = pygame.image.load('TankWar-master/images/bullet/bullet.png')
        #方向（坦克方向）
        self.direction = tank.direction
        #位置
        self.rect = self.image.get_rect()
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank.rect.top -  self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + self.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + self.rect.height
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + self.rect.height
        #速度
        self.speed = 7


    # 子弹移动方法
    def move(self):
        pass

    # 子弹展示方法
    def displayBullet(self):
        MainGame.window.blit(self.image, self.rect)


class Explode():  # 爆炸效果类
    def __init__(self):
        pass

    # 展示爆炸效果类
    def display(self):
        pass


class Wall():  # 墙壁类
    def __init__(self):
        pass

    # 展示墙壁方法
    def display(self):
        pass


class Music():  # 音效类
    def __init__(self):
        pass

    # 开始播放音乐
    def play(self):
        pass


MainGame().startGame()



