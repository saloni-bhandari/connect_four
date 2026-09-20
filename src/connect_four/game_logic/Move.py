from dataclasses import dataclass


@dataclass(frozen=True)
class Move:
    column: int
    player: int 