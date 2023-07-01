# Import (modules)
import json


# Import (files)
import boards
import gameGui
import gui
import moveDraw
import player


# Variables
global roundsVar
global playerVar
global mapVar
global name1Var
global name2Var
global name3Var
global name4Var

roundsVar = 0
playerVar = 0
mapVar = ''
name1Var = ''
name2Var = ''
name3Var = ''
name4Var = ''


# Main method
def Game():
    # Welcome GUI / Settings UI
    gui.welcomeGUI()
    
    # Open Settings data
    with open('./data.json') as json_file:
        saveData = json.load(json_file)
        
        # Reassign vars
        roundsVar = saveData['rounds']
        playerVar = saveData['players']
        mapVar = saveData['map']
        name1Var = saveData['name1']
        name2Var = saveData['name2']
        name3Var = saveData['name3']
        name4Var = saveData['name4']
        
        
    # Configure game
    match playerVar:
        # Create Players
        case 3:
            # Create 3 Players
            player1 = player.Player(name1Var, 1)
            player2 = player.Player(name2Var, 2)
            player3 = player.Player(name3Var, 3)
        
        case 4:
            # Create 4 Players
            player1 = player.Player(name1Var, 1)
            player2 = player.Player(name2Var, 2)
            player3 = player.Player(name3Var, 3)
            player4 = player.Player(name4Var, 4)
            
        case _:
            # Create 2 Players
            player1 = player.Player(name1Var, 1)
            player2 = player.Player(name2Var, 2)
            
            
    
    
Game()