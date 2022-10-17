"""
v1.26
    新增功能：
        1、增加重型（天启）坦克
"""
import pygame, time, random


_display = pygame.display
COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_RED = pygame.Color(255, 0, 0)
version = 'v1.26'


class MainGame:  # 主函数类
    # 游戏主窗口对象
    window = None
    SCREEN_WIDTH = 1000  # 1720
    SCREEN_HEIGHT = 800  # 1000
    # 创建我方坦克
    TANK_P1 = None
    # 存储所有敌方轻型坦克
    EnemyTank_A_list = []
    # 要创建的敌方轻型坦克的数量
    EnemyTank_A_count = 6
    # 存储所有敌方重型坦克
    EnemyTank_B_list = []
    # 要创建的敌方重型的数量
    EnemyTank_B_count = 3
    # 存储我方子弹的列表
    Bullet_list = []
    # 存储敌方子弹列表
    Enemy_bullet_list = []
    # 爆炸效果列表
    Explode_list = []
    # 墙壁列表
    Wall_list = []
    # 老巢
    home = None
    # 失败图标
    G = None

    def __init__(self):
        pass
    # 开始游戏方法
    def startGame(self):
        _display.init()  # 初始化显示模块
        # 创建窗口加载窗口（借鉴官方文档）
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])  # 初始化要显示的窗口或屏幕
        # 创建我方坦克
        self.creatMyTank()
        # 创建敌方坦克
        self.creatEnemyTank_A()
        # 创建敌方坦克
        self.creatEnemyTank_B()
        # 创建墙壁
        self.creatWalls_A()
        # 创建老巢
        self.creatHome()
        # 创建失败图标
        self.creatGameOver()
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
            MainGame.window.blit(self.getTextSurface("剩余敌方坦克%d辆" % len(MainGame.EnemyTank_A_list + MainGame.EnemyTank_B_list)), (5, 5))
            # 调用展示墙壁的方法
            self.blitWalls_A()
            # 展示老巢
            self.blitHome()
            # 展示我方坦克
            self.blitMyTank()
            # 循环展示敌方坦克
            self.blitEnemyTank_A()
            if len(MainGame.EnemyTank_A_list) == 0:
                self.blitEnemyTank_B()
            # 调用渲染子弹列表的一个方法
            self.blitBUllet()
            # 调用渲染敌方子弹列表的一个方法
            self.blitEnemyBullet()
            #调用爆炸效果方法
            self.displayExplodes()
            time.sleep(0.02)
            # 窗口刷新
            _display.update()
            # 失败方法
            if MainGame.home.live == False:
                self.blitGameOver()
                _display.update()
                music = Music('TankWar-master/music/天赐音画 - 超级玛丽失败音效 (节目).mp3')
                music.play()
                pygame.time.delay(2200)
                return exit()



    # 创建我方坦克方法
    def creatMyTank(self):
        # 创建我方坦克
        MainGame.TANK_P1 = MyTank(465, 400)
        # 创建音乐对象
        music = Music('TankWar-master/music/start.wav')
        # 调用播放音乐方法
        music.play()

    # 加入我方坦克
    def blitMyTank(self):
        # 将我方坦克加入到窗口中
        if MainGame.TANK_P1 and MainGame.TANK_P1.live:
            MainGame.TANK_P1.displayTank()
            # 根据坦克的开关状态调用坦克的移动方法
            if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
                MainGame.TANK_P1.move()
            # 调用碰撞墙壁的方法
            MainGame.TANK_P1.hitWalls()
            # 调用碰撞到敌方坦克
            MainGame.TANK_P1.hitEnemyTank()
            # 调用敌方坦克碰撞老巢方法
            MainGame.TANK_P1.hitHomes()
            # MainGame.TANK_P1.hitMyTank_EnemyTank()
        else:
            del MainGame.TANK_P1
            MainGame.TANK_P1 = None

    # 创建敌方坦克
    def creatEnemyTank_A(self):
        for i in range(MainGame.EnemyTank_A_count):
            speed = random.uniform(2.0, 5.0)
            top = random.randint(0,10)
            if top == 1:
                left = random.randint(0, 20)
            elif 4 <= top <= 8:
                left = random.randint(0, 10)
            elif 9 <= top <= 10:
                left = random.randint(10, 20)
            else:
                left = 19
            eTank = EnemyTank_A(left * 50, top * 50, speed)
            MainGame.EnemyTank_A_list.append(eTank)

    # 创建敌方重型坦克
    def creatEnemyTank_B(self):
        for i in range(MainGame.EnemyTank_B_count):
            speed = random.uniform(2.0, 5.0)
            top = random.randint(0,10)
            if top == 1:
                left = random.randint(0, 20)
            elif 4 <= top <= 8:
                left = random.randint(0, 10)
            elif 9 <= top <= 10:
                left = random.randint(10, 20)
            else:
                left = 19
            eTank = EnemyTank_B(left * 50, top * 50, speed)
            MainGame.EnemyTank_B_list.append(eTank)

    # 创建墙壁的方法
    def creatWalls_A(self):
        for i in range(2, 8):
            wall = Wall_A(140, 50 * i)
            MainGame.Wall_list.append(wall)
        for i in range(2, 8):
            wall = Wall_A(MainGame.SCREEN_WIDTH - 190, 50 * i)
            MainGame.Wall_list.append(wall)
        for i in range(0, 5):
            wall = Wall_A(50 * i, MainGame.SCREEN_HEIGHT - 250)
            MainGame.Wall_list.append(wall)
        for i in range(1, 6):
            wall = Wall_A(MainGame.SCREEN_WIDTH - (50 * i), MainGame.SCREEN_HEIGHT - 250)
            MainGame.Wall_list.append(wall)
        for i in range(1, 4):
            wall = Wall_A(MainGame.SCREEN_WIDTH - 450, MainGame.SCREEN_HEIGHT - 50 * i)
            MainGame.Wall_list.append(wall)
        for i in range(1, 4):
            wall = Wall_A(400, MainGame.SCREEN_HEIGHT - 50 * i)
            MainGame.Wall_list.append(wall)
        for i in range(1, 4):
            wall = Wall_A(400 + i * 50, MainGame.SCREEN_HEIGHT - 150)
            MainGame.Wall_list.append(wall)

    # 将墙壁加入到窗口中
    def blitWalls_A(self):
        for wall in MainGame.Wall_list:
            if wall.live:
                wall.displayWall()
            else:
                MainGame.Wall_list.remove(wall)

    # 创建老巢的方法
    def creatHome(self):
       MainGame.home = Home(455, 700)

    # 展示老巢的方法
    def blitHome(self):
        if MainGame.home.live:
            MainGame.home.displayHome()
        else:
            MainGame.home.live = False

    # 将敌方坦克加入到窗口中
    def blitEnemyTank_A(self):
        for eTank in MainGame.EnemyTank_A_list:
            if eTank.live:
                eTank.displayTank()
                # 调用敌方坦克的射击方法
                eBullet = eTank.shot_A()
                # 调用坦克的移动方法
                eTank.randMove_A()
                # 调用敌方坦克碰撞墙壁方法
                eTank.hitWalls()
                # 调用敌方坦克碰撞我方坦克方法
                eTank.hitMyTank_A()
                # 调用敌方坦克碰撞老巢方法
                eTank.hitHomes()
                # 调用敌方坦克碰撞敌方坦克方法
                #eTank.hitEnemyTank_EnemyTank() ---有问题
                # 将子弹存储到敌方子弹列表
                if eBullet and len(MainGame.Enemy_bullet_list) <= 2:
                    # 如果子弹为None，不加入列表
                    MainGame.Enemy_bullet_list.append(eBullet)
            else:
                MainGame.EnemyTank_A_list.remove(eTank)

    # 将敌方坦克加入到窗口中
    def blitEnemyTank_B(self):
        for eTank in MainGame.EnemyTank_B_list:
            if eTank.live:
                eTank.displayTank()
                # 调用敌方坦克的射击方法
                eBullet = eTank.shot_B()
                # 调用坦克的移动方法
                eTank.randMove_B()
                # 调用敌方坦克碰撞墙壁方法
                eTank.hitWalls()
                # 调用敌方坦克碰撞我方坦克方法
                eTank.hitMyTank_B()
                # 调用敌方坦克碰撞老巢方法
                eTank.hitHomes()
                # 调用敌方坦克碰撞敌方坦克方法
                #eTank.hitEnemyTank_EnemyTank() ---有问题
                # 将子弹存储到敌方子弹列表
                if eBullet and len(MainGame.Enemy_bullet_list) <= 2:
                    # 如果子弹为None，不加入列表
                    MainGame.Enemy_bullet_list.append(eBullet)
            else:
                MainGame.EnemyTank_B_list.remove(eTank)

    #将我方子弹加入到窗口中
    def blitBUllet(self):
        for bullet in MainGame.Bullet_list:
            # 如果子弹还活着，绘制出来，否则，从列表中移除该子弹
            if bullet.live:
                bullet.displayBullet()
                # 让子弹移动
                bullet.bulletMove()
                # 调用我方子弹与敌方坦克的碰撞方法
                bullet.hitEnemyTank()
                # 调用判断我方子弹是否碰撞到墙壁的方法
                bullet.hitWall()
                # 调用我方子弹碰撞老巢
                bullet.hitHome()
            else:
                MainGame.Bullet_list.remove(bullet)

    #将敌方子弹加入到窗口中
    def blitEnemyBullet(self):
        for ebullet in MainGame.Enemy_bullet_list:
            # 如果子弹还活着，绘制出来，否则，从列表中移除该子弹
            if ebullet.live:
                ebullet.displayBullet()
                # 让子弹移动
                ebullet.bulletMove()
                # 调用判断敌方子弹是否碰撞到墙壁的方法
                ebullet.hitWall()
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                    ebullet.hitMyTank()
                # 调用子弹碰撞老巢
                ebullet.hitHome()
            else:
                MainGame.Enemy_bullet_list.remove(ebullet)

    #将爆炸效果加入到窗口中
    def displayExplodes(self):
        for explode in MainGame.Explode_list:
            #显示爆炸效果
            if explode.live:
                explode.displayExplode()
            else:
                MainGame.Explode_list.remove(explode)

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
                #点击 'J' 按键让我方坦克重生
                if event.key == pygame.K_j and not MainGame.TANK_P1:
                    #调用创建我方坦克的方法
                    self.creatMyTank()

                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
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
                        if len(MainGame.Bullet_list) < 3:
                            #产生一颗子弹
                            m = Bullet(MainGame.TANK_P1)
                            #将子弹加入子弹列表
                            MainGame.Bullet_list.append(m)
                            music = Music('TankWar-master/music/fire.wav')
                            music.play()
                        else:
                            print('子弹数量不足')

            if event.type == pygame.KEYUP:
                # 松开的是方向键，才更改移动开关状态
                if event.key == pygame.K_LEFT or event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == pygame.K_RIGHT:
                    if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                        # 修改坦克移动状态
                        MainGame.TANK_P1.stop = True

    #　创建失败图标
    def creatGameOver(self):
        MainGame.G = GameOver(MainGame.SCREEN_WIDTH / 4, MainGame.SCREEN_HEIGHT / 3)

    # 将失败图标导入窗口
    def blitGameOver(self):
        MainGame.G.Gplay()

    # 结束游戏方法
    def endGame(self):
        print('谢谢使用')

        # 结束Python解释器
        exit()

