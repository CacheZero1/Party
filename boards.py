from colorama import Fore, Back, Style


mapart = ". -- . -- .    . -- . -- .\n|         |    |         |\n.         . -- .         .\n|         |    |         |\n.         .    .         .\n|         |    |         |\n.         . -- .         .\n|         |    |         |\n. -- . -- .    . -- . -- .\n     |                    \n     ."


mapPartBlankRow = Back.BLUE + "                            " + Style.RESET_ALL
mapPartBlankSingular = Back.BLUE + " " + Style.RESET_ALL
mapPartBlankLong = Back.BLUE + "         " + Style.RESET_ALL
mapPartBlankShort = Back.BLUE + "    " + Style.RESET_ALL

mapPartWayRow = Back.GREEN + " -- " + Style.RESET_ALL
mapPartWayColumn = Back.GREEN + "|" + Style.RESET_ALL


def balanced():
    boardFH = {
        "sp01": {
            "spec": None,
            "bonus": 3
        },
        "sp02": {
            "spec": None,
            "bonus": 3,
        },
        "sp03": {
            "spec": "luck",
            "bonus": list(range(10, 21, 2)),
            "dir": 1
        },
        "sp04": {
            "spec": None,
            "bonus": -3
        },
        "sp05": {
            "spec": "unluck",
            "bonus": list(range(-10, -21, -2)),
            "dir": 1
        },
        "sp06": {
            "spec": "chance",
            "bonus": None,
        },
        "sp07": {
            "spec": None,
            "bonus": -3
        },
        "sp08": {
            "spec": "star",
            "bonus": None,
            "occupied": False
        },
        "sp09": {
            "spec": "luck",
            "bonus": list(range(10, 21, 2))
        },
        "sp10": {
            "spec": "unluck",
            "bonus": list(range(-10, -21, -2))
        },
        "sp11": {
            "spec": None,
            "bonus": None
        },
        "sp12": {
            "spec": "round",
            "bonus": 10
        }
    }

    boardSH = {
        "sp13": {
            "spec": None,
            "bonus": 3,
            "dir": -1
        },
        "sp14": {
            "spec": "luckExtra",
            "bonus": list(range(10, 41, 3))
        },
        "sp15": {
            "spec": None,
            "bonus": -3
        },
        "sp16": {
            "spec": None,
            "bonus": -3
        },
        "sp17": {
            "spec": None,
            "bonus": 3
        },
        "sp18": {
            "spec": "star",
            "bonus": None,
            "occupied": True
        },
        "sp19": {
            "spec": None,
            "bonus": 3
        },
        "sp20": {
            "spec": "unluckExtra",
            "bonus": list(range(-10, -41, -3))
        },
        "sp21": {
            "spec": None,
            "bonus": -3
        },
        "sp22": {
            "spec": "round",
            "bonus": 10
        },
        "sp23": {
            "spec": None,
            "bonus": 3,
            "dir": -1
        },
        "sp24": {
            "spec": "chance",
            "bonus": None
        }
    }

    maploc00 = Back.GREEN + " " + Style.RESET_ALL
    maploc01 = Back.GREEN + " " + Style.RESET_ALL
    maploc02 = Back.GREEN + " " + Style.RESET_ALL
    maploc03 = Back.MAGENTA + " " + Style.RESET_ALL
    maploc04 = Back.GREEN + " " + Style.RESET_ALL
    maploc05 = Back.RED + " " + Style.RESET_ALL
    maploc06 = Back.CYAN + " " + Style.RESET_ALL
    maploc07 = Back.GREEN + " " + Style.RESET_ALL
    maploc08 = Back.YELLOW + " " + Style.RESET_ALL
    maploc09 = Back.MAGENTA + " " + Style.RESET_ALL
    maploc10 = Back.RED + " " + Style.RESET_ALL
    maploc11 = Back.GREEN + " " + Style.RESET_ALL
    maploc12 = Back.BLACK + " " + Style.RESET_ALL
    maploc13 = Back.GREEN + " " + Style.RESET_ALL
    maploc14 = Back.MAGENTA + " " + Style.RESET_ALL
    maploc15 = Back.GREEN + " " + Style.RESET_ALL
    maploc16 = Back.GREEN + " " + Style.RESET_ALL
    maploc17 = Back.GREEN + " " + Style.RESET_ALL
    maploc18 = Back.YELLOW + " " + Style.RESET_ALL
    maploc19 = Back.GREEN + " " + Style.RESET_ALL
    maploc20 = Back.RED + " " + Style.RESET_ALL
    maploc21 = Back.GREEN + " " + Style.RESET_ALL
    maploc22 = Back.BLACK + " " + Style.RESET_ALL
    maploc23 = Back.GREEN + " " + Style.RESET_ALL
    maploc24 = Back.CYAN + " " + Style.RESET_ALL

    
    coloredMapList = [mapPartBlankRow, "\n", mapPartBlankSingular, maploc08, mapPartWayRow, maploc07, mapPartWayRow, maploc06, mapPartBlankShort, maploc22, mapPartWayRow, maploc21, mapPartWayRow, maploc20, mapPartBlankSingular, "\n"]
    coloredMapList.append(mapPartBlankSingular, mapPartWayColumn, mapPartBlankLong, mapPartWayColumn, mapPartBlankShort, mapPartWayColumn, mapPartBlankLong, mapPartWayColumn, mapPartBlankSingular, "\n")
    coloredMapList.append(mapPartBlankSingular, maploc09, mapPartBlankLong, maploc05, mapPartWayRow, maploc23, mapPartBlankLong, maploc19, mapPartBlankSingular, "\n")
    coloredMapList.append(mapPartBlankSingular, mapPartWayColumn, mapPartBlankLong, mapPartWayColumn, mapPartBlankShort, mapPartWayColumn, mapPartBlankLong, mapPartWayColumn, mapPartBlankSingular, "\n")
    coloredMapList.append(mapPartBlankSingular, maploc10, mapPartBlankLong, maploc04, mapPartBlankShort, maploc24, mapPartBlankLong, maploc18, mapPartBlankSingular, "\n")
    coloredMapList.append(mapPartBlankSingular, mapPartWayColumn, mapPartBlankLong, mapPartWayColumn, mapPartBlankShort, mapPartWayColumn, mapPartBlankLong, mapPartWayColumn, mapPartBlankSingular, "\n")
    coloredMapList.append(mapPartBlankSingular, maploc11, mapPartBlankLong, maploc03, mapPartWayRow, maploc13, mapPartBlankLong, maploc17, mapPartBlankSingular, "\n")
    coloredMapList.append(mapPartBlankSingular, mapPartWayColumn, mapPartBlankLong, mapPartWayColumn, mapPartBlankShort, mapPartWayColumn, mapPartBlankLong, mapPartWayColumn, mapPartBlankSingular, "\n")
    coloredMapList.append(mapPartBlankSingular, maploc12, mapPartWayRow, maploc01, mapPartWayRow, maploc02, mapPartBlankShort, maploc14, mapPartWayRow, maploc15, mapPartWayRow, maploc16, mapPartBlankSingular, "\n", mapPartBlankRow)
    

    coloredMap = mapPartBlankRow + "\n" 
    coloredMap += mapPartBlankSingular + maploc08 + mapPartWayRow + maploc07 + mapPartWayRow + maploc06 + mapPartBlankShort + maploc22 + mapPartWayRow + maploc21 + mapPartWayRow + maploc20 + mapPartBlankSingular + "\n"
    coloredMap += mapPartBlankSingular + mapPartWayColumn + mapPartBlankLong + mapPartWayColumn + mapPartBlankShort + mapPartWayColumn + mapPartBlankLong + mapPartWayColumn + mapPartBlankSingular + "\n"
    coloredMap += mapPartBlankSingular + maploc09 + mapPartBlankLong + maploc05 + mapPartWayRow + maploc23 + mapPartBlankLong + maploc19 + mapPartBlankSingular + "\n"
    coloredMap += mapPartBlankSingular + mapPartWayColumn + mapPartBlankLong + mapPartWayColumn + mapPartBlankShort + mapPartWayColumn + mapPartBlankLong + mapPartWayColumn + mapPartBlankSingular + "\n"
    coloredMap += mapPartBlankSingular + maploc10 + mapPartBlankLong + maploc04 + mapPartBlankShort + maploc24 + mapPartBlankLong + maploc18 + mapPartBlankSingular + "\n"
    coloredMap += mapPartBlankSingular + mapPartWayColumn + mapPartBlankLong + mapPartWayColumn + mapPartBlankShort + mapPartWayColumn + mapPartBlankLong + mapPartWayColumn + mapPartBlankSingular + "\n"
    coloredMap += mapPartBlankSingular + maploc11 + mapPartBlankLong + maploc03 + mapPartWayRow + maploc13 + mapPartBlankLong + maploc17 + mapPartBlankSingular + "\n"
    coloredMap += mapPartBlankSingular + mapPartWayColumn + mapPartBlankLong + mapPartWayColumn + mapPartBlankShort + mapPartWayColumn + mapPartBlankLong + mapPartWayColumn + mapPartBlankSingular + "\n"
    coloredMap += mapPartBlankSingular + maploc12 + mapPartWayRow + maploc01 + mapPartWayRow + maploc02 + mapPartBlankShort + maploc14 + mapPartWayRow + maploc15 + mapPartWayRow + maploc16 + mapPartBlankSingular + "\n"
    coloredMap += mapPartBlankRow

    return boardFH, boardSH, coloredMapList


