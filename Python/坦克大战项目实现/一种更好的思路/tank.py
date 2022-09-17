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
        self.hero = Hero(Startgame.HERO_IMAGE_NAME, self.screen)
        self.enemies = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for i in range(Startgame.ENEMY_COUNT):
            direction = random.randint(0, 3)
            enemy = Enemy(Startgame.ENEMY_IMAGES[direction], self.screen)
            enemy.direction = direction
            self.enemies.add(enemy)
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

    def __check_keydown(self, event):
        """检查按下按钮的事件"""
        if event.key == pygame.K_LEFT:
            # 按下左键
            self.hero.direction = Startgame.LEFT
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_RIGHT:
            # 按下右键
            self.hero.direction = Startgame.RIGHT
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_UP:
            # 按下上键
            self.hero.direction = Startgame.UP
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_DOWN:
            # 按下下键
            self.hero.direction = Startgame.DOWN
            self.hero.is_moving = True
            self.hero.is_hit_wall = False
        elif event.key == pygame.K_SPACE:
            # 坦克发射子弹
            self.hero.shot()

    def __check_keyup(self, event):
        """检查松开按钮的事件"""
        if event.key == pygame.K_LEFT:
            # 松开左键
            self.hero.direction = Startgame.LEFT
            self.hero.is_moving = False
        elif event.key == pygame.K_RIGHT:
            # 松开右键
            self.hero.direction = Startgame.RIGHT
            self.hero.is_moving = False
        elif event.key == pygame.K_UP:
            # 松开上键
            self.hero.direction = Startgame.UP
            self.hero.is_moving = False
        elif event.key == pygame.K_DOWN:
            # 松开下键
            self.hero.direction = Startgame.DOWN
            self.hero.is_moving = False

    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                TankGame.__game_over()
                print('游戏结束')
            elif event.type == pygame.KEYDOWN:
                TankGame.__check_keydown(self, event)
            elif event.type == pygame.KEYUP:
                TankGame.__check_keyup(self, event)

    def __check_collide(self):
        # 保证坦克不移出屏幕
        self.hero.hit_wall()
        #for enemy in self.enemies:
            #enemy.hit_wall_turn()

        # 子弹击中墙
        for wall in self.walls:
            # 我方坦克子弹击中墙
            for bullet in self.hero.bullets:
                if pygame.sprite.collide_rect(wall, bullet):
                    if wall.type == Startgame.RED_WALL:
                        wall.kill()
                        bullet.kill()
                    elif wall.type == Startgame.BOSS_WALL:
                        self.game_still = False
                    elif wall.type == Startgame.IRON_WALL:
                        bullet.kill()
            # 敌方坦克击中墙
            for enemy in self.enemies:
                for bullet in enemy.bullets:
                    if pygame.sprite.collide_rect(wall, bullet):
                        if wall.type == Startgame.RED_WALL:
                            wall.kill()
                            bullet.kill()
                        elif wall.type == Startgame.BOSS_WALL:
                            self.game_still = False
                        elif wall.type == Startgame.IRON_WALL:
                            bullet.kill()



            # 我方坦克撞墙
            if pygame.sprite.collide_rect(self.hero, wall):
                # 不可穿越墙
                if wall.type == Startgame.RED_WALL or wall.type == Startgame.IRON_WALL or wall.type == Startgame.BOSS_WALL:
                    self.hero.is_hit_wall = True
                    # 移出墙内
                    self.hero.move_out_wall(wall)

            # 敌方坦克撞墙
            for enemy in self.enemies:
                if pygame.sprite.collide_rect(wall, enemy):
                    if wall.type == Startgame.RED_WALL or wall.type == Startgame.IRON_WALL or wall.type == Startgame.BOSS_WALL:
                        enemy.move_out_wall(wall)
                        enemy.random_turn()

        # 子弹击中，敌方坦克碰撞，敌我坦克碰撞
        pygame.sprite.groupcollide(self.hero.bullets, self.enemies, True, True)
        # 敌方子弹击中我方
        for enemy in self.enemies:
            for bullet in enemy.bullets:
                if pygame.sprite.collide_rect(self.hero, bullet):
                    bullet.kill()
                    self.hero.kill()

    def __update_sprites(self):
        if self.hero.is_moving:
            self.hero.update()
        self.hero.bullets.update()
        self.walls.update()
        self.hero.bullets.draw(self.screen)
        self.enemies.update()
        for enemy in self.enemies:
            enemy.bullets.update()
            enemy.bullets.draw(self.screen)
        self.enemies.draw(self.screen)
        self.hero.bullets.draw(self.screen)
        self.screen.blit(self.hero.image, self.hero.rect)
        self.walls.draw(self.screen)


    def run_game(self):
        self.__init_game()
        self.__create_sprite()
        while True and self.game_still:
            self.screen.fill(Startgame.SCREEN_COLOR)
            # 1、设置刷新帧率
            self.clock.tick(Startgame.FPS)
            # 2、事件监听
            self.__event_handler()
            # 3、碰撞检测
            self.__check_collide()
            # 4、更新、绘制精灵、经理组
            self.__update_sprites()
            # 5、更新显示
            pygame.display.update()
        self.__game_over()



    @staticmethod
    def __game_over():
        pygame.quit()
        exit()