class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class GameOver():
    def __init__(self, left, top):
        self.image = pygame.image.load('resources/images/end/gameover.png')
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top

    def Gplay(self):
        MainGame.window.blit(self.image, self.rect)

class Tank(BaseItem):  # 坦克类
    def __init__(self, left, top):
        BaseItem.__init__(self)
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
        # 新增属性：live用来记录，坦克是否活着
        self.live = True
        # 新增属性： 用来记录坦克移动之前的坐标
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top

    # 坦克移动方法
    def move(self):
        # 先记录移动之前的坐标
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
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

    #还原方法
    def stay(self):
        self.rect.left = self.oldLeft
        self.rect.top = self.oldTop

    #新增碰撞墙壁方法
    def hitWalls(self):
        for wall in MainGame.Wall_list:
            if pygame.sprite.collide_rect(wall, self):
                self.stay()

    # 新增主动碰撞到老巢
    def hitHomes(self):
        if pygame.sprite.collide_rect(MainGame.home, self):
            self.stay()

    #我方坦克碰撞敌方坦克方法
    def hitMyTank_EnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if pygame.sprite.collide_rect(eTank, self):
                self.stay()

    #敌方坦克碰撞我方坦克方法
    def hitEnemyTank_MyTank(self):
        if MainGame.TANK_P1:
            if pygame.sprite.collide_rect(self, MainGame.TANK_P1):
                self.stay()

    # 敌方坦克碰撞敌方坦克方法 ---- 有问题
    def hitEnemyTank_EnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            MainGame.EnemyTank_list_New = MainGame.EnemyTank_list
            MainGame.EnemyTank_list.remove(eTank)
            for eTank in MainGame.EnemyTank_list_New:
                if pygame.sprite.collide_rect(eTank, self):
                    self.stay()

    # 射击方法
    def shot(self):
        return Bullet(self)

    # 展示坦克方法（将坦克这个surface绘制到窗口中 bilt()）
    def displayTank(self):
        # 1、重新设置坦克的图片
        self.image = self.images[self.direction]
        # 2、将坦克加入到窗口中
        MainGame.window.blit(self.image, self.rect)