def lucky():
    boardFH = {
        "sp01": {
            "spec": None,
            "bonus": -3
        },
        "sp02": {
            "spec": None,
            "bonus": 3,
        },
        "sp03": {
            "spec": "unluck",
            "bonus": list(range(-10, -21, -2)),
            "dir": 2
        },
        "sp04": {
            "spec": None,
            "bonus": -3
        },
        "sp05": {
            "spec": "unluck",
            "bonus": list(range(-10, -21, -2)),
            "dir": 2
        },
        "sp06": {
            "spec": "chance",
            "bonus": None,
        },
        "sp07": {
            "spec": None,
            "bonus": -3
        },
        "sp08": {
            "spec": "star",
            "bonus": None,
            "occupied": False
        },
        "sp09": {
            "spec": "luck",
            "bonus": list(range(10, 21, 2))
        },
        "sp10": {
            "spec": "unluck",
            "bonus": list(range(-10, -21, -2))
        },
        "sp11": {
            "spec": None,
            "bonus": None
        },
        "sp12": {
            "spec": "round",
            "bonus": 10
        }
    }

    boardSH = {
        "sp13": {
            "spec": "back",
            "bonus": None,
            "dir": 1
        },
        "sp14": {
            "spec": "unluckExtra",
            "bonus": list(range(-10, -41, -3))
        },
        "sp15": {
            "spec": None,
            "bonus": -3
        },
        "sp16": {
            "spec": None,
            "bonus": -3
        },
        "sp17": {
            "spec": None,
            "bonus": 3
        },
        "sp18": {
            "spec": "star",
            "bonus": None,
            "occupied": True
        },
        "sp19": {
            "spec": None,
            "bonus": -3
        },
        "sp20": {
            "spec": "unluckExtra",
            "bonus": list(range(-10, -41, -3))
        },
        "sp21": {
            "spec": None,
            "bonus": -3
        },
        "sp22": {
            "spec": "round",
            "bonus": 10
        },
        "sp23": {
            "spec": None,
            "bonus": 3,
            "dir": 1
        },
        "sp24": {
            "spec": "chance",
            "bonus": None
        }
    }

    return boardFH, boardSH


