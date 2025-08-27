import time
import os
import random
import msvcrt


mainStage = ["🐻", "🐰", "🐔"]
leftHall = ["  ", "  "]
rightHall = ["  ", "  "]
office = ["  "]

bonniePos = 0

door = ("🚪")
doorClosed = False
gameOver = False


def nightOneGraphics():
    print("Night1")

    os.system("cls")
    print("|-------------------\n" 
        "|     |", "" ,mainStage[0], mainStage[1], mainStage[2]," "   "|\n"
        "|                  |\n"
        "|     --------------\n"
        "|",leftHall[0]," |            |\n"
        "|     |            |\n"
        "|     --------------\n" 
        "|          ",office[0],"    |\n"
        "|     |            |\n"
        "|-------------------\n")
    time.sleep(2)



def bonnieLogic():
    global bonniePos, gameOver, mainStage, leftHall, office

    if random.randint(1,4) == 1:
        if bonniePos == 0:
            bonniePos = 1
            mainStage[1] = "  "
            leftHall[0] = "🐰"
        elif bonniePos == 1:
            if doorClosed:
                bonniePos = 0
                mainStage[1] = "🐰"
                leftHall[0] = "  "                
            else:
                bonniePos = 0
                leftHall[0] = "  "
                office[0] = "🐰"
                gameOver = True



def playNight1():
    global doorClosed, gameOver, bonniePos, mainStage, office, leftHall

    gameOver = False

    mainStage[0] = "🐻"
    mainStage[1] = "🐰"
    mainStage[2] = "🐔"

    for i in range(2):
        leftHall [i-1] = "  "

    office[0] = "  "


    nightOneGraphics()

    while not gameOver:
        bonnieLogic()
        nightOneGraphics()

    os.system("cls")
    print("You lose!")
