# Import (modules)
import os
import random
from time import sleep
import keyboard


# Import (files)
from convenience import clear
from boards import createBoards
from convenience import clear


# Vars
symbols = ["x", "o", "c", "z"]
startingPriceL = 0


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
        
        
# Starting spin
def startSpin(playerObj):
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

    sleep(5)

    return res[0]


# User filter
def userFilter(userList: list, compare: str, addTo: list, addToElse: list):
    for sub in userList:
        if sub.name == compare["name"]:
            addTo.append(sub)
        else:
            addToElse.append(sub)


# User Settings
def userIni(players: int, signs: list):
    newList = []
    count = 0
    for player in players:
        player.number = count
        player.sign = signs[count]
        newList.append(player)
        count += 1
    return newList
       

# Dice throw 
def diceThrow(name: str):
    while not keyboard.is_pressed('enter'):
        clear()
        print("Press 'Enter' to stop the dice!")
        num = random.randint(1, 10)
        print(num)
    clear()
    print(f"{name} rolled a {num}!")
    sleep(3)

    return num


# Money check
def checkMoney(player, price):
    availabe = player.money
    if availabe >= price:
        return True
    else:
        return False


# Blockage will ask
def blockageWill(name: str, price: int):
    clear()
    will = input(f"Hello {name}, you have the opportunity to cross the bridge for only {price} coins!\nDo you want to cross it? (Yes/No) (y/n)\n=> : \t")
    return will.lower().strip()
    


# Move on board
def boardMove(player, moves: int, boardFH: dict, boardSH: dict, blockadePrice: int):
    boardHalf1 = True if player.boardPosN == 0 else False
    for move in range(moves):
        player.boardPos += 1
        num = f"0{player.boardPos}" if player.boardPos > 9 else str(player.boardPos9)


        # First board side change
        if boardHalf1 and "dir" in boardFH["sp" + num].keys():
            if checkMoney(player=player, price=blockadePrice):
                will = blockageWill(name=player.name, price=blockadePrice)
                while will != 'n' and will != 'no' and will != 'y' and will != 'yes':
                    will = blockageWill(name=player.name, price=blockadePrice)
                
                if will == 'n' or will == 'no':
                    clear()
                    print("Ok, maybe next time!")
                    sleep(3)
                
                elif will == 'yes' or will == 'y':
                    #continue startingpricel



# Main Game method
def Game(turns, maxTurns, playerObject, boardChoice, startingPrice, lastPlayer):
    global startingPriceL
    startingPriceL = startingPrice
    startingPlayer = startSpin(playerObj=playerObject)
    playerOrder = []
    othersUsers = []
    userFilter(userList=playerObject, compare=startingPlayer, addTo=playerOrder, addToElse=othersUsers)
    playerOrder = playerOrder + othersUsers
    playerOrder = userIni(players=playerOrder, signs=symbols)

    boardFH, boardSH, boardGraphic = createBoards(board=boardChoice)

    while not turns <= maxTurns:
        for player in playerOrder:
            moveNum = diceThrow(player.name)
            boardMove(player, moveNum, boardFH=boardFH, boardSH=boardSH, blockadePrice=startingPriceL)