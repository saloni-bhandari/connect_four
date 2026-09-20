from dataclasses import dataclass

from connect_four.game_logic.player import  Player
from connect_four.game_logic.board import Board
from connect_four.game_logic.move import Move
from connect_four.game_logic.status import Status

@dataclass(frozen=True)
class GameState:
    board: Board
    current_player: Player
    moves: tuple[Move,...] 
    status: Status

    @classmethod
    def apply_move(cls, game_state: "GameState", column: int) -> "GameState":
        new_board = game_state.board.drop_piece(column, game_state.current_player)
        new_move = Move(column=column, player=game_state.current_player)
        next_player = game_state.current_player.opponent
        new_status = game_state.status  # Placeholder for status update logic
        return GameState(board=new_board, current_player=next_player, moves=game_state.moves + (new_move,), status=new_status)