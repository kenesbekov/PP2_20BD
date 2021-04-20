import pygame
import json
import random
import os
import sys

pygame.init()

SIZE_BLOCK = 28
WIDTH_IN_BLOCK = 21 * 2  # multiply by 2, because we have 2 displays for each player
HEIGHT_IN_BLOCK = 15
MARGIN_TOP = 1 * SIZE_BLOCK
MARGIN_BOTTOM = 2 * SIZE_BLOCK
MARGIN = 0  # Distance in pixels between blocks
size = [SIZE_BLOCK * WIDTH_IN_BLOCK + 3 * SIZE_BLOCK + MARGIN * WIDTH_IN_BLOCK,
        SIZE_BLOCK * HEIGHT_IN_BLOCK + 2 * SIZE_BLOCK + MARGIN * HEIGHT_IN_BLOCK + MARGIN_TOP + MARGIN_BOTTOM]

BACKGROUND_COLOR = (162, 194, 95)
SNAKE_COLOR = (42, 50, 26)

background = pygame.image.load(os.path.join('backgrounds', 'background.png'))
menu_background = pygame.image.load(os.path.join('backgrounds', 'play_resume.png'))
levels_background = pygame.image.load(os.path.join('backgrounds', 'levels.png'))
player1_win_background = pygame.image.load(os.path.join('backgrounds', 'player1_win.png'))
player2_win_background = pygame.image.load(os.path.join('backgrounds', 'player2_win.png'))
wall_image = pygame.image.load(os.path.join('backgrounds', 'wall.png'))
food_image = pygame.image.load(os.path.join('backgrounds', 'food.png'))
snake_image = pygame.image.load(os.path.join('backgrounds', 'snake_block.png'))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
walls = []


class SnakeBlock:
    def __init__(self, color, blocks, score, dx, dy, a, b):
        # self.blocks = [(x - 2, y), (x - 1, y), (x, y)]  # starting length is 3
        self.blocks = blocks
        self.color = color
        self.score = score
        self.dx = dx
        self.dy = dy
        self.a = a
        self.b = b

    def draw(self):
        for block in self.blocks:
            draw_block(snake_image, block[0], block[1], 'image')


    def is_out(self):
        x, y = self.blocks[-1]
        return not (self.a <= x < self.b and 0 <= y < HEIGHT_IN_BLOCK)

    def move(self):
        x, y = self.blocks[-1]
        new_head = (x + self.dx, y + self.dy)

        if new_head in self.blocks or new_head in walls:
            pygame.mixer.Sound(os.path.join('sounds', 'lose_sound.wav')).play()
            if x < WIDTH_IN_BLOCK / 2:
                player_win_background = player2_win_background
            else:
                player_win_background = player1_win_background
            while True:
                screen.blit(player_win_background, (0, 0))
                pygame.display.flip()
                clock.tick(fps)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return 'return'

        self.blocks.append(new_head)
        self.blocks.pop(0)

    def eat(self, x, y):
        if (x, y) == self.blocks[-1]:
            self.score += 1
            self.blocks.insert(0, self.blocks[0])
            return True
        return False


def get_random_empty_block(snake_blocks, a, b):  # 0 - 19, 21 - 40
    x = random.randint(a, b)
    y = random.randint(0, HEIGHT_IN_BLOCK - 1)
    empty_block = [x, y]
    cnt = 1
    while tuple(empty_block) in walls or tuple(empty_block) in snake_blocks:
        empty_block[0] = random.randint(a, b)
        cnt += 1
        if cnt % 20 == 0:
            cnt = 1
            empty_block[1] = random.randint(0, HEIGHT_IN_BLOCK - 1)
    return empty_block


def draw_block(color, x, y, type):
    if type == 'color':
        pygame.draw.rect(screen, color, [SIZE_BLOCK + x * SIZE_BLOCK + MARGIN * x,
                                         MARGIN_TOP + SIZE_BLOCK + y * SIZE_BLOCK + MARGIN * y,
                                         SIZE_BLOCK,
                                         SIZE_BLOCK])
    elif type == 'image':
        screen.blit(color, ([SIZE_BLOCK + x * SIZE_BLOCK + MARGIN * x,
                                         MARGIN_TOP + SIZE_BLOCK + y * SIZE_BLOCK + MARGIN * y,
                                         SIZE_BLOCK,
                                         SIZE_BLOCK]))


