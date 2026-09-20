from enum import Enum

class Status(Enum):
    IN_PROGRESS : str = "In Progress"
    RED_WINS : str = "Red Wins"
    YELLOW_WINS : str = "Yellow Wins"
    DRAW : str = "Draw"