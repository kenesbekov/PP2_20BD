import pygame
import math
import sys

pygame.init()

WHITE = (255, 255, 255)

WIDTH = 1000
HEIGHT = 800
BOARD_WIDTH = 1000
board = pygame.Surface((BOARD_WIDTH, HEIGHT))
board.fill(WHITE)
screen = pygame.display.set_mode((1000, 800))


def draw_curve(surf, x1, x2, y1, y2, wid, color):
    pygame.draw.line(surf, color, (x1, y1), (x2, y2), width=wid)


def draw_line(surf, x1, x2, y1, y2, wid, color):
    pygame.draw.line(surf, color, (x1, y1), (x2, y2), width=wid)


def eraser(surf, x1, y1, x2, y2, wid):
    pygame.draw.line(surf, WHITE, (x1, y1), (x2, y2), width=10 + (10 * wid))


def draw_rectangle(surf, x1, x2, y1, y2, wid, color):
    pygame.draw.rect(surf, color,
                     pygame.Rect(min(x1, x2), min(y1, y2), max(x1, x2) - min(x1, x2), max(y1, y2) - min(y1, y2)),
                     width=wid)


def draw_square(surf, x1, x2, y1, y2, wid, color):
    x3_1 = math.copysign(min(abs(x2 - x1), abs(y2 - y1)), (x2 - x1))
    y3_1 = math.copysign(min(abs(x2 - x1), abs(y2 - y1)), (y2 - y1))
    x3_2 = min(abs(x2 - x1), abs(y2 - y1))
    y3_2 = min(abs(x2 - x1), abs(y2 - y1))

    pygame.draw.rect(surf, color, pygame.Rect(min(x1, x1 + x3_1), min(y1, y1 + y3_1), x3_2, y3_2), width=wid)


def draw_ellipse(surf, x1, x2, y1, y2, wid, color):
    pygame.draw.ellipse(surf, color,
                        pygame.Rect(min(x1, x2), min(y1, y2), max(x1, x2) - min(x1, x2), max(y1, y2) - min(y1, y2)),
                        width=wid)


def draw_circle(surf, x1, x2, y1, y2, wid, color):
    x3_1 = math.copysign(min(abs(x2 - x1), abs(y2 - y1)), (x2 - x1))
    y3_1 = math.copysign(min(abs(x2 - x1), abs(y2 - y1)), (y2 - y1))
    x3_2 = min(abs(x2 - x1), abs(y2 - y1))
    y3_2 = min(abs(x2 - x1), abs(y2 - y1))

    pygame.draw.ellipse(surf, color, pygame.Rect(min(x1, x1 + x3_1), min(y1, y1 + y3_1), x3_2, y3_2), width=wid)


def main():
    is_drawing = False
    is_erasing = False
    shift_is_pressed = False

    color = (0, 0, 0)
    wid = 1
    tool = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    shift_is_pressed = True
                if event.key == pygame.K_l:
                    tool = 0
                if event.key == pygame.K_s:
                    tool = 1
                if event.key == pygame.K_c:
                    tool = 2
                if event.key == pygame.K_UP:
                    wid += 1
                if event.key == pygame.K_t:
                    pygame.image.save(board, "image.png")
                if event.key == pygame.K_DOWN:
                    if wid > 1:
                        wid -= 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    shift_is_pressed = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x1, y1 = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    x2, y2 = pygame.mouse.get_pos()
                    if shift_is_pressed:
                        if tool == 1:
                            draw_square(board, x1, y1, x2, y2, wid, color)
                        if tool == 2:
                            draw_circle(board, x1, y1, x2, y2, wid, color)
                    else:
                        if tool == 0:
                            draw_line(board, x1, y1, x2, y2, wid, color)
                        if tool == 1:
                            draw_rectangle(board, x1, y1, x2, y2, wid, color)
                        if tool == 2:
                            draw_ellipse(board, x1, y1, x2, y2, wid, color)
                    is_drawing = False
                    is_erasing = False
            if event.type == pygame.MOUSEMOTION and is_drawing:
                x2, y2 = pygame.mouse.get_pos()
                draw_curve(board, x1, y1, x2, y2, wid, color)
                x1, y1 = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION and is_erasing:
                x2, y2 = pygame.mouse.get_pos()
                eraser(board, x1, y1, x2, y2, wid)
                x1, y1 = pygame.mouse.get_pos()

            screen.blit(board, (0, 0))

            pygame.display.flip()

main()