# Import (modules)
import os
import random
from time import sleep
import keyboard
from colorama import Back, Fore, Style


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
   
   
# Ruby will ask 
def rubyWill(name: str):
    clear()
    will = input(f"Hello {name}, you have the opportunity to buy a ruby! Do you want to buy one for 30 coins? (Yes/No) (y/n)\n=> : \t")
    return will.lower().strip()


# Chance
def chanceSpin():
    signs = ["-", "+"]
    while not keyboard.is_pressed('enter'):
        clear()
        sign = random.choice(signs)
        print(sign)
        
    while not keyboard.is_pressed('enter'):
        clear()
        money = random.choice(1, 100)
        print(sign + money)
        
    if sign == "+":
        return money
    else:
        return -money


# Move on board
def boardMove(player, moves: int, boardFH: dict, boardSH: dict, blockadePrice: int):
    boardHalf1 = True if player.boardPosN == 0 else False
    for move in range(moves):
        player.boardPos += 1
        num = f"0{player.boardPos}" if player.boardPos > 9 else str(player.boardPos)


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
                    player.money -= startingPriceL
                    startingPriceL += 1
                    player.boardPosN += boardFH["sp" + num]["dir"]
                    player.boardPos = 13 if player.boardPos == 3 else 23
                    clear()
                    print("You have crossed the blockade and the price has increased!")
                    sleep(3)
                    
                    
        if not boardHalf1 and "dir" in boardSH["sp" + num].keys():
            if checkMoney(player=player, price=blockadePrice):
                will = blockageWill(name=player.name, price=blockadePrice)
                while will != 'n' and will != 'no' and will != 'y' and will != 'yes':
                    will = blockageWill(name=player.name, price=blockadePrice)
                
                if will == 'n' or will == 'no':
                    clear()
                    print("Ok, maybe next time!")
                    sleep(3)
                
                elif will == 'yes' or will == 'y':
                    player.money -= startingPriceL
                    startingPriceL += 1
                    player.boardPosN += boardFH["sp" + num]["dir"]
                    player.boardPos = 3 if player.boardPos == 13 else 5
                    clear()
                    print("You have crossed the blockade and the price has increased!")
                    sleep(3)
                    
                    
        # Buy star
        if boardHalf1 and boardFH["sp" + num]["spec"] == "star" or not boardHalf1 and boardSH["sp" + num]["spec"] == "star":
            if checkMoney(player=player, price=30):
                will = rubyWill(name=player.name)
                while will != 'n' and will != 'no' and will != 'y' and will != 'yes':
                    will = rubyWill(name=player.name)
                    
                if will == 'n' or will == 'no':
                    clear()
                    print("Strange, but ok!")
                    sleep(3)
                    
                elif will == 'yes' or will == 'y':
                    player.money -= 30
                    clear()
                    print("A ruby has been added to your account!")
                    player.stars += 1
                    sleep(3)
                    
                    
            else:
                clear()
                print("You sadly don't have enough coins to buy a ruby, better luck next time!")
                sleep(3)
                
    if boardHalf1 and player.boardPos > 12:
        player.boardPos -= 12
    elif not boardHalf1 and player.boardPos > 24:
        player.boardPos -= 12    
         
    num = f"0{player.boardPos}" if player.boardPos > 9 else str(player.boardPos)       
    if boardHalf1 and boardFH["sp" + num]["spec"] == "luck" or boardHalf1 and boardFH["sp" + num]["spec"] == "unluck" or not boardHalf1 and boardSH["sp" + num]["spec"] == "luckExtra" or not boardHalf1 and boardSH["sp" + num]["spec"] == "unluckExtra":
        addMoney = random.choice(boardFH["sp" + num]["bonus"]) if boardHalf1 else random.choice(boardSH["sp" + num]["bonus"])
        if addMoney > 0:
            clear()
            print(f"{addMoney} coins have been added to your balance!")
        else:
            clear()
            print(f"{addMoney} coins have been deducted from your balance!")
            
    elif boardHalf1 and boardFH["sp" + num]["spec"] == "chance" or not boardHalf1 and boardSH["sp" + num]["spec"] == "chance":
        clear()
        print("Chance time!")
        sleep(3)
        chance = chanceSpin()
        clear()
        print("Fate has decided! " + str(chance))
        player.money += chance
        sleep(3)
        
    elif boardHalf1 and boardFH["sp" + num]["spec"] == "round" or not boardHalf1 and boardSH["sp" + num]["spec"] == "round":
        clear()
        print("You have received 10 coins from completing a round!")
        player.money += 10
        sleep(3)
        
    elif boardHalf1 and boardFH["sp" + num]["spec"] == None or not boardHalf1 and boardSH["sp" + num]["spec"] == None:
        clear()
        if boardHalf1:
            bonus = boardFH["sp" + num]["bonus"]
        else:
            bonus = boardSH["sp" + num]["bonus"]
            
        print("Not a special place. " + bonus + " coins!")
        player.money += bonus
        sleep(3)
        
    
    player.turns += 1
    
        
# Paint board
def boardPaint(playerSymbol: str, playerPos: int, board: list[str], previousPos: int):
    match playerPos:
        case 1:
            board[80]
        case 2:
            board[82]
        case 3:
            board[60]
        case 4:
            board[49]
        case 5:
            board[29]
        case 6:
            board[7] = Back.CYAN + playerSymbol + Style.RESET_ALL
        case 7:
            board[5] = Back.GREEN + playerSymbol + Style.RESET_ALL
        case 8:
            board[3] = Back.YELLOW + playerSymbol + Style.RESET_ALL
        case 9:
            board[27]   
        case 10:
            board[47]
        case 11:
            board[58]
        case 12:
            board[78]
        case 13:
            board[62]
        case 14:
            board[84]
        case 15:
            board[86]
        case 16:
            board[89]
        case 17:
            board[64]
        case 18:
            board[53]
        case 19:
            board[33]
        case 20:
            board[13]
        case 21:
            board[11]
        case 22:
            board[9]
        case 23:
            board[31]
        case 24:
            board[51]
            
            
    if previousPos != 0:
        match previousPos:
            case 8:
                board[3] = Back.YELLOW + " " + Style.RESET_ALL
        

    bawdw = "i3=loc8, i5=loc7"


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
            prevPos = player.boardPos
            moveNum = diceThrow(player.name)
            boardMove(player, moveNum, boardFH=boardFH, boardSH=boardSH, blockadePrice=startingPriceL)
            boardPaint(player.sign, player.boardPos, boardGraphic, previousPos=prevPos)
            
        turns += 1