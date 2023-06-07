import random

def placement(x, y):
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

def open(inpx, inpy):
    a = [[inpx, inpy]]
    b = []
    while a != []:
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
        placeforgame[x][y] = place[x][y]
        print("a", a)
        print("b", b)

place = []
for i in range(10):
    place.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

placeforgame = []
for i in range(10):
    placeforgame.append(["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"])

for i in range(10):
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    while(place[x][y] == "X"):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    place[x][y] = "X"
    placement(x, y)

print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in placeforgame]))
game = True
while(game == True):
    inpx = int(input("Строка: "))
    inpx = inpx - 1
    if(inpx >= 0 and inpx <= 9):
        inpy = int(input("Столбец: "))
        inpy = inpy - 1
        if(inpy >= 0 and inpy <= 9):
            this = place[inpx][inpy]
            placeforgame[inpx][inpy] = this
            if(this == "X"):
                game = False
            elif(this == 0):
                open(inpx, inpy)
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in placeforgame]))