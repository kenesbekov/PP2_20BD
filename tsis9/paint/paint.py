import pygame
import math
import sys

pygame.init()

WHITE = (255, 255, 255)

WIDTH = 1000
HEIGHT = 800
BOARD_WIDTH = 800
board = pygame.Surface((800, HEIGHT))
board.fill(WHITE)
tool_bar = pygame.image.load('tool_bar.png')
font = pygame.font.SysFont("Verdana", 20)
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def draw_curve(surf, x1, y1, x2, y2, wid, color):
    pygame.draw.line(surf, color, (x1, y1), (x2, y2), width=wid)


def eraser(surf, x1, y1, x2, y2, wid):
    pygame.draw.line(surf, WHITE, (x1, y1), (x2, y2), width=10 + (10 * wid))


def draw_line(surf, x1, y1, x2, y2, wid, color):
    pygame.draw.line(surf, color, (x1, y1), (x2, y2), width=wid)


def draw_rectangle(surf, x1, y1, x2, y2, wid, color):
    pygame.draw.rect(surf, color,
                     pygame.Rect(min(x1, x2), min(y1, y2), max(x1, x2) - min(x1, x2), max(y1, y2) - min(y1, y2)),
                     width=wid)


def draw_square(surf, x1, y1, x2, y2, wid, color):
    x3_1 = math.copysign(min(abs(x2 - x1), abs(y2 - y1)), (x2 - x1))
    y3_1 = math.copysign(min(abs(x2 - x1), abs(y2 - y1)), (y2 - y1))
    x3_2 = min(abs(x2 - x1), abs(y2 - y1))
    y3_2 = min(abs(x2 - x1), abs(y2 - y1))

    pygame.draw.rect(surf, color, pygame.Rect(min(x1, x1 + x3_1), min(y1, y1 + y3_1), x3_2, y3_2), width=wid)


def draw_ellipse(surf, x1, y1, x2, y2, wid, color):
    pygame.draw.ellipse(surf, color,
                        pygame.Rect(min(x1, x2), min(y1, y2), max(x1, x2) - min(x1, x2), max(y1, y2) - min(y1, y2)),
                        width=wid)


def draw_circle(surf, x1, y1, x2, y2, wid, color):
    x3_1 = math.copysign(min(abs(x2 - x1), abs(y2 - y1)), (x2 - x1))
    y3_1 = math.copysign(min(abs(x2 - x1), abs(y2 - y1)), (y2 - y1))
    x3_2 = min(abs(x2 - x1), abs(y2 - y1))
    y3_2 = min(abs(x2 - x1), abs(y2 - y1))

    pygame.draw.ellipse(surf, color, pygame.Rect(min(x1, x1 + x3_1), min(y1, y1 + y3_1), x3_2, y3_2), width=wid)


click = False

def main():
    is_drawing = False
    shift_is_pressed = False

    red_value = green_value = blue_value = 0
    wid = 1
    tool = 1

    pen_button = pygame.Rect(825, 350, 75, 50)
    eraser_button = pygame.Rect(900, 350, 75, 50)
    line_button = pygame.Rect(830, 550, 140, 10)
    square_button = pygame.Rect(830, 450, 60, 60)
    circle_button = pygame.Rect(905, 450, 60, 60)
    save_button = pygame.Rect(825, 725, 150, 50)

    width_button = pygame.Rect(825, 25, 150, 50)
    red_button = pygame.Rect(825, 200, 150, 30)
    green_button = pygame.Rect(825, 230, 150, 30)
    blue_button = pygame.Rect(825, 260, 150, 30)

    color = (0, 0, 0)
    while True:
        pressed_mouse = pygame.mouse.get_pressed()
        color = (int(red_value), int(green_value), int(blue_value))
        mx, my = pygame.mouse.get_pos()

        if pen_button.collidepoint(mx, my):
            if click:
                tool = 1
        if eraser_button.collidepoint(mx, my):
            if click:
                tool = 2
        if line_button.collidepoint(mx, my):
            if click:
                tool = 3
        if square_button.collidepoint(mx, my):
            if click:
                tool = 4
        if circle_button.collidepoint(mx, my):
            if click:
                tool = 5
        if save_button.collidepoint(mx, my):
            if click:
                pygame.image.save(board, "image.png")

        click = False

        if pressed_mouse[0]:
            if width_button.collidepoint(mx, my):
                if wid < 10:
                    wid += 0.0001
            if red_button.collidepoint(mx, my):
                if red_value < 255:
                    red_value += 0.001
            if green_button.collidepoint(mx, my):
                if green_value < 255:
                    green_value += 0.001
            if blue_button.collidepoint(mx, my):
                if blue_value < 255:
                    blue_value += 0.001
        if pressed_mouse[2]:
            if width_button.collidepoint(mx, my):
                if wid > 2:
                    wid -= 0.001
            if red_button.collidepoint(mx, my):
                if red_value > 1:
                    red_value -= 0.001
            if green_button.collidepoint(mx, my):
                if green_value > 1:
                    green_value -= 0.001
            if blue_button.collidepoint(mx, my):
                if blue_value > 1:
                    blue_value -= 0.001

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    shift_is_pressed = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    shift_is_pressed = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
                x1, y1 = pygame.mouse.get_pos()

                if tool == 1 or tool == 2:
                    is_drawing = True

            if event.type == pygame.MOUSEBUTTONUP:
                wid = int(wid)
                if event.button == 1:
                    x2, y2 = pygame.mouse.get_pos()
                    if shift_is_pressed:
                        if tool == 3:
                            draw_line(board, x1, y1, x2, y2, wid, color)
                        if tool == 4:
                            draw_square(board, x1, y1, x2, y2, wid, color)
                        if tool == 5:
                            draw_circle(board, x1, y1, x2, y2, wid, color)
                    else:
                        if tool == 3:
                            draw_line(board, x1, y1, x2, y2, wid, color)
                        if tool == 4:
                            draw_rectangle(board, x1, y1, x2, y2, wid, color)
                        if tool == 5:
                            draw_ellipse(board, x1, y1, x2, y2, wid, color)
                    is_drawing = False
            if event.type == pygame.MOUSEMOTION and is_drawing:
                wid = int(wid)
                x2, y2 = pygame.mouse.get_pos()
                print(x1, y1, x2, y2)
                if tool == 1:
                    draw_curve(board, x1, y1, x2, y2, wid, color)
                elif tool == 2:
                    eraser(board, x1, y1, x2, y2, wid)
                x1, y1 = pygame.mouse.get_pos()

            screen.blit(board, (0, 0))
            screen.blit(tool_bar, (800, 0))

            width_text = font.render(str(int(wid)), True, WHITE)
            red_text = font.render(str(int(red_value)), True, WHITE)
            green_text = font.render(str(int(green_value)), True, WHITE)
            blue_text = font.render(str(int(blue_value)), True, WHITE)
            color_rect = pygame.Rect(850, 125, 100, 50)

            screen.blit(width_text, (930, 37))
            screen.blit(red_text, (930, 205))
            screen.blit(green_text, (930, 230))
            screen.blit(blue_text, (930, 262))
            pygame.draw.rect(screen, color, color_rect)
            pygame.draw.rect(screen, (0, 0, 0), line_button)

            pygame.display.flip()


main()
