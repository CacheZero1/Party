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
        sleep(7)
        

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
        sleep(5)
        
        starterPlayer(starters=starter, starterNrs=starterNr, playObjs=res, isStr=True)

        res = []
        
        starterFilter(userList=starter, compare=starterNr, addTo=res)
        sleep(5)

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
    while not keyboard.is_pressed('space'):
        pass

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
        money = random.choice(list(range(1, 101)))
        print(str(sign) + str(money))
        
    if sign == "+":
        return money
    else:
        return -money


# Move on board
def boardMove(player, moves: int, boardFH: dict[dict], boardSH: dict[dict], blockadePrice: int):
    global startingPriceL
    for move in range(moves):
        boardHalf1 = True if player.boardPosN == 0 else False
        player.boardPos += 1
        if boardHalf1 and player.boardPos > 12 or not boardHalf1 and player.boardPos > 24:
            player.boardPos -= 12

        num = f"0{player.boardPos}" if len(str(player.boardPos)) != 2 else str(player.boardPos)
        
        
        # Buy star
        if boardHalf1 and boardFH["sp" + num]["spec"] == "star" or not boardHalf1 and boardSH["sp" + num]["spec"] == "star":
            if checkMoney(player=player, price=30):
                will = rubyWill(name=player.name)
                while will != 'n' and will != 'no' and will != 'y' and will != 'yes':
                    will = rubyWill(name=player.name)
                    
                if will == 'n' or will == 'no':
                    clear()
                    print("Strange, but ok!")
                    sleep(5)
                    
                elif will == 'yes' or will == 'y':
                    player.money -= 30
                    clear()
                    print("A ruby has been added to your account!")
                    player.stars += 1
                    sleep(5)
                    
                    
            else:
                clear()
                print("You sadly don't have enough coins to buy a ruby, better luck next time!")
                sleep(5)



    # First board side change
    if boardHalf1 and "dir" in boardFH["sp" + num].keys():
        if checkMoney(player=player, price=blockadePrice):
            will = blockageWill(name=player.name, price=blockadePrice)
            while will != 'n' and will != 'no' and will != 'y' and will != 'yes':
                will = blockageWill(name=player.name, price=blockadePrice)
                
            if will == 'n' or will == 'no':
                clear()
                print("Ok, maybe next time!")
                sleep(5)
                
            elif will == 'yes' or will == 'y':
                player.money -= startingPriceL
                startingPriceL += 1
                player.boardPosN = player.boardPosN +  boardFH["sp" + num]["dir"] if boardHalf1 else player.boardPosN + boardSH["sp" + num]["dir"]
                player.boardPos = 13 if player.boardPos == 3 else 23
                boardHalf1 = not boardHalf1
                num = f"0{player.boardPos}" if len(str(player.boardPos)) != 2 else str(player.boardPos)
                clear()
                print("You have crossed the blockade and the price has increased!")
                sleep(5)
                    
                    
    if not boardHalf1 and "dir" in boardSH["sp" + num].keys():
        if checkMoney(player=player, price=blockadePrice):
            will = blockageWill(name=player.name, price=blockadePrice)
            while will != 'n' and will != 'no' and will != 'y' and will != 'yes':
                will = blockageWill(name=player.name, price=blockadePrice)
                
            if will == 'n' or will == 'no':
                clear()
                print("Ok, maybe next time!")
                sleep(5)
                
            elif will == 'yes' or will == 'y':
                player.money -= startingPriceL
                startingPriceL += 1
                player.boardPosN = player.boardPosN + boardSH["sp" + num]["dir"] if not boardHalf1 else player.boardPosN + boardFH["sp" + num]["dir"]
                player.boardPos = 3 if player.boardPos == 13 else 5
                boardHalf1 = not boardHalf1
                num = f"0{player.boardPos}" if len(str(player.boardPos)) != 2 else str(player.boardPos)
                clear()
                print("You have crossed the blockade and the price has increased!")
                sleep(5)
                    
                 
         
    num = f"0{player.boardPos}" if len(str(player.boardPos)) != 2 else str(player.boardPos)       
    if boardHalf1 and boardFH["sp" + num]["spec"] == "luck" or boardHalf1 and boardFH["sp" + num]["spec"] == "unluck" or not boardHalf1 and boardSH["sp" + num]["spec"] == "luckExtra" or not boardHalf1 and boardSH["sp" + num]["spec"] == "unluckExtra":
        addMoney = random.choice(boardFH["sp" + num]["bonus"]) if boardHalf1 else random.choice(boardSH["sp" + num]["bonus"])
        if addMoney > 0:
            clear()
            print(f"{addMoney} coins have been added to your balance!")
            player.money += addMoney
        else:
            clear()
            print(f"{addMoney} coins have been deducted from your balance!")
            if not checkMoney(player, abs(addMoney)):
                player.money = 0
            else:
                player.money += addMoney
            
        sleep(5)
            
    elif boardHalf1 and boardFH["sp" + num]["spec"] == "chance" or not boardHalf1 and boardSH["sp" + num]["spec"] == "chance":
        clear()
        print("Chance time!")
        sleep(5)
        chance = chanceSpin()
        clear()
        print("Fate has decided! " + str(chance))
        if chance < 0:
            if checkMoney(player, abs(chance)):
                player.money += chance
            else:
                player.money = 0
                
        else:
            player.money += chance

        sleep(4)
        
    elif boardHalf1 and boardFH["sp" + num]["spec"] == "round" or not boardHalf1 and boardSH["sp" + num]["spec"] == "round":
        clear()
        print("You have received 10 coins from completing a round!")
        player.money += 10
        sleep(5)
        
    elif boardHalf1 and boardFH["sp" + num]["spec"] == None or not boardHalf1 and boardSH["sp" + num]["spec"] == None:
        clear()
        if boardHalf1:
            bonus = boardFH["sp" + num]["bonus"]
        else:
            bonus = boardSH["sp" + num]["bonus"]
            
        print("Not a special place. " + str(bonus) + " coins!")
        player.money += bonus if bonus != None else 0
        sleep(4)
        
    
    player.turns += 1
    
        
