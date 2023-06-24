def getBeachIslands(playerNr, playerField):
    """Get the Beach Islands map

    Args:
        playerNr (int): return the coords for player number
        playerField (int): search field data for coords
    """
    beachIslandsMap = {
        "sp1": {
            "coords1": (19, 32),
            "coords2": (20, 32),
            "coords3": (19, 33),
            "coords4": (20, 33),
            "bonus": 3,
            "spec": None,
        },
        
        "sp2": {
            "coords1": (25, 29),
            "coords2": (26, 29),
            "coords3": (25, 30),
            "coords4": (26, 30),
            "bonus": 3,
            "spec": None,
        },
        
        "sp3": {
            "coords1": (30, 33),
            "coords2": (31, 33),
            "coords3": (30, 34),
            "coords4": (31, 34),
            "bonus": 3,
            "spec": None,
        },
        
        "sp4": {
            "coords1": (35, 28),
            "coords2": (36, 28),
            "coords3": (35, 29),
            "coords4": (36, 29),
            "bonus": 0,
            "spec": ("bridge", 103),
        },
        
        "sp5": {
            "coords1": (37, 22),
            "coords2": (38, 22),
            "coords3": (37, 23),
            "coords4": (38, 23),
            "bonus": 0,
            "spec": ("lucky", list(range(1, 31)).append(-10)),
        },
        
        "sp6": {
            "coords1": (33, 11),
            "coords2": (34, 11),
            "coords3": (33, 12),
            "coords4": (34, 12),
            "bonus": 0,
            "spec": ("bridge", 100),
        },
        
        "sp7": {
            "coords1": (29, 6),
            "coords2": (30, 6),
            "coords3": (29, 7),
            "coords4": (30, 7),
            "bonus": 0,
            "spec": ("chance", list(range(-50, 51))),
        },
        
        "sp8": {
            "coords1": (21, 10),
            "coords2": (22, 10),
            "coords3": (21, 11),
            "coords4": (22, 11),
            "bonus": 3,
            "spec": None,
        },
        
        "sp9": {
            "coords1": (16, 7),
            "coords2": (17, 7),
            "coords3": (16, 8),
            "coords4": (17, 8),
            "bonus": 0,
            "spec": ("ruby", -30),
        },
        
        "sp10": {
            "coords1": (13, 13),
            "coords2": (14, 13),
            "coords3": (13, 14),
            "coords4": (14, 14),
            "bonus": 3,
            "spec": None,
        },
        
        "sp11": {
            "coords1": (10, 20),
            "coords2": (11, 20),
            "coords3": (10, 21),
            "coords4": (11, 21),
            "bonus": 3,
            "spec": ("unlucky", list(range(-1, -31)).append(10)),
        },
        
        "sp12": {
            "coords1": (6, 25),
            "coords2": (7, 25),
            "coords3": (6, 26),
            "coords4": (7, 26),
            "bonus": 3,
            "spec": None,
        },
        
        "sp13": {
            "coords1": (10, 35),
            "coords2": (11, 35),
            "coords3": (10, 36),
            "coords4": (11, 36),
            "bonus": 0,
            "spec": ("round", 10),
        },
        
        
        
        "sp100": {
            "coords1": (43, 11),
            "coords2": (44, 11),
            "coords3": (43, 12),
            "coords4": (44, 12),
            "bonus": 0,
            "spec": ("bridge", 6),
        },
        
        "sp101": {
            "coords1": (42, 18),
            "coords2": (43, 18),
            "coords3": (42, 19),
            "coords4": (43, 19),
            "bonus": 3,
            "spec": None,
        },
        
        "sp102": {
            "coords1": (45, 24),
            "coords2": (46, 24),
            "coords3": (45, 25),
            "coords4": (46, 25),
            "bonus": 0,
            "spec": ("unlucky", list(range(-1, -31)).append(10)),
        },
        
        "sp103": {
            "coords1": (42, 28),
            "coords2": (43, 28),
            "coords3": (42, 29),
            "coords4": (43, 29),
            "bonus": 0,
            "spec": ("bridge", 4),
        },
        
        "sp104": {
            "coords1": (39, 34),
            "coords2": (40, 34),
            "coords3": (39, 35),
            "coords4": (40, 35),
            "bonus": 3,
            "spec": None,
        },
        
        "sp105": {
            "coords1": (45, 39),
            "coords2": (46, 39),
            "coords3": (45, 40),
            "coords4": (46, 40),
            "bonus": -3,
            "spec": None,
        },
        
        "sp106": {
            "coords1": (53, 41),
            "coords2": (54, 41),
            "coords3": (53, 42),
            "coords4": (54, 42),
            "bonus": 3,
            "spec": None,
        },
        
        "sp107": {
            "coords1": (60, 36),
            "coords2": (61, 36),
            "coords3": (60, 37),
            "coords4": (61, 37),
            "bonus": 0,
            "spec": ("lucky", list(range(1, 31)).append(-10)),
        },
        
        "sp108": {
            "coords1": (57, 29),
            "coords2": (58, 29),
            "coords3": (57, 30),
            "coords4": (58, 30),
            "bonus": 3,
            "spec": None,
        },
        
        "sp109": {
            "coords1": (57, 21),
            "coords2": (58, 21),
            "coords3": (57, 22),
            "coords4": (58, 22),
            "bonus": 0,
            "spec": ("chance", list(range(-50, 50))),
        },
        
        "sp110": {
            "coords1": (60, 12),
            "coords2": (61, 12),
            "coords3": (60, 13),
            "coords4": (61, 13),
            "bonus": 0,
            "spec": ("ruby", -30),
        },
        
        "sp111": {
            "coords1": (53, 8),
            "coords2": (54, 8),
            "coords3": (53, 9),
            "coords4": (54, 9),
            "bonus": 3,
            "spec": None,
        },
        
        "sp112": {
            "coords1": (47, 6),
            "coords2": (48, 6),
            "coords3": (47, 7),
            "coords4": (48, 7),
            "bonus": 0,
            "spec": ("round", 10),
        },
    }
    
    return beachIslandsMap["sp" + str(playerField)]["coords" + str(playerNr)], beachIslandsMap["sp" + str(playerField)]


def getMineShafts():
    mineShaftsMap = {}
    

def getGardenLabyrinth():
    gardenLabyrinthMap = {}
    

def getMansionHalls():
    mansionHallsMap = {}