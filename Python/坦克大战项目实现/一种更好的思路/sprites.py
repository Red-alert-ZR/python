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
        if self.direction == Startgame.LEFT:
            self.rect.x -= self.speed
        elif self.direction == Startgame.RIGHT:
            self.rect.x += self.speed
        elif self.direction == Startgame.UP:
            self.rect.y -= self.speed
        elif self.direction == Startgame.DOWN:
            self.rect.y += self.speed

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
            pygame.mixer.music.load(Startgame.FIRE_MUSIC)
            pygame.mixer.music.play()

        # 发射子弹
        bullet = Bullet()
        pass

    def move_out_wall(self, wall):
        if self.direction == Startgame.LEFT:
            self.rect.left = wall.rect.right + 2
        elif self.direction == Startgame.RIGHT:
            self.rect.right = wall.rect.left - 2
        elif self.direction == Startgame.LEFT:
            self.rect.top = wall.rect.bottom + 2
        elif self.direction == Startgame.LEFT:
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

    def update(self):
        if not self.is_alive:
            return
        super(TankSprite, self).update()

    def boom(self):
        pygame.mixer.music.load(Startgame.BOOM_MUSIC)
        pygame.game.mixer.music.play()
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
        self.speed = Startgame.HERO_SPEED * 4 ##
        self.direction = Startgame.UP
        self.is_hit_wall = False

        # 初始化未知
        self.rect.centerx = Startgame.SCREEN_RECT.centerx - Startgame.BOX_RECT.width * 2
        self.rect.bottom = Startgame.SCREEN_RECT.bottom

    def __turn(self):
        self.image = pygame.image.load(Startgame.HERO_IMAGES.get(self.direction))

    def hit_wall(self):
        if self.direction == Startgame.LEFT and self.rect.left >= 0 or \
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


class Wall(Basesprite):

    def __init__(self, image_name, screen):
        super().__init__(image_name, screen)
        self.type = None
        self.life = 2

    def update(self):
        pass

    def boom(self):
        pygame.mixer.music.load(Startgame.BOOM_MUSIC)
        pygame.game.mixer.music.play()
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