def unlucky():
    boardFH = {
        "sp01": {
            "spec": None,
            "bonus": 3
        },
        "sp02": {
            "spec": None,
            "bonus": 3,
        },
        "sp03": {
            "spec": "luck",
            "bonus": list(range(10, 21, 2)),
            "dir": 2
        },
        "sp04": {
            "spec": None,
            "bonus": -3
        },
        "sp05": {
            "spec": "luck",
            "bonus": list(range(10, 21, 2)),
            "dir": 2
        },
        "sp06": {
            "spec": "chance",
            "bonus": None,
        },
        "sp07": {
            "spec": None,
            "bonus": 3
        },
        "sp08": {
            "spec": "star",
            "bonus": None,
            "occupied": False
        },
        "sp09": {
            "spec": "luck",
            "bonus": list(range(10, 21, 2))
        },
        "sp10": {
            "spec": "unluck",
            "bonus": list(range(-10, -21, -2))
        },
        "sp11": {
            "spec": None,
            "bonus": None
        },
        "sp12": {
            "spec": "round",
            "bonus": 10
        }
    }

    boardSH = {
        "sp13": {
            "spec": "back",
            "bonus": None,
            "dir": 1
        },
        "sp14": {
            "spec": "luckExtra",
            "bonus": list(range(10, 41, 3))
        },
        "sp15": {
            "spec": None,
            "bonus": 3
        },
        "sp16": {
            "spec": None,
            "bonus": -3
        },
        "sp17": {
            "spec": None,
            "bonus": 3
        },
        "sp18": {
            "spec": "star",
            "bonus": None,
            "occupied": True
        },
        "sp19": {
            "spec": None,
            "bonus": 3
        },
        "sp20": {
            "spec": "luckExtra",
            "bonus": list(range(10, 41, 3))
        },
        "sp21": {
            "spec": None,
            "bonus": -3
        },
        "sp22": {
            "spec": "round",
            "bonus": 10
        },
        "sp23": {
            "spec": None,
            "bonus": 3,
            "dir": 1
        },
        "sp24": {
            "spec": "chance",
            "bonus": None
        }
    }

    return boardFH, boardSH



def createBoards(board):
    if str(board) == "1":
        boardT = balanced()
    elif str(board) == "2":
        boardT = lucky()
    elif str(board) == "3":
        boardT = unlucky()
    
    return boardT




