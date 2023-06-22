import os

system = 'clear' if os.name == "posix" else 'cls'

def clear():
    os.system(system)
    
def newMSG():
    os.system(system)
    print("Welcome to PyParty!")