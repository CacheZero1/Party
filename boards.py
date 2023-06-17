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
            "dir": 1
        },
        "sp24": {
            "spec": "chance",
            "bonus": None
        }
    }

    return boardFH, boardSH


def lucky():
    board = 0
    return board


def unlucky():
    board = 0
    return board


boards = {
    "1": "Balanced",
    "2": "Lucky",
    "3": "Unlucky"
}


sections = {
    "Balanced": balanced,
    "Lucky": lucky,
    "Unlucky": unlucky
}


def createBoards(board):
    boardChoice = boards[str(board)]
    board1, board2 = sections[boardChoice]
    return board1, board2


mapart = """
. -- . -- .    . -- . -- .\n
|         |    |         |\n
.         . -- .         .\n
|         |    |         |\n
.         .    .         .\n
|         |    |         |\n
.         . -- .         .\n
|         |    |         |\n
. -- . -- .    . -- . -- .\n
     |                    \n
     .
"""