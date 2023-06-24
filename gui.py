# Imports (modules)
import tkinter as tk
from PIL import Image, ImageTk
from imageOpener import getPreviews

# Main gui
def welcomeGUI():
    """Open the main GUI
    """
    beachIslandsPreview = getPreviews(); bea
    root = tk.Tk()
    img = ImageTk.PhotoImage(beachIslandsPreview)
    panel = tk.Label(root, image=beachIslandsPreview)
    panel.pack()



    root.mainloop()
