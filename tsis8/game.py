import pygame, os
from pygame.locals import *
import random, time


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        global ENEMY_SPEED
        super().__init__()
        self.properties()
        
    def properties(self):
        global ENEMY_SPEED
        x = random.choice((95, 160, 235, 300))
        if x == 235 or x == 300:
            i = random.randint(1, 4)
            self.image = pygame.image.load(os.path.join('car_along', str(i) + '.png'))
            ENEMY_SPEED = ROAD_SPEED + random.randint(-3, -1)
        else:
            i = random.randint(1, 3)
            self.image = pygame.image.load(os.path.join('car_opposite', str(i) + '.png'))
            ENEMY_SPEED = ROAD_SPEED + random.randint(2, 5)
        self.image_width, self.image_height = self.image.get_size()
        self.surf = pygame.Surface((self.image_width - 6, self.image_height - 5))
        self.rect = self.surf.get_rect(center=(x, -self.image_height))

    def move(self):
        global SCORE_CNT
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE_CNT += 1
            self.properties()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join('car_player', 'player.png'))
        self.image_width, self.image_height = self.image.get_size()
        self.surf = pygame.Surface((self.image_width - 6, self.image_height - 5))
        self.rect = self.surf.get_rect(
            center=(random.randint(ROAD_X1 + self.image_width, ROAD_X2 - self.image_width), 500))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > ROAD_X1:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < ROAD_X2:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join('background', 'coin.png'))
        self.image_width, self.image_height = self.image.get_size()
        self.surf = pygame.Surface((self.image_width, self.image_height))
        self.rect = self.surf.get_rect(
            center=(random.randint(ROAD_X1 + self.image_width, ROAD_X2 - self.image_width), -self.image_height))

    def move(self):
        self.rect.move_ip(0, COIN_SPEED)


def main():
    global ROAD_SPEED, ENEMY_SPEED, COIN_SPEED, SCORE_CNT, COINS_CNT, P1, E1, y

    ROAD_SPEED = 5
    ENEMY_SPEED = ROAD_SPEED + random.randint(1, 5)
    COIN_SPEED = ROAD_SPEED + 1
    SCORE_CNT = 0
    COINS_CNT = 0

    P1 = Player()
    E1 = Enemy()

    enemies.add(E1)
    all_sprites.add(P1, E1)

    running = True

    while True:
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                ROAD_SPEED += 0.1
                COIN_SPEED = ROAD_SPEED + 1
            if event.type == COIN_SPAWN and running:
                C1 = Coins()
                coins.add(C1)
                all_sprites.add(C1)
            if event.type == SONG_END:
                pygame.mixer.music.play()
            if running == False:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    running = True
                    main()
            if event.type == pygame.QUIT:
                pygame.quit()

        if running:
            DISPLAYSURF.blit(background, (0, 0), (0, y, SCREEN_WIDTH, SCREEN_HEIGHT))
            scores_text = font.render(str(SCORE_CNT), True, BLACK)
            coins_text = font.render(str(COINS_CNT), True, BLACK)
            DISPLAYSURF.blit(scores_text, (10, 10))
            DISPLAYSURF.blit(score_sign, (40, 15))
            DISPLAYSURF.blit(coins_text, (10, 30))
            DISPLAYSURF.blit(coin_sign, (40, 35))

            for sprite in all_sprites:
                DISPLAYSURF.blit(sprite.image, sprite.rect)
                sprite.move()
            if pygame.sprite.spritecollideany(P1, coins):
                sound = pygame.mixer.Sound(os.path.join('sounds', 'coin.mp3'))
                sound.set_volume(0.5)
                sound.play()
                COINS_CNT += 1
                all_sprites.remove(C1)
                coins.empty()

            pygame.display.update()
            Fps.tick(FPS)

            y -= ROAD_SPEED
            if y <= ROAD_SPEED:
                y = SCREEN_HEIGHT

            if pygame.sprite.spritecollideany(P1, enemies):
                pygame.mixer.Sound(os.path.join('sounds', 'crash.wav')).play()
                DISPLAYSURF.blit(gameover, (0, 0))
                scores_text = font.render(str(SCORE_CNT), True, WHITE)
                coins_text = font.render(str(COINS_CNT), True, WHITE)
                DISPLAYSURF.blit(scores_text, (240, 240))
                DISPLAYSURF.blit(coins_text, (240, 290))
                pygame.display.update()
                for sprite in all_sprites:
                    sprite.kill()
                running = False


pygame.init()

FPS = 60
Fps = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont("Verdana", 20)

background = pygame.image.load(os.path.join('background', 'background.png'))
score_sign = pygame.image.load(os.path.join('background', 'score.png'))
coin_sign = pygame.image.load(os.path.join('background', 'dollar.png'))
gameover = pygame.image.load(os.path.join('background', 'gameover.png'))
pygame.mixer.music.load(os.path.join('sounds', 'background.mp3'))
pygame.mixer.music.play()

SCREEN_WIDTH, SCREEN_HEIGHT = background.get_size()
SCREEN_HEIGHT //= 2
# начало и конец дороги по ширине
ROAD_X1, ROAD_X2 = SCREEN_WIDTH * 0.175, SCREEN_WIDTH * 0.8125

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("8Bit Racer")

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

COIN_SPAWN = pygame.USEREVENT + 2
pygame.time.set_timer(COIN_SPAWN, 4000)

SONG_END = pygame.USEREVENT + 3
pygame.mixer.music.set_endevent(SONG_END)

y = SCREEN_HEIGHT  # для прорисовки анимированного бэкграунда

main()
