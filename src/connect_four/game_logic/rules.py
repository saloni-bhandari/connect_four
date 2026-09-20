from connect_four.game_logic.board import Board
from connect_four.game_logic.player import Player
from connect_four.game_logic.move import Move
from connect_four.game_logic.status import Status

DIRECTIONS = [(0, 1), (1, 0), (1, 1), (1, -1)] 

def _count_consecutive_pieces(board: Board, player: Player, row: int, column: int, dr: int, dc: int) -> int:
    count = 0
    r, c = row + dr, column + dc
    while 0 <= r < board.rows and 0 <= c < board.columns and board.cells[r][c] == player:
        count += 1
        r += dr
        c += dc
    return count

def is_winning_move(board, player, row, column):
    for dr, dc in DIRECTIONS:
        count = 1 + _count_consecutive_pieces(board, player, row, column, dr, dc) + _count_consecutive_pieces(board, player, row, column, -dr, -dc)
        if count >= 4:
            return True

    return False  


def get_status(board: Board, last_move: Move, row: int) -> Status:
    if is_winning_move(board, last_move.player, row, last_move.column):
        return Status.RED_WINS if last_move.player == Player.RED else Status.YELLOW_WINS
    elif board.is_full():
        return Status.DRAW
    else:
        return Status.IN_PROGRESS