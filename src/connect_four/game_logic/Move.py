from dataclasses import dataclass

from connect_four.game_logic import Player


@dataclass(frozen=True)
class Move:
    column: int
    player: Player