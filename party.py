# Imports (modules)
import os
import time


# Imports (files)
from startquestions import askAmountPlayers
from startquestions import askAmountTurns
from startquestions import askNumberBoard
from startquestions import confirmSettings
from player import createPlayers
from game import Game
from convenience import newMSG


# Standart vars
turns = 0
maxTurns = 1
players = []
playerObj = []
boardChoice = 0
startingPrice = 1
lastPlayer = 0


# Exit method
def exit():
    quit()


# Reset the game vars
def reset():
    global turns
    turns = 0
    global maxTurns
    maxTurns = 0
    global players
    players = []
    global playerObj
    playerObj = []
    global boardChoice
    boardChoice = 0
    global board0
    board0 = {}
    global board1
    board1 = {}
    global startingPrice
    startingPrice = 1
    global lastPlayer
    lastPlayer = 0


# Game starting config
def startGame():

    newMSG()
    playerAmount = 0
    while playerAmount not in list(range(2, 5)):
        playerAmount = askAmountPlayers()
        
    
    newMSG()
    turnAmount = 0
    while turnAmount not in list(range(10, 21)):
        turnAmount = askAmountTurns()
    global maxTurns 
    maxTurns = turnAmount
    
    newMSG()
    boardNumber = 0
    while boardNumber not in list(range(1, 4)):
        boardNumber = askNumberBoard()
    global boardChoice
    boardChoice = boardNumber
    

    newMSG()
    for playerNum in range(playerAmount):
        newPlayer = createPlayers(playNr=playerNum, playerNames=players)
        players.append(newPlayer.name)
        playerObj.append(newPlayer)

    newMSG()


# Main game loop
def GameLoop():
    while True:
        startGame()
        try:
            confirmed = confirmSettings(players, maxTurns, boardChoice)
            while confirmed != 'n' and confirmed != 'no' and confirmed != 'y' and confirmed != 'yes':
                newMSG()
                print("Please write either 'no/n' or 'yes/y'!")
                time.sleep(3)
                newMSG()
                confirmed = confirmSettings(players, maxTurns, boardChoice)

            while confirmed == 'n' or confirmed == 'no':
                reset()
                GameLoop()

            if confirmed == 'yes' or confirmed == 'y':
                Game(turns, maxTurns, playerObj, boardChoice, startingPrice, lastPlayer)


        except KeyboardInterrupt:
            newMSG()
            print("Thanks for playing!")
            time.sleep(5)
            exit()

GameLoop()