# Imports
import time
import os

from convenience import newMSG


# Vars
boardNames = {
    "1": "Balanced",
    "2": "Lucky",
    "3": "Unlucky"
}


# Ask player amount
def askAmountPlayers():
    try:
        players = int(input("Please select the amount of players (2-4): \t"))
        if players > 4 or players < 2:
            newMSG()
            print("Please enter a number from 2 to 4 instead!")
            time.sleep(3)
            newMSG()
            return
        else:
            return players
    
    except ValueError:
        newMSG()
        print("Please enter a number from 2 to 4 instead!")
        time.sleep(3)
        newMSG()
        return
    
    except KeyboardInterrupt:
        newMSG()
        print("Thanks for playing!")
        time.sleep(5)
        exit()


# Ask turns amount
def askAmountTurns():
    try:
        turns = int(input("Please select the amount of turns per player (10-20): \t"))
        if turns > 20 or turns < 10:
            newMSG()
            print("Please enter a number from 10 to 20 instead!")
            time.sleep(3)
            newMSG()
            return
        else:
            return turns
    
    except ValueError:
        newMSG()
        print("Please enter a number from 10 to 20 instead!")
        time.sleep(3)
        newMSG()
        return
    
    except KeyboardInterrupt:
        newMSG()
        print("Thanks for playing!")
        time.sleep(5)
        exit()


# Ask board number
def askNumberBoard():
    try:
        map = int(input("Please select one of the following maps:\n1. Balanced\n2. Lucky\n3. Unlucky\nPlease select a number: \t"))
        if int(map) > 3 or int(map) < 1:
            newMSG()
            print("Please enter a number from 1 to 3 instead!")
            time.sleep(3)
            newMSG()
            return
        else:
            return map
    
    except ValueError:
        newMSG()
        print("Please enter a number from 1 to 3 instead!")
        time.sleep(3)
        newMSG()
        return
    
    except KeyboardInterrupt:
        newMSG()
        print("Thanks for playing!")
        time.sleep(5)
        exit()


# Confirm Settings
def confirmSettings(names, turns, board):
    settings = "Are you sure you want to continue with these settings? (Yes/No) (y/n)\n------------------------------------------------------\n"
    for player in range(len(names)):
        settings += f"Player {player + 1}: {names[player]}\n"

    settings += "------------------------------------------------------\n"
    settings += f"Turns: {turns}\n"
    settings += f"Board: {board}. {boardNames[str(board)]}\n"
    settings += "=> : \t"

    choice = input(settings)
    return choice.lower().strip()