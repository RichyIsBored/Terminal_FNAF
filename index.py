import msvcrt, time, os

from nights.night1 import playNight1
from nights.night2 import playNight2

def mainMenu():

    selector = 2

    while True:
              
        os.system("cls")
        print("---------------\n|FNAF TERMINAL|\n---------------")
        for i in range(2):
            print("")
        if selector == 1:
            print("Night 1   <---")
            print("Night 2")
        elif selector == 2:
            print("Night 1")
            print("Night 2   <---")
        for i in range(2):
            print("")    

        if msvcrt.kbhit():
            choice = msvcrt.getch().decode()
            if choice == "w":
                selector = 1
            elif choice == "s":
                selector = 2
            elif choice == "\r" and selector == 1:
                night1()
            elif choice == "\r" and selector == 2:
                night2()

            else:
                os.system("cls")
                for i in range(8):
                    print("")
                print("BYE BYE!")
                for i in range(8):
                    print("")
                break            
        time.sleep(0.5)        

def night1():
    os.system("cls")

    playNight1()
    time.sleep(3)    

def night2():
    os.system("cls")
    playNight2()
    print("Brochacho theres nothing here yet, im sending you back")
    time.sleep(3)    

mainMenu()