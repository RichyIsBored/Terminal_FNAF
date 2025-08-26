
def mainMenu():

    selector = 1
    while True:
              
        print("\x1b[2J")
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

        choice = input("")
        if choice == "w":
            selector = 1
        elif choice == "s":
            selector = 2
        else:
            print("\x1b[2J")
            print("BYE BYE!")
            for i in range(8):
                print("")
            break            

mainMenu()