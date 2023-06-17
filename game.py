from boards import createBoards
import os
import random
import time


system = 'clear' if os.name == "posix" else 'cls'


def turnDice(name):
    for i in range(200):
        os.system(system)
            
        print(f"{name}'s spin:")
        number = random.randint(1, 10)
        print(number)
    spun = number
    
    os.system(system)
    print(f"{name} has spun: {spun}")
    return spun
        



def Game(turns, maxTurns, playerObj, boardChoice, startingPrice, lastPlayer):
    os.system(system)
    print("Let's get started. The highest spin will start.")
    time.sleep(2)
    starter = []
    starterNr = []
    for players in playerObj:
        spunNumber = turnDice(name=players.name)
        starter.append({"name": players.name, "number": spunNumber})
        starterNr.append(spunNumber)
        time.sleep(3)

    global res
    res = []
    
    for sub in starter:
        if sub["number"] == max(starterNr):
            res.append(sub)

    while len(res) != 1:
        os.system(system)
        print("We have more than 1 starter, so let's spin again!")
        starterNr = []
        starter = []
        time.sleep(3)
        for sub in res:
            spunNumber = turnDice(name=sub["name"])
            starter.append({"name": sub["name"], "number": spunNumber})
            starterNr.append(spunNumber)
            time.sleep(3)

        res = []
        time.sleep(3)
        
        for sub in starter:
            if sub["number"] == max(starterNr):
                res.append(sub)
        time.sleep(3)

    os.system(system)
    print(f"Ok, look's like {res[0]['name']} is starting")

    time.sleep(10)
    