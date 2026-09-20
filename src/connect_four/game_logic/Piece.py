from dataclasses import dataclass

@dataclass(frozen=True)
class Piece:
    player: int
    position: tuple