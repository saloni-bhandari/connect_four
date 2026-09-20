from enum import Enum

class Player(Enum):
    RED = 1
    YELLOW = 2

    @property
    def opponent(self) -> "Player":
        return Player.YELLOW if self is Player.RED else Player.RED