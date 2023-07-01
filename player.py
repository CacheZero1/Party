# Main Player Class
class Player():
    def __init__(self, name, number) -> None:
        self.name = name
        self.money = 0
        self.rubies = 0
        self.layer = 0
        self.number = number
        self.symbol = str(number)