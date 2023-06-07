import pygame

import config
import command

pygame.init()
win = pygame.display.set_mode((750, 500))

clock = pygame.time.Clock()
FPS = 30

#спрайты
cell = [pygame.image.load("sprites/game/cell0.png"), pygame.image.load("sprites/game/cell1.png")]
mine = pygame.image.load("sprites/game/mine.png")
flag = pygame.image.load("sprites/game/flag.png")
fon = pygame.image.load("sprites/logo/fons/fon_progect.png")

restartbtn = [pygame.image.load("sprites/button/restart/restart0.png"), pygame.image.load("sprites/button/restart/restart1.png")]
menubtn = [pygame.image.load("sprites/button/button_of_back/button_back_of_menu.png"), pygame.image.load("sprites/button/button_of_back/button_back_of_menu1.png")]

winanim = pygame.image.load("sprites/final_screen/win_for_anim.png")
loseanim = pygame.image.load("sprites/final_screen/lose_for_anim.png")

text = pygame.font.SysFont("Impact", 20)
textOfFlags = pygame.font.SysFont("Impact", 36)

def restart(pos, press):
    x = 70
    y = 200
    if(pos[0] > x and pos[0] < x + 84 and pos[1] > y and pos[1] < y + 28):
        win.blit(pygame.transform.scale(restartbtn[1], (84, 28)), (x, y))
        if(press[0] == True):
            config.config["game_run"] = False
    else:
        win.blit(pygame.transform.scale(restartbtn[0], (84, 28)), (x, y))

def menu(pos, press):
    x = 80
    y = 300
    if(pos[0] > x and pos[0] < x + 65 and pos[1] > y and pos[1] < y + 30):
        win.blit(pygame.transform.scale(menubtn[1], (65, 30)), (x, y))
        if(press[0] == True):
            config.config["scene"] = "menu"
            config.config["game_run"] = False
    else:
        win.blit(pygame.transform.scale(menubtn[0], (65, 30)), (x, y))

def winAnimation():
    s = 0
    while(s < 60):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.config["global_run"] = False
                config.config["game_run"] = False
                s = 59
        win.blit(winanim, (50, 10))
        s += 1
        pygame.display.update()

def loseAnimation():
    s = 0
    while(s < 60):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.config["global_run"] = False #закроет полностью программу
                config.config["game_run"] = False
                s = 59
        win.blit(loseanim, (50, 10))
        s += 1
        pygame.display.update()

def startGame(): #поместил всю игру в одну функцию
    place = command.setPlace() #генерация игрового поля
    objects = command.indexing(place) #создание игровых клеток (кнопок)
    repeat = 0
    config.config["game_run"] = True
    while(config.config["game_run"] == True): #цикл игры
        clock.tick(FPS)
        closed = 100 #счётчик закрытых клеток
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.config["global_run"] = False #закроет полностью программу
                config.config["game_run"] = False
                break

        win.fill((230,230,230))
        win.blit(fon, (0, 0))
        flagsCnt = 10

        press = pygame.mouse.get_pressed()

        if(press[0] == True or press[2] == True):
            repeat += 1
        else:
            repeat = 0
        pos = pygame.mouse.get_pos()
        for i in objects: #цикл работы со всеми кнопочками
            if(pos[0] > i.x and pos[0] < i.x + 32 and pos[1] > i.y and pos[1] < i.y + 32 and i.chk == False): #проверка, открывалась ли клетка ранее
                if(i.flag == True):
                    win.blit(cell[1], (i.x, i.y))
                    win.blit(flag, (i.x, i.y))
                    flagsCnt -= 1
                else:
                    win.blit(cell[1], (i.x, i.y))
                if(press[0] == True and repeat == 1 and i.flag == False): #открытие клетки
                    i.setOpen()
                    if(i.content == 0): #если пустая - запускает открытие пустых клеток
                        command.openEmpty(i.plx, i.ply)
                elif(press[2] == True and repeat == 1):
                    i.setFlag()
            elif(i.chk == True):
                closed -= 1
                if(i.content == "X"): #если мина
                    win.blit(mine, (i.x, i.y))
                    config.config["scene"] = "lose"
                    config.config["game_run"] = False
                    closed = 0

                elif(i.content != 0): #любой, кроме, пустой клетки и мины
                    win.blit(text.render(str(i.content), 1, config.config["colors"][i.content], (230,230,230)), (i.x + 12, i.y + 4))
            else: #просто закрытые клетки
                if(i.flag == True):
                    win.blit(cell[0], (i.x, i.y))
                    win.blit(flag, (i.x, i.y))
                    flagsCnt -= 1
                else:
                    win.blit(cell[0], (i.x, i.y))

        win.blit(pygame.transform.scale(flag, (64, 64)), (40, 50))
        win.blit(textOfFlags.render(str(flagsCnt), 1, (107, 50, 0), (230, 230, 230)), (120, 70))

        if(closed != 100):
            restart(pos, press)
        menu(pos, press)

        if(config.config["scene"] == "lose"):
            loseAnimation()
        if(closed == 10): #если закрытых клеток осталось 10 - победа
            config.config["game_run"] = False
            config.config["scene"] = "win"
            winAnimation()

        pygame.display.update()