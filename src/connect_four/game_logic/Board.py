from dataclasses import dataclass

from connect_four.game_logic.player import Player

Cell = Player | None

@dataclass(frozen=True)
class Board:
    cells: tuple[tuple[Cell, ...], ...]

    @classmethod
    def empty(cls, rows: int = 6, columns: int = 7) -> "Board":
        return cls(tuple(tuple(None for _ in range(columns)) for _ in range(rows)))

    @property
    def rows(self) -> int:
        return len(self.cells)

    @property
    def columns(self) -> int:
        return len(self.cells[0])