class MyTank(Tank):  # 我方坦克类
    def __init__(self, left, top):
        super(MyTank, self).__init__(left, top)

    #新增主动碰撞到敌方坦克
    def hitEnemyTank(self):
        for eTank in MainGame.EnemyTank_A_list:
            if pygame.sprite.collide_rect(eTank, self):
                self.stay()
        for eTank in MainGame.EnemyTank_B_list:
            if pygame.sprite.collide_rect(eTank, self):
                self.stay()



class EnemyTank_A(Tank):  # 敌方坦克类
    def __init__(self, left, top, speed):
        self.left = left
        self.top = top
        super(EnemyTank_A, self).__init__(self.left, self.top)
        self.images = {
            'U': pygame.image.load('resources/images/A_enemy/enemyU.png'),
            'D': pygame.image.load('resources/images/A_enemy/enemyD.png'),
            'L': pygame.image.load('resources/images/A_enemy/enemyL.png'),
            'R': pygame.image.load('resources/images/A_enemy/enemyR.png')
        }
        self.direction = self.randDirection()
        self.image = self.images[self.direction]
        # 坦克所在的区域 Rect ->
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置 分别距x轴，y轴的位置
        self.rect.left = left
        self.rect.top = top
        # 新增速度属性
        self.speed = speed
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
    def randMove_A(self):
        if self.step <= 0:
            self.direction = self.randDirection()
            self.step = 75
        else:
            self.move()
            self.step -= 1

    #射击方法
    def shot_A(self):
        num = random.randint(1,100)
        if num == 1:
            return Bullet(self)

    # 敌方坦克碰撞我方坦克方法
    def hitMyTank_A(self):
        if MainGame.TANK_P1:
            if pygame.sprite.collide_rect(self, MainGame.TANK_P1):
                #让敌方坦克停下来
                self.stay()

