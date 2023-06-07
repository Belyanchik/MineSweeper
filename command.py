import random

import buttons

def placement(x, y): #создание цифр, окружающих мину
    for i in range(3):
        newx = x

        if(i == 0):
            newx -= 1
        elif(i == 2):
            newx += 1

        if(newx >= 0 and newx <= 9):
            if(i == 1):
                for j in range(2):
                    newy = y
                    if (j == 0):
                        newy -= 1
                    elif (j == 1):
                        newy += 1
                    if(newy >= 0 and newy <= 9):
                        if(place[newx][newy] != "X"):
                            place[newx][newy] += 1

            else:
                for j in range(3):
                    newy = y
                    if(j == 0):
                        newy -= 1
                    elif(j == 2):
                        newy += 1
                    if(newy >= 0 and newy <= 9):
                        if(place[newx][newy] != "X"):
                            place[newx][newy] += 1

def openEmpty(inpx, inpy): #открытие пустых клеток
    a = [[inpx, inpy]]
    b = []
    s = 0
    while a != []:
        s += 1
        x = a[0][0]
        y = a[0][1]
        if([x, y] not in b):
            if(place[x][y] == 0):
                for i in range(3):
                    newx = x
                    if(i == 0):
                        newx -= 1
                    elif(i == 2):
                        newx += 1

                    if(newx >= 0 and newx <= 9):
                        if(i == 1):
                            for j in range(2):
                                newy = y
                                if(j == 0):
                                    newy -= 1
                                elif(j == 1):
                                    newy += 1
                                if(newy >= 0 and newy <= 9 and [newx, newy] not in b):
                                    a.append([newx, newy])

                        else:
                            for j in range(3):
                                newy = y
                                if(j == 0):
                                    newy -= 1
                                elif(j == 2):
                                    newy += 1
                                if (newy >= 0 and newy <= 9 and [newx, newy] not in b):
                                    a.append([newx, newy])
            b.append(a[0])

        a.pop(0)
    for i in objects:
        if([i.plx, i.ply] in b):
            i.setOpen()

def setPlace(): #создание игрового поля
    global place
    place = []
    for i in range(10):
        place.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    for i in range(10):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        while(place[x][y] == "X"):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        place[x][y] = "X"
        placement(x, y)
    return place

def indexing(place): #создание игровых клеток (кнопок)
    global objects
    objects = []
    for i in range(10):
        for j in range(10):
            objects.append(buttons.Buttons(185 + 40 * i, 45 + 40 * j, place[j][i], j, i))
    return objects