from connect_four.game_logic.game_state import GameState
from connect_four.game_logic.board import Board
from connect_four.game_logic.player import Player

initial_game_state = GameState(board=Board.empty(), current_player=Player.RED, moves=())
print(initial_game_state)

def play_game(game_state: GameState) -> GameState:
    # Implement the game loop logic here
    # For example, you can prompt players for moves, update the game state, and check for win conditions.
    # This is a placeholder implementation.
    return game_state