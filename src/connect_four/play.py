from connect_four.game_logic.game_state import GameState
from connect_four.game_logic.board import Board
from connect_four.game_logic.player import Player
from connect_four.game_logic.status import Status
from connect_four.cli.render import render_board
from connect_four.cli.input import ask_for_column

def play_game(game_state: GameState):
    while game_state.status == Status.IN_PROGRESS:
        print(render_board(game_state.board))
        column = ask_for_column(game_state)
        game_state = GameState.apply_move(game_state, column)

initial_game_state = GameState(board=Board.empty(10,10), current_player=Player.RED, moves=(), status=Status.IN_PROGRESS)
play_game(initial_game_state)