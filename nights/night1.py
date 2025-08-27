import time
import os
import random
import msvcrt


mainStage = ["🐻", "🐰", "🐔"]

leftHall = ["  ", "  "]
leftDoor = ["  ", "  "]

rightHall = ["  ", "  "]
rightDoor = ["  ", "  "]

office = ["  "]

bonniePos = 0

door1 = ("  ")
door2 = ("  ")

door1Closed = False
door2Closed = False
gameOver = False



def nightOneGraphics():
    

    os.system("cls")
    print("        |------------------------|\n" 
        "        |     |", "" ,mainStage[0], mainStage[1], mainStage[2]," "   "|     |\n"
        "        |                        |\n"
        "        |     --------------     |\n"
        "        |",leftHall[0]," |            |     |\n"
        "        |     |            |     |\n"
        "        |     --------------     |\n" 
        "        |   ",door1,"  " ,office[0],"   ", door2,   "    |\n"
        "        |", leftDoor[0]," |            |     |\n"
        "        |------------------------|\n")
    


def bonnieLogic():
    global bonniePos, gameOver, mainStage, leftHall, office

    if random.randint(1,4) == 1:
        if bonniePos == 0:
            bonniePos = 1
            mainStage[1] = "  "
            leftHall[0] = "🐰"

        elif bonniePos == 1:
            bonniePos = 2
            leftHall[0] = "  "
            leftDoor[0] = "🐰"

        elif bonniePos == 2:
            if door1Closed:
                bonniePos = 0
                mainStage[1] = "🐰"
                leftDoor[0] = "  "                
            else:
                bonniePos = 0
                leftDoor[0] = "  "
                office[0] = "🐰"
                gameOver = True



def playNight1():
    global door1Closed, door2Closed, gameOver, bonniePos, mainStage, office, leftHall, rightHall, door1, door2

    gameOver = False

    mainStage[0] = "🐻"
    mainStage[1] = "🐰"
    mainStage[2] = "🐔"

    for i in range(2):
        leftHall [i-1] = "  "
        rightHall [i-1] = "  "


    office[0] = "  "




    while not gameOver:

        if msvcrt.kbhit():
            key = msvcrt.getch().decode()
            if key == 'a':
                door1Closed = not door1Closed
                if door1Closed == False:
                    door1 = "  "
                else:
                    door1 = "🚪"

            elif key == 'd':
                door2Closed = not door2Closed
                if door2Closed == False:
                    door2 = "  "
                else:
                    door2 = "🚪"


        nightOneGraphics()
        time.sleep(1)
        bonnieLogic()
        nightOneGraphics()

    nightOneGraphics()
    time.sleep(1)
    os.system("cls")
    print("You lose!")
