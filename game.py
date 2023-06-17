from boards import createBoards
import os
import random
import time


system = os.name


def turnDice(name):
    for i in range(200):
        if system == "posix":
            os.system('clear')
        elif system in ("nt", "dos", "ce"):
            os.system('CLS')
            
        print(f"{name}'s spin:")
        number = random.randint(1, 10)
        print(number)
    spun = number
    if system == "posix":
        os.system('clear')
    elif system in ("nt", "dos", "ce"):
        os.system('CLS')
    print(f"{name} has spun: {spun}")
    return spun
        



def Game(turns, maxTurns, playerObj, boardChoice, startingPrice, lastPlayer):
    if system == "posix":
        os.system('clear')
    elif system in ("nt", "dos", "ce"):
        os.system('CLS')
    print("Let's get started. The highest spin will start.")
    time.sleep(2)
    starter = []
    starterNr = []
    for players in playerObj:
        spunNumber = turnDice(name=players.name)
        starter.append({"name": players.name, "number": spunNumber})
        starterNr.append(spunNumber)
        time.sleep(3)

    res = []
    
    for sub in starter:
        if sub["number"] == max(starterNr):
            res.append(sub)

    print(res)
    time.sleep(10)
    