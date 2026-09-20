from connect_four.game_logic.board import Board
from connect_four.game_logic.player import Player
from connect_four.game_logic.status import Status

SYMBOLS = {None: ".", Player.RED: "R", Player.YELLOW: "Y"}

def render_board(board: Board) -> str:
    rows = [" ".join(SYMBOLS[cell] for cell in row) for row in board.cells]
    footer = " ".join(str(c + 1) for c in range(board.columns))
    return "\n".join([footer] + rows)

def print_status(status):
    if status == Status.RED_WINS:
        print("Player RED wins!")
    elif status == Status.YELLOW_WINS:
        print("Player YELLOW wins!")
    elif status == Status.DRAW:
        print("The game is a draw!")
        