from pygame import Rect
import random
import os

class Startgame:

    # 游戏设置
    FPS = 60
    GAME_NAME = "坦克大战"  #屏幕标题
    BOX_SIZE = 50
    BOX_RECT = Rect(0, 0, BOX_SIZE, BOX_SIZE)
    SCREEN_RECT = Rect(0, 0, BOX_SIZE * 21, BOX_SIZE * 15)
    SCREEN_COLOR = (0, 0, 0)
    COLOR_R = (255, 255, 255)

    # 通用变量
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

    # 地图
    MAP_ONE = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, ],
        [0, 0, 1, 0, 0, 1, 3, 3, 1, 1, 2, 1, 1, 3, 3, 1, 0, 0, 1, 0, ],
        [0, 0, 1, 0, 0, 1, 3, 3, 1, 1, 2, 1, 1, 3, 3, 1, 0, 0, 1, 0, ],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, ],
        [0, 0, 1, 0, 0, 1, 4, 4, 1, 1, 0, 1, 1, 4, 4, 1, 0, 0, 1, 0, ],
        [0, 0, 1, 0, 0, 1, 4, 4, 1, 1, 0, 1, 1, 4, 4, 1, 0, 0, 1, 0, ],
        [0, 0, 1, 0, 0, 1, 4, 4, 1, 1, 2, 1, 1, 4, 4, 1, 0, 0, 1, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, ],
        [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, ],
        [0, 0, 1, 3, 3, 3, 1, 0, 0, 1, 1, 1, 0, 0, 1, 3, 3, 3, 1, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, ],
    ]

    # 音频
    BOOM_MUSIC ="resources/musics/boom.wav"
    START_MUSIC = "TankWar-master/music/start.wav"
    FIRE_MUSIC = "TankWar-master/music/fire.wav"
    HIT_MUSIC = "TankWar-master/music/hit.wav"
    VIC_MUSIC = "TankWar-master/music/victory.mp3"
    DEFEAT_MUSIC = "TankWar-master/music/天赐音画 - 超级玛丽失败音效 (节目).mp3"

    # 坦克类型
    HERO = 0
    ENEMY = 1

    # 我方坦克
    HERO_IMAGE_NAME = "resources/images/hero/hero1U.gif"
    HERO_IMAGES ={
        LEFT : "resources/images/hero/hero1L.gif",
        RIGHT : "resources/images/hero/hero1R.gif",
        UP : "resources/images/hero/hero1U.gif",
        DOWN : "resources/images/hero/hero1D.gif"
    }
    HERO_SPEED = 3
    HERO_LIVE = 3

    # 我方老巢
    BOSS_IMAGE = ""

    # 敌方坦克
    ENEMY_IMAGES ={
        LEFT : "resources/images/A_enemy/enemyL.png",
        RIGHT : "resources/images/A_enemy/enemyR.png",
        UP : "resources/images/A_enemy/enemyU.png",
        DOWN : "resources/images/A_enemy/enemyD.png"
    }
    ENEMY_COUNT = 5
    ENEMY_SPEED = random.uniform(1, 2)
    # 初始化位置
    ENEMY_POSITION = [0,[0, 1, 2, 3, 4, 5]]

    # 子弹
    BULLET_IMAGE_NAME = "resources/images/bullet/bullet.png"
    BULLET_RECT = Rect(0, 0, 5, 5)
    BULLET_SPEED = 5

    # 0表示空白、1表示红墙、2表示铁墙、3表示草、4表示海、5表示老巢
    RED_WALL = 1
    IRON_WALL = 2
    WEED_WALL = 3
    SEA_WALL = 4
    BOSS_WALL = 5
    WALLS = [
        f"resources/images/walls/{file}" for file in os.listdir("resources/images/walls")
    ]




    # 爆炸的图片
    BOOMS = [
        "resources/images/boom/" + file for file in os.listdir("resources/images/boom")
    ]
