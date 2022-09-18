import time
import random
import pygame
from startGame import Startgame
from threading import Thread


class Basesprite(pygame.sprite.Sprite):
    """
    Basesprite类，是游戏中所有变化物体的底层父类
    """
    def __init__(self, image_name, screen):
        super().__init__()
        self.screen = screen
        self.direction = None
        self.speed = None
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()

    def update(self):
        # 根据方向移动
        self.old_x = self.rect.x
        self.old_y = self.rect.y
        if self.direction == Startgame.LEFT:
            self.rect.x -= self.speed
        elif self.direction == Startgame.RIGHT:
            self.rect.x += self.speed
        elif self.direction == Startgame.UP:
            self.rect.y -= self.speed
        elif self.direction == Startgame.DOWN:
            self.rect.y += self.speed


class Bullet(Basesprite):

    def __init__(self, image_name, screen):
        super().__init__(image_name, screen)
        self.speed = Startgame.BULLET_SPEED


class TankSprite(Basesprite):
    """
    ImageSprite类，Basesprite的子类，所有带图片的精灵的父类
    """
    def __init__(self, image_name, screen):
        super().__init__(image_name, screen)
        self.type = None
        self.bullets = pygame.sprite.Group()
        self.is_alive = True
        self.is_moving = False
        self.old_x = self.rect.x
        self.old_y = self.rect.y

    def shot(self):
        """
        射击类，坦克调用该类发射子弹
        :return:
        """

        # 把消失的子弹移除
        self.__remove_sprites()
        if not self.is_alive:
            return
        if len(self.bullets) >= 3:
            return
        if self.type == Startgame.HERO:
            music = Music(Startgame.FIRE_MUSIC)
            music.play()
        if self.type == Startgame.ENEMY and pygame.time.get_ticks() >= 5500:
            music = Music(Startgame.HIT_MUSIC)
            music.play()

        # 发射子弹
        bullet = Bullet(Startgame.BULLET_IMAGE_NAME, self.screen)
        bullet.direction = self.direction
        if self.direction == Startgame.LEFT:
            bullet.rect.right = self.rect.left
            bullet.rect.centery = self.rect.centery
        elif self.direction == Startgame.RIGHT:
            bullet.rect.left = self.rect.right
            bullet.rect.centery = self.rect.centery
        elif self.direction == Startgame.UP:
            bullet.rect.bottom = self.rect.top
            bullet.rect.centerx = self.rect.centerx
        elif self.direction == Startgame.DOWN:
            bullet.rect.top = self.rect.bottom
            bullet.rect.centerx = self.rect.centerx
        self.bullets.add(bullet)

    def move_out_wall(self, wall):
        if self.direction == Startgame.LEFT:
            self.rect.left = wall.rect.right + 2
        elif self.direction == Startgame.RIGHT:
            self.rect.right = wall.rect.left - 2
        elif self.direction == Startgame.UP:
            self.rect.top = wall.rect.bottom + 2
        elif self.direction == Startgame.DOWN  :
            self.rect.bottom = wall.rect.top - 2

    def __remove_sprites(self):
        """
        移除无用的子弹
        :return:
        """
        for bullet in self.bullets:
            if bullet.rect.bottom <= 0 or \
                    bullet.rect.top >= Startgame.SCREEN_RECT.bottom or \
                    bullet.rect.right <= 0 or \
                    bullet.rect.left >= Startgame.SCREEN_RECT.right:
                self.bullets.remove(bullet)
                bullet.kill()

    # 还原方法
    def stay(self):
        self.rect.x = self.old_x
        self.rect.y = self.old_y

    def update(self):
        if not self.is_alive:
            return
        super(TankSprite, self).update()

    def boom(self):
        pygame.mixer.music.load(Startgame.BOOM_MUSIC)
        pygame.mixer.music.play()
        for boom in Startgame.BOOMS:
            self.image = pygame.image.load(boom)
            time.sleep(0.05)
            self.screen.blit(self.image, self.rect)
        pygame.mixer.music.stop()
        super(TankSprite, self).kill()

    def kill(self):
        self.is_alive = False
        t = Thread(target=self.boom)
        t.start()


