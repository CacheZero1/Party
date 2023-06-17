import os
import time

system = 'clear' if os.name == "posix" else 'cls'


def newMSG():
    os.system(system)
    print("Welcome to PyParty!")


def createPlayers(playNr, playerNames):
    try:
        name = 0
        while name == 0 or name in playerNames:
            if name in playerNames:
                print("That name is already taken. Please choose another name!")
                time.sleep(3)
            newMSG()
            name = input(f"Please enter the name of Player {playNr + 1}: \n")

        playerClass = Player(name=name, number=playNr)

        return playerClass
    
    except KeyboardInterrupt:
        newMSG()
        print("Thanks for playing!")
        time.sleep(5)
        exit()

class Player():
    def __init__(self, name, number):
        self.name = name
        self.money = 0
        self.stars = 0
        self.turns = 0
        self.number = number
        self.boardPosN = 0
        self.boardPos = 0
