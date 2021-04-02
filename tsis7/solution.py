import pygame
import math


def graph_size():
    x_size, y_size = size[0], size[1]
    setxy = False
    while setxy == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                color[0], color[1] = color[1], color[0]
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                setxy = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                size[1] += 50
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                size[1] -= 50
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                size[0] += 50
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                size[0] -= 50
        screen.fill(color[0])
        width_text = pygame.font.SysFont('calibri', x_size // 25).render(f'Width of the Graph [← →]: {size[0]}', True, color[1])
        height_text = pygame.font.SysFont('calibri', x_size // 25).render(f'Height of the Graph [↓ ↑]: {size[1]}', True, color[1])
        screen.blit(width_text, (x_size // 5, y_size // 3))
        screen.blit(height_text, (x_size // 5, y_size // 2))
        pygame.display.update()
    set_sides = False
    while set_sides == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                color[0], color[1] = color[1], color[0]
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                set_sides = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                sides[0] += 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                sides[0] -= 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                sides[1] += 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                sides[1] -= 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                sides[2] += 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                sides[2] -= 1
        screen.fill(color[0])
        side_text = pygame.font.SysFont('calibri', x_size // 25).render(f'Free Space on the sides [← →]: {sides[0]}', True, color[1])
        up_text = pygame.font.SysFont('calibri', x_size // 25).render(f'Free Space on the top side [↓ ↑]: {sides[1]}', True, color[1])
        down_text = pygame.font.SysFont('calibri', x_size // 25).render(f'Free Space on the underside [q e]: {sides[2]}', True, color[1])
        screen.blit(side_text, (x_size // 6, y_size // 3))
        screen.blit(up_text, (x_size // 6, y_size // 2.2))
        screen.blit(down_text, (x_size // 6, y_size // 1.7))
        pygame.display.update()
    return True


def ox_graph():
    for i in (dx * side, dx * (side + 52)):
        pygame.draw.line(screen, color[1], (i, dy * up), (i, dy * (up + 36)), 2)
    curr_pi = -3
    for i in range(dx * (side + 2), dx * (side + 50) + 1, dx):
        if (i - dx * (side + 2)) % (dx * 8) == 0:
            if curr_pi == 0:
                pygame.draw.line(screen, color[1], (i, dy * up), (i, dy * (up + 36)), 2)
            elif curr_pi == 1:
                pygame.draw.line(screen, color[1], (i, dy * up), (i, dy * (up + 2)))
                pygame.draw.line(screen, color[1], (i, dy * (up + 6)), (i, dy * (up + 36)))

                # Drawing Sinx --- Cosx ---
                sinx_text = pygame.font.SysFont('timesnewroman', int(dx * 1.6 + dy / 6)).render('sin x', True, color[1])
                cosx_text = pygame.font.SysFont('timesnewroman', int(dx * 1.6 + dy / 6)).render('cos x', True, color[1])
                screen.blit(sinx_text, (i - dx, dy * (up + 2)))
                screen.blit(cosx_text, (i - dx * 1.3, dy * (up + 3.8)))

                pygame.draw.line(screen, RED, (i + dx * 2.8, dy * (up + 3.2)), (i + dx * 5.6, dy * (up + 3.2)), 2)
                cnt = 0
                prev_coordinate = i + dx * 2.8
                for coordinate_x in range(int(i + dx * 2.8 - dx / 5), int(i + dx * 5.6 + 1)):
                    if cnt == dx / 5:
                        prev_coordinate = coordinate_x
                    elif cnt == dx or coordinate_x == int(i + dx * 5.6):
                        pygame.draw.line(screen, BLUE, (prev_coordinate, dy * (up + 5)), (coordinate_x, dy * (up + 5)), 2)
                        cnt = 0
                    cnt += 1
            # Drawing Hot Keys
            elif curr_pi == 3:
                sinx_text = pygame.font.SysFont('timesnewroman', int(dx * 0.6 + dy / 10)).render('Press C or N', True, color[1])
                screen.blit(sinx_text, (i + dx * 2.3, dy * (up + 3)))

                pygame.draw.line(screen, color[1], (i, dy * up), (i, dy * (up + 36)))
            else:
                pygame.draw.line(screen, color[1], (i, dy * up), (i, dy * (up + 36)))

            # Drawing PI Values
            if curr_pi == 0:
                text = '0'
                x_symbol = pygame.font.SysFont('timesnewromanbolditalic', int(dx * 1.5)).render('X', True, color[1])
                screen.blit(x_symbol, (i - dx / 2, y - dy * (down - 2)))
            elif curr_pi == -1:
                text = '-π'
            elif curr_pi == 1:
                text = 'π'
            else:
                text = str(int(curr_pi)) + 'π'
            pi_value = pygame.font.SysFont('timesnewromanitalic', int(dx * 1.5)).render(text, True, color[1])
            screen.blit(pi_value, (i - dx / 2, y - dy * down))
            curr_pi += 0.5

        elif (i - dx * (side + 6)) % (dx * 8) == 0:
            pygame.draw.line(screen, color[1], (i, dy * up), (i, dy * (up + 1.5)))
            pygame.draw.line(screen, color[1], (i, dy * (up + 34.5)), (i, dy * (up + 36)))

            # Drawing PI/2 Values
            if abs(curr_pi) == 0.5:
                numerator_text = '  π'
            else:
                numerator_text = ' ' + str(int(abs(curr_pi * 2))) + 'π'
            numerator = pygame.font.SysFont('timesnewromanitalic', int(dx * 1.5)).render(numerator_text, True, color[1])
            divider = pygame.font.SysFont('timesnewromanitalic', int(dx * 1.5)).render('-—', True, color[1])
            denominator = pygame.font.SysFont('timesnewromanitalic', int(dx * 1.5)).render('  2', True, color[1])
            screen.blit(numerator, (i - dx * 4 / 3, y - dy * (down + 0.2)))
            screen.blit(divider, (i - dx * 4 / 3, y - dy * (down - 0.35)))
            screen.blit(denominator, (i - dx * 4 / 3, y - dy * (down - 1.2)))
            curr_pi += 0.5
        elif (i - dx * side) % (dx * 4) == 0:
            pygame.draw.line(screen, color[1], (i, dy * up), (i, dy * (up + 1)))
            pygame.draw.line(screen, color[1], (i, dy * (up + 35)), (i, dy * (up + 36)))
        elif (i - dx * (side + 1)) % (dx * 2) == 0:
            pygame.draw.line(screen, color[1], (i, dy * up), (i, dy * (up + 0.5)))
            pygame.draw.line(screen, color[1], (i, dy * (up + 35.5)), (i, dy * (up + 36)))


def oy_graph():
    for i in (dy * up, dy * (up + 36)):
        pygame.draw.line(screen, color[1], (dx * side, i), (dx * (side + 52), i), 2)
    curr_value = 1.00
    for i in range(dy * (up + 2), dy * (up + 34) + 1, dy):
        if (i - dy * (up + 2)) % (dy * 4) == 0:
            if curr_value == 0:
                pygame.draw.line(screen, color[1], (dx * side, i), (dx * (side + 52), i), 2)
            else:
                pygame.draw.line(screen, color[1], (dx * side, i), (dx * (side + 52), i))

            # Drawing Numeric Values
            if curr_value >= 0:
                text = ' ' + str(f'{curr_value:.2f}')
            else:
                text = str(f'{curr_value:.2f}')
            value = pygame.font.SysFont('timesnewromanitalic', int(dx * 1.5)).render(text, True, color[1])
            screen.blit(value, (dx * (side - 4), i - dy))
            curr_value -= 0.25
        elif (i - dy * up) % (dy * 4) == 0:
            pygame.draw.line(screen, color[1], (dx * side, i), (dx * (side + 1), i))
            pygame.draw.line(screen, color[1], (dx * (side + 51), i), (dx * (side + 52), i))
        elif (i - dy * (up + 3)) % (dy * 2) == 0:
            pygame.draw.line(screen, color[1], (dx * side, i), (dx * (side + 0.5), i))
            pygame.draw.line(screen, color[1], (dx * (side + 51.5), i), (dx * (side + 52), i))


def sinxcosx_graph():
    prev_sinx = (dx * (side + 2), dy * (up + 18))
    prev_cosx = [[0, 0], (dx * (side + 2), dy * (up + 34))] # (start drawing, start resting), starting drawing coordinates
    has_drown = False
    cnt = 0
    for i in range(dx * (side + 2), dx * (side + 50) + 1):
        radians = -3 * math.pi + (math.pi / 2) * (i - dx * (side + 2)) / (dx * 4)

        value_sinx = math.sin(radians)
        value_cosx = math.cos(radians)

        coordinate_y_sinx = dy * (up + 2) + (dy * 4) * (1.00 - value_sinx) / 0.25
        coordinate_y_cosx = dy * (up + 2) + (dy * 4) * (1.00 - value_cosx) / 0.25

        # Drawing SinX
        pygame.draw.aaline(screen, RED, prev_sinx, (i, coordinate_y_sinx), 2)
        prev_sinx = (i, coordinate_y_sinx)

        # Drawing CosX
        # dots for little parts
        if coordinate_y_cosx <= dy * (up + 7) or coordinate_y_cosx >= dy * (up + 29):
            if cnt == 0:
                prev_cosx[1] = (i, coordinate_y_cosx)
            elif cnt == 4:
                pygame.draw.aaline(screen, BLUE, prev_cosx[1], (i, coordinate_y_cosx), 2)
                cnt = -3
            cnt += 1
        # separated values
        else:
            cnt = 0
            if has_drown == False:
                prev_cosx[0][1] = coordinate_y_cosx

            # leaving white space
            if abs(coordinate_y_cosx - prev_cosx[0][1]) >= dy / 5:
                has_drown = False
                prev_cosx[0][0] = coordinate_y_cosx
                prev_cosx[1] = (i, coordinate_y_cosx)

            # drawing if length is large enough
            if abs(coordinate_y_cosx - prev_cosx[0][0]) >= dy * 0.8 and has_drown == False:
                pygame.draw.aaline(screen, BLUE, prev_cosx[1], (i, coordinate_y_cosx), 2)
                has_drown = True
                prev_cosx[0][1] = coordinate_y_cosx


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

color = [WHITE, BLACK]

print('Press "n" to switch to the Night Mode')

# Default
size = [1200, 800]
sides = [0, 0, 0]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SinCoS Python')
screen.fill(color[0])

get_size = False

pygame.init()

done = False
while not done:
    screen.fill(color[0])
    if get_size == False:
        get_size = graph_size()
        
        screen = pygame.display.set_mode(size)
        side, up, down = sides
        x, y = size

        # для оставления пустых мест под - Values, PI Values and X Symbol
        side += 4
        down += 4
        
        # длина мин.отрезков по оси Ох и Oy (52 секций по Ox и 36 по Oy)
        dx = x // (52 + side * 2)
        dy = y // (36 + up + down)
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                color[0], color[1] = color[1], color[0]
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                get_size = False
        
        ox_graph()
        oy_graph()
        sinxcosx_graph()

        pygame.display.update()
pygame.quit()
