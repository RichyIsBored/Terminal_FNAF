import time
import os
import random
import msvcrt

#----Location Variables----#

mainStage = ["🐰", "🐻", "🐔"]
pirateCove = "🦊"


diningArea = ["  ", "  ", "  "]


leftHall = ["  ", "  "]
supplyCloset = "  "
leftDoor = ["  ", "  "]

rightHall = ["  ", "  "]
rightDoor = ["  ", "  "]

office = ["  "]


bonniePos = 0
bonnieMove = 0
bonnieRage = 2

door1 = ("🚪")
door2 = ("🚪")

door1Closed = False
door2Closed = False

gameTime = 12
lastTimeUpdate = time.time()

power = 100
powerDrainRate = 0
drainMultiply = 0.15

gameOver = False
gameWin = False


def nightOneGraphics():

    os.system("cls")
    print(f"| Time = {gameTime}AM | Power = {round(power)}% |\n\n"
"\n\n" \
""
f"             |‾‾‾‾‾‾‾|                                     \n" \
f"             |       | |‾‾‾‾‾‾‾‾‾‾‾‾‾‾|                    \n" \
f"              ‾‾‾‾|  | |  {mainStage[0]}  {mainStage[1]}  {mainStage[2]}  |                    \n" \
f"                  |  |_|    -    -    |_______             \n" \
f"           ___|‾‾‾‾    -              -       |            \n" \
f"          |               -        -          | |‾‾|       \n" \
f"           ‾‾‾|               --              |_|  |       \n" \
f"              |                                    |_|‾‾‾| \n" \
f"              |         []    []    []        |‾|        | \n" \
f"        ______|            {diningArea[1]}    {diningArea[0]}           | |  |‾|___| \n" \
f"       |      .         []    []    []        | |  |       \n" \
f"       | {pirateCove}  .                                | |  |_|‾‾‾| \n" \
f"       |  .                                   | |        | \n" \
f"       |_______           _________           | |__|‾|___| \n" \
f"               ‾‾‾‾‾|    |         |     |‾‾||‾             \n" \
f"           _____   |      |       |      | |  ‾‾‾‾‾|        \n" \
f"          |     |  |  {leftHall[0]}  |       |      | |       |        \n" \
f"          |     |__|      |       |      | |_______|                 \n" \
f"          |   {supplyCloset}          |       |      |                 \n" \
f"          |     |‾‾|      |  ___  |      |                 \n" \
f"          |     |  |      | |📺 | |      |                 \n" \
f"           ‾‾‾‾‾   |      |_|   |_|      |                 \n" \
f"                   |      {door1} {office[0]} {door2}       |                 \n" \
f"                   |      |‾|   |‾|      |                 \n" \
f"                   | {leftDoor[0]}   | |___| | {rightDoor[0]}   |                 \n" \
f"                    ‾‾‾‾‾‾         ‾‾‾‾‾‾" 
" \n\n") 
    print(powerDrainRate, bonnieMove)

nightOneGraphics()

def bonnieLogic():
    global bonniePos, gameOver, mainStage, leftHall, office, bonnieRage, bonnieMove, supplyCloset

    if random.randint(bonnieRage,20) == 20:
        
        bonnieMove += 1

        if bonnieMove == 3:
            bonnieMove = 0

            if bonniePos == 0:
                bonniePos = 1
                mainStage[0] = "  "
                diningArea[0] = "🐰"  


            elif bonniePos == 1:
                bonniePos = 2
                diningArea[0] = "  "  
                leftHall[0] = "🐰"

            elif bonniePos == 2:
                bonniePos = 3
                leftHall[0] = "  "
                supplyCloset = "🐰"

            elif bonniePos == 3:
                bonniePos = 4
                supplyCloset = "  "
                leftHall[0] = "🐰"   

            elif bonniePos == 4:
                bonniePos = 5
                leftHall[0] = "  "
                leftDoor[0] = "🐰"       

            elif bonniePos == 5:
                if door1Closed:
                    bonniePos = 0
                    mainStage[0] = "🐰"
                    leftDoor[0] = "  "                
                else:
                    bonniePos = 6
                    leftDoor[0] = "  "
                    office[0] = "🐰"
                    gameOver = True




def playNight1():
    global door1Closed, door2Closed, gameOver, bonniePos, mainStage, office, leftHall, rightHall, door1, door2, gameTime, lastTimeUpdate, power, gameWin, drainMultiply, powerDrainRate, bonnieMove

    gameOver = False

    gameTime = 12
    lastTimeUpdate = time.time()

    door1Closed = False
    door2Closed = False
    door1 = ("  ")
    door2 = ("  ")

    power = 100
    powerDrainRate = 0

    mainStage[0] = "🐰"
    bonniePos = 0
    bonnieMove = 0
    mainStage[1] = "🐻"
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
            
            elif key == "c":
                gameOver = True

            
        if door1Closed and door2Closed:
            powerDrainRate = drainMultiply * 6
        elif door1Closed or door2Closed:
            powerDrainRate = drainMultiply * 3
        else:
            powerDrainRate = drainMultiply
        

        power -=  powerDrainRate

        if power <= 0:
            gameOver = True


        nightOneGraphics()
        time.sleep(0.5)
        bonnieLogic()


        #Number of seconds each hour lasts \/
        if time.time() - lastTimeUpdate >= 30:
            gameTime += 1
            lastTimeUpdate = time.time()
            if gameTime > 12:
                gameTime = 1

        if gameTime == 6:
            gameOver = True
            gameWin = True

        nightOneGraphics()

    nightOneGraphics()
    time.sleep(3)
    os.system("cls")
    
    if gameWin == True:
        print("You Win!")
    else:
        print("You Lose :(")


