from pygame import Rect
import os

class Startgame:

    # 游戏设置
    FPS = 60
    GAME_NAME = "坦克大战"  #屏幕标题
    BOX_SIZE = 50
    BOX_RECT = Rect(0, 0, BOX_SIZE, BOX_SIZE)
    SCREEN_RECT = Rect(0, 0, BOX_SIZE * 20, BOX_SIZE * 15)
    SCREEN_COLOR = (51, 76, 117)


