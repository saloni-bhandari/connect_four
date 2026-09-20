from connect_four.game_logic.game_state import GameState
from connect_four.game_logic.board import Board
from connect_four.game_logic.player import Player

initial_game_state = GameState(board=Board.empty(), current_player=None, moves=())
print(initial_game_state)

def play_game(game_state: GameState) -> GameState:
    return game_state