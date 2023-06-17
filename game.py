# Import (modules)
import os
import random
from time import sleep


# Import (files)
from convenience import clear
from boards import createBoards


# Dice turn
def turnDice(name):
    for i in range(200):
        clear()
            
        print(f"{name}'s spin:")
        number = random.randint(1, 10)
        print(number)
    spun = number
    
    clear()
    print(f"{name} has spun: {spun}")
    return spun
        

# Determine highest
def starterPlayer(starters: list, starterNrs: list, playObjs, isStr: bool):
    for playObj in playObjs:
        if isStr:
            spunNumber = turnDice(name=playObj["name"])
            starters.append({"name": playObj["name"], "number": spunNumber})
        else:
            spunNumber = turnDice(name=playObj.name)
            starters.append({"name": playObj.name, "number": spunNumber})
            
        starterNrs.append(spunNumber)
        sleep(3)
        

# Filter highest
def starterFilter(userList: list, compare: list, addTo: list):
    for sub in userList:
        if sub["number"] == max(compare):
            addTo.append(sub)
        
        
# Main Game method
def Game(turns, maxTurns, playerObj, boardChoice, startingPrice, lastPlayer):
    # New Mesage
    clear()
    print("Let's get started. The highest spin will start.")
    sleep(2)
    
    # Create user lists
    starter = []
    starterNr = []
    
    starterPlayer(starters=starter, starterNrs=starterNr, playObjs=playerObj, isStr=False)

    global res
    res = []
    
    starterFilter(userList=starter, compare=starterNr, addTo=res)

    while len(res) != 1:
        clear()
        print("We have more than 1 starter, so let's spin again!")
        starterNr = []
        starter = []
        sleep(3)
        
        starterPlayer(starters=starter, starterNrs=starterNr, playObjs=res, isStr=True)

        res = []
        sleep(3)
        
        starterFilter(userList=starter, compare=starterNr, addTo=res)
        sleep(3)

    clear()
    print(f"Ok, look's like {res[0]['name']} is starting")

    sleep(10)
    