snake1 = SnakeBlock(SNAKE_COLOR, [(9 - 2, 9), (9 - 1, 9), (9, 9)], 0, 1, 0, 0, WIDTH_IN_BLOCK // 2 - 1)
snake2 = SnakeBlock(SNAKE_COLOR, [(30 - 2, 9), (30 - 1, 9), (30, 9)], 0, 1, 0, WIDTH_IN_BLOCK // 2 + 1,
                    WIDTH_IN_BLOCK - 1)
food1 = get_random_empty_block(snake1.blocks, snake1.a, snake1.b)
food2 = get_random_empty_block(snake2.blocks, snake2.a, snake2.b)

all_info = {'snake1': {},
            'snake2': {},
            'walls': [],
            'food1': [],
            'food2': []
            }

speed_count, snake_speed = 0, 10  # higher speed gives fewer movements

click = False

def main_menu():
    while True:
        screen.blit(menu_background, (0, 0))

        mx, my = pygame.mouse.get_pos()

        button_play = pygame.Rect(200, 280, 320, 140)
        button_reload = pygame.Rect(700, 280, 400, 140)
        if button_play.collidepoint(mx, my):
            if click:
                choose_level()
        if button_reload.collidepoint(mx, my):
            if click:
                reload_game('state')

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(fps)

def game():
    global speed_count
    running = True
    while running:
        screen.blit(background, (0, 0))
        speed_count += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save_game()
                    running = False
                if event.key == pygame.K_w and snake1.dx != 0:
                    snake1.dx = 0
                    snake1.dy = -1
                elif event.key == pygame.K_s and snake1.dx != 0:
                    snake1.dx = 0
                    snake1.dy = 1
                elif event.key == pygame.K_a and snake1.dy != 0:
                    snake1.dx = -1
                    snake1.dy = 0
                elif event.key == pygame.K_d and snake1.dy != 0:
                    snake1.dx = 1
                    snake1.dy = 0

                elif event.key == pygame.K_UP and snake2.dx != 0:
                    snake2.dx = 0
                    snake2.dy = -1
                elif event.key == pygame.K_DOWN and snake2.dx != 0:
                    snake2.dx = 0
                    snake2.dy = 1
                elif event.key == pygame.K_LEFT and snake2.dy != 0:
                    snake2.dx = -1
                    snake2.dy = 0
                elif event.key == pygame.K_RIGHT and snake2.dy != 0:
                    snake2.dx = 1
                    snake2.dy = 0

        [draw_block(wall_image, *wall, 'image') for wall in walls]

        for i in ('1', '2'):  # do stuff for each snake
            snake = globals()['snake' + i]
            food = globals()['food' + i]
            if i == '1':
                player_win_background = globals()['player2_win_background']
            else:
                player_win_background = globals()['player1_win_background']

            if snake.is_out():
                pygame.mixer.Sound(os.path.join('sounds', 'lose_sound.wav')).play()
                while True:
                    screen.blit(player_win_background, (0, 0))
                    pygame.display.flip()
                    clock.tick(fps)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                return

            draw_block(food_image, *food, 'image')

            snake.draw()

            # speed doesn't depends on fps
            if not speed_count % snake_speed:
                if snake.eat(*food):
                    pygame.mixer.Sound(os.path.join('sounds', 'beep.wav')).play()
                    if i == '1':
                        global food1
                        food1 = get_random_empty_block(snake.blocks, snake.a, snake.b)
                    else:
                        global food2
                        food2 = get_random_empty_block(snake.blocks, snake.a, snake.b)
                if snake.move() == 'return':
                    return

        pygame.display.flip()
        clock.tick(fps)

def save_game():
    all_info['snake1'] = snake1.__dict__
    all_info['snake2'] = snake2.__dict__
    all_info['walls'] = walls
    all_info['food1'] = food1
    all_info['food2'] = food2
    with open(os.path.join('levels','game_state.txt'), 'w') as state_file:
        state_file.write(json.dumps(all_info))

def reload_game(mode):
    with open(os.path.join('levels', 'game_' + mode + '.txt'), 'r') as state_file:
        global snake1, snake2, walls, food1, food2
        all_info = json.loads(state_file.read())

        temp1 = all_info['snake1']
        blocks1 = temp1['blocks']
        color1 = temp1['color']
        score1 = temp1['score']
        dx1, dy1, a1, b1 = temp1['dx'], temp1['dy'], temp1['a'], temp1['b']
        snake1 = SnakeBlock(color1, blocks1, score1, dx1, dy1, a1, b1)
        temp2 = all_info['snake2']
        blocks2 = temp2['blocks']
        color2 = temp2['color']
        score2 = temp2['score']
        dx2, dy2, a2, b2 = temp2['dx'], temp2['dy'], temp2['a'], temp2['b']
        snake2 = SnakeBlock(color2, blocks2, score2, dx2, dy2, a2, b2)

        walls = all_info['walls']
        food1 = all_info['food1']
        food2 = all_info['food2']
    if mode == 'state':
        game()

def choose_level():
    click = False
    not_choosen = True
    mode = ''
    while not_choosen:
        screen.blit(levels_background, (0, 0))

        mx, my = pygame.mouse.get_pos()
        button_easy = pygame.Rect(180, 280, 250, 140)
        button_medium = pygame.Rect(480, 280, 320, 140)
        button_hard = pygame.Rect(860, 280, 250, 140)
        if button_easy.collidepoint(mx, my):
            if click:
                mode = 'easy'
                not_choosen = False
        if button_medium.collidepoint(mx, my):
            if click:
                mode = 'medium'
                not_choosen = False
        if button_hard.collidepoint(mx, my):
            if click:
                mode = 'hard'
                not_choosen = False

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(fps)
    load_level(mode)

def load_level(level):
    reload_game('start')
    with open(os.path.join('levels', 'level_' + level + '.txt'), 'r') as level_map:
        txt = level_map.read()
    i = 0
    for row in range(HEIGHT_IN_BLOCK):
        for column in range(WIDTH_IN_BLOCK + 1):
            # 0 - empty, 1 - wall
            if txt[i] == '1':
                walls.append((column, row))
            i += 1
        i += 1
    global food1, food2
    food1 = get_random_empty_block(snake1.blocks, snake1.a, snake1.b)
    food2 = get_random_empty_block(snake2.blocks, snake2.a, snake2.b)
    game()

main_menu()