# Paint board
def boardPaint(playerSymbol: str, playerPos: int, board: list[str], previousPos: int):
    match playerPos:
        case 1:
            board[89] = Back.GREEN + playerSymbol + Style.RESET_ALL
        case 2:
            board[91] = Back.GREEN + playerSymbol + Style.RESET_ALL
        case 3:
            board[69] = Back.MAGENTA + playerSymbol + Style.RESET_ALL
        case 4:
            board[49] = Back.GREEN + playerSymbol + Style.RESET_ALL
        case 5:
            board[29] = Back.RED + playerSymbol + Style.RESET_ALL
        case 6:
            board[7] = Back.CYAN + playerSymbol + Style.RESET_ALL
        case 7:
            board[5] = Back.GREEN + playerSymbol + Style.RESET_ALL
        case 8:
            board[3] = Back.YELLOW + playerSymbol + Style.RESET_ALL
        case 9:
            board[27] = Back.MAGENTA + playerSymbol + Style.RESET_ALL
        case 10:
            board[47] = Back.RED + playerSymbol + Style.RESET_ALL
        case 11:
            board[67] = Back.GREEN + playerSymbol + Style.RESET_ALL
        case 12:
            board[87] = Back.BLACK + playerSymbol + Style.RESET_ALL
        case 13:
            board[71] = Back.GREEN + playerSymbol + Style.RESET_ALL
        case 14:
            board[93] = Back.MAGENTA + playerSymbol + Style.RESET_ALL
        case 15:
            board[95] = Back.GREEN + playerSymbol + Style.RESET_ALL
        case 16:
            board[97] = Back.GREEN + playerSymbol + Style.RESET_ALL
        case 17:
            board[73] = Back.GREEN + playerSymbol + Style.RESET_ALL
        case 18:
            board[53] = Back.YELLOW + playerSymbol + Style.RESET_ALL
        case 19:
            board[33] = Back.GREEN + playerSymbol + Style.RESET_ALL
        case 20:
            board[13] = Back.RED + playerSymbol + Style.RESET_ALL
        case 21:
            board[11] = Back.GREEN + playerSymbol + Style.RESET_ALL
        case 22:
            board[9] = Back.BLACK + playerSymbol + Style.RESET_ALL
        case 23:
            board[31] = Back.GREEN + playerSymbol + Style.RESET_ALL
        case 24:
            board[51] = Back.CYAN + playerSymbol + Style.RESET_ALL
            
            
    if previousPos != 0:
        match previousPos:
            case 1:
                board[89] = Back.GREEN + " " + Style.RESET_ALL
            case 2:
                board[91] = Back.GREEN + " " + Style.RESET_ALL
            case 3:
                board[69] = Back.MAGENTA + " " + Style.RESET_ALL
            case 4:
                board[49] = Back.GREEN + " " + Style.RESET_ALL
            case 5:
                board[29] = Back.RED + " " + Style.RESET_ALL
            case 6:
                board[7] = Back.CYAN + " " + Style.RESET_ALL
            case 7:
                board[5] = Back.GREEN + " " + Style.RESET_ALL
            case 8:
                board[3] = Back.YELLOW + " " + Style.RESET_ALL
            case 9:
                board[27] = Back.MAGENTA + " " + Style.RESET_ALL
            case 10:
                board[47] = Back.RED + " " + Style.RESET_ALL
            case 11:
                board[67] = Back.GREEN + " " + Style.RESET_ALL
            case 12:
                board[87] = Back.BLACK + " " + Style.RESET_ALL
            case 13:
                board[71] = Back.GREEN + " " + Style.RESET_ALL
            case 14:
                board[93] = Back.MAGENTA + " " + Style.RESET_ALL
            case 15:
                board[95] = Back.GREEN + " " + Style.RESET_ALL
            case 16:
                board[97] = Back.GREEN + " " + Style.RESET_ALL
            case 17:
                board[73] = Back.GREEN + " " + Style.RESET_ALL
            case 18:
                board[53] = Back.YELLOW + " " + Style.RESET_ALL
            case 19:
                board[33] = Back.GREEN + " " + Style.RESET_ALL
            case 20:
                board[13] = Back.RED + " " + Style.RESET_ALL
            case 21:
                board[11] = Back.GREEN + " " + Style.RESET_ALL
            case 22:
                board[9] = Back.BLACK + " " + Style.RESET_ALL
            case 23:
                board[31] = Back.GREEN + " " + Style.RESET_ALL
            case 24:
                board[51] = Back.CYAN + " " + Style.RESET_ALL

    return board
        

    


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

    while not turns >= maxTurns:
        for player in playerOrder:
            prevPos = player.boardPos

            moveNum = diceThrow(player.name)
            sleep(1)

            boardMove(player, moveNum, boardFH=boardFH, boardSH=boardSH, blockadePrice=startingPriceL)
            paintedBoard = boardPaint(player.sign, player.boardPos, boardGraphic, previousPos=prevPos)
            sleep(1)
            clear()
            for boardTile in paintedBoard:
                print(boardTile, end="")
            print("\n------------------------------")
            for playerstats in playerObject:
                print(f"{playerstats.name} {playerstats.sign}: Coins = {playerstats.money} | Rubies = {playerstats.stars}")
            print("\n------------------------------")
            print(f"Turns: {turns}")
            print(f"Blockade price: {startingPriceL}")

            while not keyboard.is_pressed('space'):
                pass
            
            sleep(1)

            
        turns += 1

    
    clear()
    print("Done!")
    while not keyboard.is_pressed('space'):
        pass