class EnemyTank_B(Tank):  # 敌方坦克类
    def __init__(self, left, top, speed):
        self.left = left
        self.top = top
        super(EnemyTank_B, self).__init__(self.left, self.top)
        self.images = {
            'U': pygame.image.load('resources/images/B_enemy/enemyU.png'),
            'D': pygame.image.load('resources/images/B_enemy/enemyD.png'),
            'L': pygame.image.load('resources/images/B_enemy/enemyL.png'),
            'R': pygame.image.load('resources/images/B_enemy/enemyR.png')
        }
        self.direction = self.randDirection()
        self.image = self.images[self.direction]
        # 坦克所在的区域 Rect ->
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置 分别距x轴，y轴的位置
        self.rect.left = left
        self.rect.top = top
        # 新增速度属性
        self.speed = speed
        # 新增属性： 坦克的移动开关
        self.stop = True
        # 新增步数属性，用来控制敌方坦克随机移动
        self.step = 50
        #　增加生命值
        self.hp = 3

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
    def randMove_B(self):
        if self.step <= 0:
            self.direction = self.randDirection()
            self.step = 75
        else:
            self.move()
            self.step -= 1

    #射击方法
    def shot_B(self):
        num = random.randint(1,100)
        if num == 1:
            return Bullet(self)

    # 敌方坦克碰撞我方坦克方法
    def hitMyTank_B(self):
        if MainGame.TANK_P1:
            if pygame.sprite.collide_rect(self, MainGame.TANK_P1):
                #让敌方坦克停下来
                self.stay()

