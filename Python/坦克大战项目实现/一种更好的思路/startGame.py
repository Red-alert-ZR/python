from pygame import Rect
import os

class Startgame:

    # 游戏设置
    FPS = 60
    GAME_NAME = "坦克大战"  #屏幕标题
    BOX_SIZE = 50
    BOX_RECT = Rect(0, 0, BOX_SIZE, BOX_SIZE)
    SCREEN_RECT = Rect(0, 0, BOX_SIZE * 20, BOX_SIZE * 15)
    SCREEN_COLOR = (0, 0, 0)

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
        [0, 0, 1, 0, 0, 1, 4, 4, 1, 1, 2, 1, 1, 4, 4, 1, 0, 0, 1, 0, ],
        [0, 0, 1, 0, 0, 1, 4, 4, 1, 1, 2, 1, 1, 4, 4, 1, 0, 0, 1, 0, ],
        [0, 0, 1, 0, 0, 1, 4, 4, 1, 1, 2, 1, 1, 4, 4, 1, 0, 0, 1, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, ],
        [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, ],
        [0, 0, 1, 3, 3, 3, 1, 0, 0, 1, 1, 1, 0, 0, 1, 3, 3, 3, 1, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, ],
    ]

    # 音频
    BOOM_MUSIC ="TankWar-master/music/bang.wav"
    START_MUSIC = "TankWar-master/music/start.wav"
    FIRE_MUSIC = "TankWar-master/music/fire.wav"
    HIT_MUSIC = "TankWar-master/music/hit.wav"



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
