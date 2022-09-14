import pygame, time, random
from startGame import Startgame


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
        pass

    def __event_quit(self):
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                TankGame.__game_over()
                print('游戏结束')



    def run_game(self):
        self.__init_game()
        self.__create_sprite()
        while True and self.game_still:
            self.screen.fill(Startgame.SCREEN_COLOR)
            # 1、设置刷新帧率
            self.clock.tick(Startgame.FPS)
            # 2、事件监听
            self.__event_quit()
            # 5、更新显示
            pygame.display.update()
        self.__game_over()


    @staticmethod
    def __game_over():
        pygame.quit()
        exit()