class Bullet(BaseItem):  # 子弹类
    def __init__(self, tank):
        BaseItem.__init__(self)
        #图片
        self.images ={
            'U' : pygame.image.load('TankWar-master/images/bullet/bullet_U.png'),
            'D' : pygame.image.load('TankWar-master/images/bullet/bullet_D.png'),
            'L' : pygame.image.load('TankWar-master/images/bullet/bullet_L.png'),
            'R' : pygame.image.load('TankWar-master/images/bullet/bullet_R.png')
        }
        #方向（坦克方向）
        self.direction = tank.direction
        #位置
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        if self.direction == 'U':
            self.image = self.images[self.direction]
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2 + 2
            self.rect.top = tank.rect.top- self.rect.height
        elif self.direction == 'D':
            self.image = self.images[self.direction]
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width /2 + 4
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.image = self.images[self.direction]
            self.rect.left = tank.rect.left  - self.rect.width / 2 - 4
            self.rect.top = tank.rect.top + self.rect.height + 8
        elif self.direction == 'R':
            self.image = self.images[self.direction]
            self.rect.left = tank.rect.left + tank.rect.width / 2 + self.rect.width + 6
            self.rect.top = tank.rect.top + self.rect.height + 4
        #速度
        self.speed = 10
        #用来记录子弹是否活着
        self.live = True

    # 子弹移动方法
    def bulletMove(self):
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                #修改状态值
                self.live = False
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < MainGame.SCREEN_WIDTH :
                self.rect.left += self.speed
            else:
                self.live = False
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.live = False
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < MainGame.SCREEN_HEIGHT:
                self.rect.top += self.speed
            else:
                self.live = False

    # 子弹展示方法
    def displayBullet(self):
        MainGame.window.blit(self.image, self.rect)

    # 新增我方子弹碰撞敌方轻型坦克的方法
    def hitEnemyTank(self):
        for eTank in MainGame.EnemyTank_A_list:
            if pygame.sprite.collide_rect(eTank, self):
                #产生一个爆炸效果
                explode = Explode(eTank)
                #将爆炸效果加入到爆炸效果列表中
                MainGame.Explode_list.append(explode)
                self.live = False
                eTank.live = False
        for eTank in MainGame.EnemyTank_B_list:
            if pygame.sprite.collide_rect(eTank, self):
                #产生一个爆炸效果
                explode = Explode(eTank)
                #将爆炸效果加入到爆炸效果列表中
                MainGame.Explode_list.append(explode)
                self.live = False
                if eTank.hp <= 0:
                    eTank.live = False
                else:
                    eTank.hp -= 1

    # 新增子弹与我方坦克的碰撞的方法
    def  hitMyTank(self):
        if pygame.sprite.collide_rect(self, MainGame.TANK_P1):
            #产生爆炸效果，并加入到爆炸效果列表中
            explode = Explode(MainGame.TANK_P1)
            MainGame.Explode_list.append(explode)
            #修改子弹状态
            self.live = False
            #修改我方坦克状态
            MainGame.TANK_P1.live = False

    # 新增子弹与墙壁的碰撞
    def hitWall(self):
        for wall in MainGame.Wall_list:
            if pygame.sprite.collide_rect(self, wall):
                # 产生爆炸效果，并加入到爆炸效果列表中
                explode = Explode(wall)
                MainGame.Explode_list.append(explode)
                #修改子弹的live属性
                self.live = False
                wall.hp -= 1
                if wall.hp <= 0:
                    wall.live = False

    # 子弹与老巢的碰撞
    def hitHome(self):
        if pygame.sprite.collide_rect(self, MainGame.home):
            explode = Explode(MainGame.home)
            MainGame.Explode_list.append(explode)
            # 修改子弹的live属性
            self.live = False
            MainGame.home.hp -= 1
            if MainGame.home.hp <= 0:
                MainGame.home.live = False

class Explode():  # 爆炸效果类
    def __init__(self, item):
        self.images = [
            pygame.image.load('TankWar-master/images/boom/blast1.gif'),
            pygame.image.load('TankWar-master/images/boom/blast2.gif'),
            pygame.image.load('TankWar-master/images/boom/blast3.gif'),
            pygame.image.load('TankWar-master/images/boom/blast4.gif'),
            pygame.image.load('TankWar-master/images/boom/blast5.gif'),
            pygame.image.load('TankWar-master/images/boom/blast6.gif'),
            pygame.image.load('TankWar-master/images/boom/blast7.gif'),
            pygame.image.load('TankWar-master/images/boom/blast8.gif')
        ]
        self.rect = item.rect
        self.step = 0
        self.image = self.images[-1]
        self.rect.left = item.rect.left + 16
        self.rect.top = item.rect.top + 16
        self.live = True

    # 展示爆炸效果类
    def displayExplode(self):
        if self.step < len(self.images):
            MainGame.window.blit(self.image, self.rect)
            self.image = self.images[self.step]
            self.step += 1
        else:
            self.step =0
            self.live = False

class Wall_A():  # 墙壁类
    def __init__(self, left, top):
        self.image = pygame.image.load('TankWar-master/images/walls/1.png')
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        #用来判断墙壁是否是应该在窗口中展示
        self.live = True
        #用来记录墙壁的生命值
        self.hp = 1

    # 展示墙壁方法
    def displayWall(self):
        MainGame.window.blit(self.image, self.rect)

class Music():  # 音效类
    def __init__(self, filename):
        self.filename = filename
        #初始化混合器
        pygame.mixer.init()
        pygame.mixer.music.load(self.filename)

    # 开始播放音乐
    def play(self):
        pygame.mixer.music.play()

class Home():
    def __init__(self, left, top):
        self.image = pygame.image.load('resources/images/walls/5.png')
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.live = True
        self.hp = 1

    #展示方法
    def displayHome(self):
        MainGame.window.blit(self.image, self.rect)


MainGame().startGame()

