from dataclasses import dataclass

from connect_four.game_logic import Player
from connect_four.game_logic.Board import Board

@dataclass(frozen=True)
class GameState:
    board: Board
    current_player: Player
    moves: tuple

    def __init__(self, rows, columns):
        self.board = Board.create_empty_board(rows, columns)
        self.current_player = Player.RED
        self.moves = tuple()  # Store moves as a tuple of (column, player)