class Hero(TankSprite):
    def __init__(self, image_name, screen):
        super(Hero, self).__init__(image_name, screen)
        self.type = Startgame.HERO
        self.speed = Startgame.HERO_SPEED
        self.direction = Startgame.UP
        self.is_hit_wall = False

        # 初始化位置
        self.rect.centerx = Startgame.SCREEN_RECT.centerx - Startgame.BOX_RECT.width * 2
        self.rect.bottom = Startgame.SCREEN_RECT.bottom

        # 初始化音乐
        music =Music('TankWar-master/music/start.wav')
        music.play()


    def __turn(self):
        self.image = pygame.image.load(Startgame.HERO_IMAGES.get(self.direction))

    def hit_wall(self):
        if self.direction == Startgame.LEFT and self.rect.left <= 0 or \
            self.direction == Startgame.RIGHT and self.rect.right >= Startgame.SCREEN_RECT.right or \
            self.direction == Startgame.UP and self.rect.top <= 0 or \
                  self.direction == Startgame.DOWN and self.rect.bottom >= Startgame.SCREEN_RECT.bottom:
            self.is_hit_wall = True

    def update(self):
        if not self.is_hit_wall:
            super().update()
            self.__turn()

    def kill(self):
        self.is_alive = False
        self.boom()
        self.rect.centerx = Startgame.SCREEN_RECT.centerx - Startgame.BOX_RECT.width * 2
        self.rect.bottom = Startgame.SCREEN_RECT.bottom


class Enemy(TankSprite):

    def __init__(self, image_name, screen):
        super().__init__(image_name, screen)
        self.is_hit_wall = False
        self.type = Startgame.ENEMY
        self.speed = Startgame.ENEMY_SPEED
        self.direction = random.randint(0, 3)
        self.terminal = float(random.randint(40*2, 40*8))

        # 初始化位置
        self.rect.x = Startgame.SCREEN_RECT.width - Startgame.ENEMY_POSITION[1][Startgame.ENEMY_POSITION[0]] * Startgame.BOX_RECT.width * 5
        self.rect.top = Startgame.SCREEN_RECT.top
        Startgame.ENEMY_POSITION[0] += 1


    def random_turn(self):
        # 随机转向
        self.is_hit_wall = False
        directions = [i for i in range(4)]
        directions.remove(self.direction)
        self.direction = directions[random.randint(0, 2)]
        self.terminal = float(random.randint(40 * 2, 40 * 8))
        self.image = pygame.image.load(Startgame.ENEMY_IMAGES.get(self.direction))

    def random_shot(self):
        # 随机射击
        shot_flag = random.choice([True] + [False]*59)
        if shot_flag:
            super().shot()

    def hit_wall_turn(self):
        turn = False
        if self.direction == Startgame.LEFT and self.rect.left <= 0:
            turn = True
            self.rect.left = 2
        elif self.direction == Startgame.RIGHT and self.rect.right >= Startgame.SCREEN_RECT.right-1:
            turn = True
            self.rect.right = Startgame.SCREEN_RECT.right-2
        elif self.direction == Startgame.UP and self.rect.top <= 0:
            turn = True
            self.rect.top = 2
        elif self.direction == Startgame.DOWN and self.rect.bottom >= Startgame.SCREEN_RECT.bottom-1:
            turn = True
            self.rect.bottom = Startgame.SCREEN_RECT.bottom-2
        if turn:
            self.random_turn()

    def update(self):
        self.random_shot()
        if self.terminal <= 0:
            self.random_turn()
        else:
            super().update()
            # 碰撞调头
            self.terminal -= self.speed


class Wall(Basesprite):

    def __init__(self, image_name, screen):
        super().__init__(image_name, screen)
        self.type = None
        self.life = 2

    def update(self):
        pass

    def boom(self):
        pygame.mixer.music.load(Startgame.BOOM_MUSIC)
        pygame.mixer.music.play()
        for boom in Startgame.BOOMS:
            self.image = pygame.image.load(boom)
            time.sleep(0.06)
            self.screen.blit(self.image, self.rect)
        pygame.mixer.music.stop()
        super().kill()

    def kill(self):
        self.life -= 1
        if not self.life:
            t = Thread(target=self.boom)
            t.start()

class Music():
    def __init__(self, filename):
        self.filename =filename
        # 初始化混合器
        pygame.mixer.init()
        pygame.mixer.music.load(self.filename)

    def play(self):
        pygame.mixer.music.play()
