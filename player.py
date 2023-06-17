import os
import time
from convenience import newMSG

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
    def __init__(self, name: str, number: int):
        self.name: str = name
        self.money: int = 0
        self.stars: int = 0
        self.turns: int = 0
        self.number: int = number
        self.boardPosN: int = 0
        self.boardPos: int = 0
        self.sign: str = ""
