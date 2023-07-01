# Imports (modules)
import tkinter as tk
import tkinter.ttk as ttk
import darkdetect
import ttkthemes
import json
from PIL import Image, ImageTk
from tkinter import messagebox


# Setter method
def setVars(roundsVar, playerVar, mapVar, name1Var, name2Var, name3Var, name4Var):
    """Set the settings in the JSON file

    Args:
        roundsVar (int): Amount of Rounds
        playerVar (int): Amount of Players
        mapVar (str): Selected Map
        name1Var (str): Name of Player 1
        name2Var (str): Name of Player 2
        name3Var (str): Name of Player 3
        name4Var (str): Name of Player 4
    """
    
    # Game data Dictionary
    gameData = {
        'rounds': roundsVar,
        'players': playerVar,
        'map': mapVar,
        'name1': name1Var,
        'name2': name2Var,
        'name3': name3Var,
        'name4': name4Var
    }
    
    # Write to file
    with open('./data.json', 'w') as json_file:
        json.dump(gameData, json_file, indent=4)
    

# Main gui
def welcomeGUI():
    """Open the main GUI
    """
    root = tk.Tk()
    root.geometry("700x700")
    
    
    # Vars
    mapList = ["Beach Islands", "Mineshafts", "Garden Labyrinth", "Mansion Halls"]
    amountList = list(range(10, 31))
    
    
    # Preview Images
    beachIslandsPreviewImg = ImageTk.PhotoImage(Image.open("./beachIslands/beachIslandsPreview.png"));
    #mineShaftsPreviewImg = ImageTk.PhotoImage(Image.open("./mineShafts/mineShaftsPreview.png"));
    #gardenLabyrinthPreviewImg = ImageTk.PhotoImage(Image.open("./gardenLabirynth/gardenLabyrinthPreview.png"));
    #mansionHallsPreviewImg = ImageTk.PhotoImage(Image.open("./mansionHalls/mansionHallsPreview.png"));
    
   
    # Design GUI
    root.title("Ruby Hunter")
    
    rootStyle = ttkthemes.ThemedStyle(root)
    rootStyle.set_theme("equilux")
        
        
    # ------------ <Add widgets> ------------
    # Previews
    beachIslandsPreview = ttk.Label(root, image=beachIslandsPreviewImg, border=0, borderwidth=0)
    beachIslandsPreview.place(x=115, y=20, width=468, height=349)
    
    #mineShaftsPreview = ttk.Label(root, image=mineShaftsPreviewImg, border=0, borderwidth=0)
    #gardenLabyrinthPreview = ttk.Label(root, image=gardenLabirynthPreviewImg, border=0, borderwidth=0)
    #mansionHallsPreview = ttk.Label(root, image=mansionHallsPreviewImg, border=0, borderwidth=0)
    
    
    # ------------ <Widget Func> ------------
    # Combobox select
    def comboboxselect(event):
        """Change Preview Image on Combobox Select

        Args:
            event: event to get widget
        """
        boxValue = event.widget.get()
        
        match boxValue:
            # Check for Beach Islands
            case "Beach Islands":
                beachIslandsPreview.place(x=115, y=20, width=468, height=349)
                #mineShaftsPreview.place_forget()
                #gardenLabyrinthPreview.place_forget()
                #mansionHallsPreview.place_forget()
                
            # Check for Mineshafts
            case "Mineshafts":
                beachIslandsPreview.place_forget()
                #mineShaftsPreview.place(x=115, y=20, width=468, height=349)
                #gardenLabyrinthPreview.place_forget()
                #mansionHallsPreview.place_forget()
                
            # Check for Garden Labyrinth
            case "Garden Labyrinth":
                beachIslandsPreview.place_forget()
                #mineShaftsPreview.place_forget()
                #gardenLabyrinthPreview.place(x=115, y=20, width=468, height=349)
                #mansionHallsPreview.place_forget()
                
            #Check for Mansion Halls
            case "Mansion Halls":
                beachIslandsPreview.place_forget()
                #mineShaftsPreview.place_forget()
                #gardenLabyrinthPreview.place_forget()
                #mansionHallsPreview.place(x=115, y=20, width=468, height=349)
                
    
    # Name entry shower
    def nameAvailability(playerCount, field3, field4):
        """Make the Entries for playername appear

        Args:
            playerCount (int): amount of players playing
            field3: Entry widget for player 3
            field4: Entry widget for player 4
        """
        match playerCount:
            case 2:
                field3.place_forget()
                field4.place_forget()
                
            case 3:
                field3.place(x=354 ,y=520, width=164, height=30)
                field4.place_forget()
                
            case 4:
                field3.place(x=354 ,y=520, width=164, height=30)
                field4.place(x=354 ,y=560, width=164, height=30)
                
                
    # On Play-Button press
    def playButtonPress(roundAmountVariable, playerAmountVariable, selectedMap, playerNames0, playerNames1, playerNames2, playerNames3):
        canStart = False
        
        match playerAmountVariable:
            case 2:
                if playerNames0.strip() == "" or playerNames1.strip() == "":
                    messagebox.showwarning("Warning: Name", "Names can't be empty!")
                     
                else:
                    messagebox.showinfo("Game Startup", "Please wait while the Game starts!")
                    canStart = True
                    
                    
            case 3:
                if playerNames0.strip() == "" or playerNames1.strip() == "" or playerNames2.strip() == "":
                    messagebox.showwarning("Warning: Name", "Names can't be empty!")
                    
                else:
                    messagebox.showinfo("Game Startup", "Please wait while the Game starts!")
                    canStart = True  
                
                
            case 4:
                if playerNames0.strip() == "" or playerNames1.strip() == "" or playerNames2.strip() == "" or playerNames3.strip() == "":
                    messagebox.showwarning("Warning: Name", "Names can't be empty!")
                    
                else:
                    messagebox.showinfo("Game Startup", "Please wait while the Game starts!")
                    canStart = True
                    
                    
        if canStart:
            root.destroy()
            setVars(roundsVar=roundAmountVariable, playerVar=playerAmountVariable, mapVar=selectedMap, name1Var=playerNames0, name2Var=playerNames1, name3Var=playerNames2, name4Var=playerNames3)
                
    
    # ------------ </Widget Func> ------------
    
    
    # Game Map Selector
    mapSelectorPrompt = ttk.Label(root, text="Select the Map", font="Skia 14 underline", anchor="center")
    mapSelectorPrompt.place(x=9, y=400, width=164, height=30)
    
    Combo = ttk.Combobox(root, values=mapList, font="Skia 12", state="readonly")
    Combo.set(mapList[0])
    Combo.bind("<<ComboboxSelected>>", comboboxselect)
    Combo.place(x=9, y=440, width=164, height=30)
    
    
    # Player Amount Selector
    playerAmountPrompt = ttk.Label(root, text="Select Player amount", font="Skia 14 underline", anchor="center")
    playerAmountPrompt.place(x=182, y=400, width=164, height=30)
    
    playerAmountVar = tk.IntVar()
    playerAmountVar.set(2)
    
    radioStyle = ttk.Style()
    radioStyle.theme_use("equilux")
    radioStyle.configure('designP.TRadiobutton', font="Skia 12")
    
    rBtn2p = ttk.Radiobutton(root, text="2 Players", value=2, variable=playerAmountVar, takefocus=0, style='designP.TRadiobutton')
    rBtn3p = ttk.Radiobutton(root, text="3 Players", value=3, variable=playerAmountVar, takefocus=0, style='designP.TRadiobutton')
    rBtn4p = ttk.Radiobutton(root, text="4 Players", value=4, variable=playerAmountVar, takefocus=0, style='designP.TRadiobutton')
    
    rBtn2p.place(x=182, y=440, width=164, height=30)
    rBtn3p.place(x=182, y=480, width=164, height=30)
    rBtn4p.place(x=182, y=520, width=164, height=30)
    
    
    # Player Name Selector
    playerNamePrompt = ttk.Label(root, text="Enter Player names", font="Skia 14 underline", anchor="center")
    playerNamePrompt.place(x=354, y=400, width=164, height=30)
    
    playerNameEntry1 = ttk.Entry(root, font="Skia 12", takefocus=0)
    playerNameEntry2 = ttk.Entry(root, font="Skia 12", takefocus=0)
    playerNameEntry3 = ttk.Entry(root, font="Skia 12", takefocus=0)
    playerNameEntry4 = ttk.Entry(root, font="Skia 12", takefocus=0)
    
    playerNameEntry1.place(x=354, y=440, width=164, height=30)
    playerNameEntry2.place(x=354, y=480, width=164, height=30)
    
    rBtn2p.configure(command=lambda: nameAvailability(2, playerNameEntry3, playerNameEntry4))
    rBtn3p.configure(command=lambda: nameAvailability(3, playerNameEntry3, playerNameEntry4))
    rBtn4p.configure(command=lambda: nameAvailability(4, playerNameEntry3, playerNameEntry4))
    
    
    # Round Amount Selector
    roundAmountPrompt = ttk.Label(root, text="Select Rounds", font="Skia 14 underline", anchor="center")
    roundAmountPrompt.place(x=526, y=400, width=164, height=30)
    
    roundAmountVar = tk.IntVar()
    roundAmountVar.set(10)
    
    radioStyle1 = ttk.Style()
    radioStyle1.theme_use("equilux")
    radioStyle1.configure('designR.TRadiobutton', font="Skia 12")
    
    rBtn10R = ttk.Radiobutton(root, text="10 Rounds", value=10 ,variable=roundAmountVar, takefocus=0, style='designR.TRadiobutton')
    rBtn20R = ttk.Radiobutton(root, text="20 Rounds", value=20 ,variable=roundAmountVar, takefocus=0, style='designR.TRadiobutton')
    rBtn30R = ttk.Radiobutton(root, text="30 Rounds", value=30 ,variable=roundAmountVar, takefocus=0, style='designR.TRadiobutton')
    rBtn40R = ttk.Radiobutton(root, text="40 Rounds", value=40 ,variable=roundAmountVar, takefocus=0, style='designR.TRadiobutton')
    
    rBtn10R.place(x=526, y=440, width=164, height=30)
    rBtn20R.place(x=526, y=480, width=164, height=30)
    rBtn30R.place(x=526, y=520, width=164, height=30)
    rBtn40R.place(x=526, y=560, width=164, height=30)
    
    
    # Play Button
    buttonStyle = ttk.Style()
    buttonStyle.theme_use("equilux")
    buttonStyle.configure('playB.TButton', font="Skia 16", background='green')
    
    playBtn = ttk.Button(root, text="PLAY", cursor="bogosity", style='playB.TButton', takefocus=0, command=lambda: playButtonPress(roundAmountVariable=roundAmountVar.get(), playerAmountVariable=playerAmountVar.get(), selectedMap=Combo.get(), playerNames0=playerNameEntry1.get(), playerNames1=playerNameEntry2.get(), playerNames2=playerNameEntry3.get(), playerNames3=playerNameEntry4.get()))
    playBtn.place(x= 9, y=620, width=680, height=50)
    
    
    # ------------ </Add widgets> ------------
    

    # Mainloop
    root.mainloop()
    