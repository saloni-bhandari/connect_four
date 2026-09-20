from dataclasses import dataclass

from connect_four.game_logic.Piece import Piece

@dataclass
class Board:
    rows: int
    columns: int
    board: tuple[tuple[int, ...], ...]
    pieces: tuple[Piece, ...] = tuple()

    @classmethod
    def create_empty_board(cls, rows: int, columns: int) -> "Board":
        empty_board = tuple(tuple(0 for _ in range(columns)) for _ in range(rows))
        return cls(rows, columns, empty_board)
    