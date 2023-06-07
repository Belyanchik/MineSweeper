import pygame

import config

import webbrowser

pygame.init()
win = pygame.display.set_mode((750, 500))

programmes = [pygame.image.load("sprites/button/button_of_git/button_one/Belyanchik_first_programmer.png"),
                pygame.image.load("sprites/button/button_of_git/button_two/ArhanCrane_second_programmer.png")]

first_button = [pygame.image.load("sprites/button/button_of_git/button_one/first_programmer.png"),
                pygame.image.load("sprites/button/button_of_git/button_one/first_programmer1.png")]

second_button = [pygame.image.load("sprites/button/button_of_git/button_two/second_programmer.png"),
                 pygame.image.load("sprites/button/button_of_git/button_two/second_programmer1.png")]

back_button = [pygame.image.load("sprites/button/button_of_back/button_back.png"),
               pygame.image.load("sprites/button/button_of_back/button_back1.png")]

fon = (pygame.image.load("sprites/logo/fons/fon_progect.png"),
    pygame.image.load("sprites/logo/fons/fon_one.png"))


button_of_back_intake = back_button[0].get_rect(topleft=(600, 400))
button_of_back_take = back_button[1].get_rect(topleft=(600, 400))


def githubbtn(pos, press):

    win.blit(fon[0], (0, 0))
    win.blit(fon[1], (180, 260))
    win.blit(first_button[0], (160, 200))
    win.blit(second_button[0], (410, 200))
    win.blit(programmes[0], (167, 130))
    win.blit(programmes[1], (409, 142))
    win.blit(back_button[0], button_of_back_intake)



    x = 160
    y = 200
    if (pos[0] > x and pos[0] < x + 168 and pos[1] > y and pos[1] < y + 58):
        win.blit(first_button[1], (x, y))
        if (press == True):
            webbrowser.open_new("https://github.com/Belyanchik")

    else:
        win.blit(first_button[0], (x, y))

    x = 410
    y = 200
    if (pos[0] > x and pos[0] < x + 168 and pos[1] > y and pos[1] < y + 58):
        win.blit(second_button[1], (x, y))
        if (press == True):
            webbrowser.open_new("https://github.com/ArhanCrane")
    else:
        win.blit(second_button[0], (x, y))

    if button_of_back_intake.collidepoint(pos):
        win.blit(back_button[1], button_of_back_take)
    if button_of_back_intake.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
        config.config["scene"] = "menu"

    pygame.display.update()