from connect_four.game_logic.board import Board
from connect_four.game_logic.player import Player

SYMBOLS = {None: ".", Player.RED: "R", Player.YELLOW: "Y"}

def render_board(board: Board) -> str:
    rows = [" ".join(SYMBOLS[cell] for cell in row) for row in board.cells]
    footer = " ".join(str(c + 1) for c in range(board.columns))
    return "\n".join(rows + [footer])