from __future__ import annotations
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

    def is_column_valid(self, column: int) -> bool:
        return 0 <= column < self.columns

    def is_column_full(self, column: int) -> bool:
        return self.cells[0][column] is not None

    def lowest_empty_row(self, column: int) -> int | None:
        for row in reversed(range(self.rows)):
            if self.cells[row][column] is None:
                return row
        return None

    def drop_piece(self, column: int, player: Player) -> Board:
        if not self.is_column_valid(column):
            raise ValueError(f"Column {column} is invalid.")
        if self.is_column_full(column):
            raise ValueError(f"Column {column} is full.")

        row = self.lowest_empty_row(column)
        if row is None:
            raise ValueError(f"Column {column} is full.")
        else:
            new_cells = [list(row) for row in self.cells]
            new_cells[row][column] = player
            return Board(tuple(tuple(row) for row in new_cells))