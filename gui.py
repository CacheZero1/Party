# Imports (modules)
import tkinter as tk
import tkinter.ttk as ttk
import darkdetect
import ttkthemes
from PIL import Image, ImageTk


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
    radioStyle.configure('design.TRadiobutton', font="Skia 12")
    
    rBtn2p = ttk.Radiobutton(root, text="2 Players", value=2, variable=playerAmountVar, takefocus=0, style='design.TRadiobutton')
    rBtn3p = ttk.Radiobutton(root, text="3 Players", value=3, variable=playerAmountVar, takefocus=0, style='design.TRadiobutton')
    rBtn4p = ttk.Radiobutton(root, text="4 Players", value=4, variable=playerAmountVar, takefocus=0, style='design.TRadiobutton')
    
    rBtn2p.place(x=182, y=440, width=164, height=30)
    rBtn3p.place(x=182, y=480, width=164, height=30)
    rBtn4p.place(x=182, y=520, width=164, height=30)
    
    
    # Player Name Selector
    playerNamePrompt = ttk.Label(root, text="Enter Player names", font="Skia 14 underline", anchor="center")
    playerNamePrompt.place(x=354, y=400, width=164, height=30)
    
    
    # Round Amount Selector
    roundAmountPrompt = ttk.Label(root, text="Select Rounds", font="Skia 14 underline", anchor="center")
    roundAmountPrompt.place(x=526, y=400, width=164, height=30)
    
    
    # ------------ </Add widgets> ------------
    

    # Mainloop
    root.mainloop()
    
    
