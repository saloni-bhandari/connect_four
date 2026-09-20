from dataclasses import dataclass

from connect_four.game_logic.player import  Player
from connect_four.game_logic.board import Board
from connect_four.game_logic.move import Move

@dataclass(frozen=True)
class GameState:
    board: Board
    current_player: Player
    moves: tuple[Move,...] = ()
