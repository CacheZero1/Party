# Imports (modules)
import tkinter as tk
import tkinter.ttk as ttk
import darkdetect
import ttkthemes
from PIL import Image, ImageTk
from tkinter import messagebox


# Game Window
def gameGUI(): #rounds: int, players: int, map: str, player1, player2, player3, player4
    """Open the Game GUI
    """
    # Design GUI
    root = tk.Tk()
    root.geometry("900x800")
    root.title("Ruby Hunter")
    
    rootStyle = ttkthemes.ThemedStyle(root)
    rootStyle.set_theme("equilux")
    
    
    # Create Elements
    player1Label = ttk.Label(root, text="Player 1:", font="Skia 20 underline", takefocus=0, foreground="white", background="black") # f"{player1.name}: {player1.symbol}"
    player2Label = ttk.Label(root, text="Player 2:", font="Skia 20 underline", takefocus=0, foreground="white", background="black") # f"{player1.name}: {player1.symbol}"
    player3Label = ttk.Label(root, text="Player 3:", font="Skia 20 underline", takefocus=0, foreground="white", background="black") # f"{player1.name}: {player1.symbol}"
    player4Label = ttk.Label(root, text="Player 4:", font="Skia 20 underline", takefocus=0, foreground="white", background="black") # f"{player1.name}: {player1.symbol}"
    
    player1Stats = tk.Text(root, state="normal", font="Skia 20", takefocus=0, border=0, highlightthickness=0)
    player2Stats = tk.Text(root, state="normal", font="Skia 20", takefocus=0, border=0, highlightthickness=0)
    player3Stats = tk.Text(root, state="normal", font="Skia 20", takefocus=0, border=0, highlightthickness=0)
    player4Stats = tk.Text(root, state="normal", font="Skia 20", takefocus=0, border=0, highlightthickness=0)
    
    player1Stats.insert(1.0, "Coins: {//} \nRubies: {**}".format(**{"//": 11, "**": 1})) # str(player1.money) str(player1.rubies)
    player2Stats.insert(1.0, "Coins: {//} \nRubies: {**}".format(**{"//": 12, "**": 2})) # str(player2.money) str(player2.rubies)
    player3Stats.insert(1.0, "Coins: {//} \nRubies: {**}".format(**{"//": 13, "**": 3})) # str(player3.money) str(player3.rubies)
    player4Stats.insert(1.0, "Coins: {//} \nRubies: {**}".format(**{"//": 14, "**": 4})) # str(player4.money) str(player4.rubies)
    
    actionDisplay = tk.Text(root, state="normal", font="Skia 20", takefocus=0, background="black", foreground="white", border=0, highlightthickness=0)
    boardFrame = ttk.Frame(root, relief="raised", takefocus=0)
    
    
    # Disable Elements
    player1Stats.config(state="disabled")
    player2Stats.config(state="disabled")
    player3Stats.config(state="disabled")
    player4Stats.config(state="disabled")
    
    actionDisplay.config(state="disabled")
    
    # Place Elements
    player1Label.place(x=9, y=556, width=150, height=30)
    player1Stats.place(x=9, y=591, width=150, height=60)
    
    player2Label.place(x=740, y=556, width=150, height=30)
    player2Stats.place(x=740, y=591, width=150, height=60)
    
    player3Label.place(x=9, y=696, width=150, height=30)
    player3Stats.place(x=9, y=731, width=150, height=60)
    
    player4Label.place(x=740, y=696, width=150, height=30)
    player4Stats.place(x=740, y=731, width=150, height=60)
    
    
    actionDisplay.place(x=169, y=556, width=561, height=235)
    
    # Main loop
    root.mainloop()
    
gameGUI()