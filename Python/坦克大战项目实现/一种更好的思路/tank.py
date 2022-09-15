import pygame
from sprites import *


class TankGame():

    def __init__(self):
        self.screen = pygame.display.set_mode(Startgame.SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.game_still = True
        self.hero = None
        self.enemies = None
        self.enemy_bullets = None
        self.walls = None


    @staticmethod
    def __init_game():
        """
        初始化游戏设置
        :return:
        """
        pygame.init()
        pygame.display.set_caption(Startgame.GAME_NAME)
        pygame.mixer.init()

    def __create_sprite(self):
        self.walls = pygame.sprite.Group()
        self.__draw_map()

    def __draw_map(self):
        """
        绘制地图
        """
        for y in range(len(Startgame.MAP_ONE)):
            for x in range(len(Startgame.MAP_ONE[y])):
                if Startgame.MAP_ONE[y][x] == 0:
                    continue
                wall = Wall(Startgame.WALLS[Startgame.MAP_ONE[y][x]], self.screen)
                wall.rect.x = x * Startgame.BOX_SIZE
                wall.rect.y = y * Startgame.BOX_SIZE
                if Startgame.MAP_ONE[y][x] == Startgame.RED_WALL:
                    wall.type = Startgame.RED_WALL
                elif Startgame.MAP_ONE[y][x] ==Startgame.IRON_WALL:
                    wall.type = Startgame.IRON_WALL
                elif Startgame.MAP_ONE[y][x] ==Startgame.WEED_WALL:
                    wall.type = Startgame.WEED_WALL
                elif Startgame.MAP_ONE[y][x] ==Startgame.SEA_WALL:
                    wall.type = Startgame.SEA_WALL
                elif Startgame.MAP_ONE[y][x] ==Startgame.BOSS_WALL:
                    wall.type = Startgame.BOSS_WALL
                    wall.life = 1
                self.walls.add(wall)


    def __event_quit(self):
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                TankGame.__game_over()
                print('游戏结束')

    def __update_sprites(self):
        self.walls.update()
        self.walls.draw(self.screen)


    def run_game(self):
        self.__init_game()
        self.__create_sprite()
        while True and self.game_still:
            self.screen.fill(Startgame.SCREEN_COLOR)
            # 1、设置刷新帧率
            self.clock.tick(Startgame.FPS)
            # 2、事件监听
            self.__event_quit()
            # 4、更新、绘制精灵、经理组
            self.__update_sprites()
            # 5、更新显示
            pygame.display.update()
        self.__game_over()


    @staticmethod
    def __game_over():
        pygame.quit()
        exit()
