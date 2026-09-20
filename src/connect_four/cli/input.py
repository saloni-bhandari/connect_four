from connect_four.game_logic.game_state import GameState


def ask_for_column(game_state: GameState) -> int:
    print(f"Current player: {game_state.current_player}\n")
    while True:
        player_input = input(f"Make your move! Enter a column number (1-{game_state.board.columns}) to place your next piece!\n")
        try:
            column = int(player_input) - 1
        except ValueError:
            print("Please enter a number.")
            continue
        if not game_state.board.is_column_valid(column):
            print("That column is invalid. Please choose a column from 1 to {game_state.board.columns}.")
        elif game_state.board.is_column_full(column):
            print("That column is full. Please choose another column.")
        else:
            return column
