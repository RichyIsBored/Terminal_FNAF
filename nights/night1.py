import time
import os
import random
import msvcrt


mainStage = ["🐻", "🐰", "🐔"]
leftHall = ["  ", "  "]
rightHall = ["  ", "  "]
killer = ["  "]

bonniePos = 0

door = ("🚪")
doorClosed = False
gameOver = False


def nightOneGraphics():
    print("Night1")

    while True:

 

        os.system("cls")
        print("|-------------------\n" 
            "|     |", "" ,mainStage[0], mainStage[1], mainStage[2]," "   "|\n"
            "|                  |\n"
            "|     --------------\n"
            "|",leftHall[0]," |            |\n"
            "|     |            |\n"
            "|     --------------\n" 
            "|          ",killer[0],"    |\n"
            "|     |            |\n"
            "|-------------------\n")
        time.sleep(2)


def bonnieLogic():
    global bonniePos, gameOver, mainStage, leftHall, killer

    if random.randint(1,4) == 1:
        if bonniePos == 0:
            bonniePos = bonniePos + 1
            mainStage[1] = "  "
            leftHall[0] = " "


def playNight1():
    global doorClosed, gameOver, bonniePos
    nightOneGraphics()

playNight1()