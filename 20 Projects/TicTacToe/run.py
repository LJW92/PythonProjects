import tkinter as tk
from tkinter import font
from typing import NamedTuple


class Player(NamedTuple):
    label: str
    color: str


class Move(NamedTuple):
    row: int
    col: int
    label: str = ""


BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="green")
)


class Game:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self.players = players
        self.board_size = board_size
        self.current_player = self.players[0]
        self.winner_combo = []
        self._current_moves = [[Move(row, col) for col in range(self.board_size)] for row in range(self.board_size)]
        self._winning_combos = self._get_winning_combos()
        self._has_winner = False

    def _get_winning_combos(self):
        rows = [[(row, col) for col in range(self.board_size)] for row in range(self.board_size)]
        columns = [[(row, col) for row in range(self.board_size)] for col in range(self.board_size)]
        diagonals = [
            [(i, i) for i in range(self.board_size)],
            [(i, self.board_size - i - 1) for i in range(self.board_size)]
        ]
        return rows + columns + diagonals

    def is_valid_move(self, move):
        row, col = move.row, move.col
        return not self._has_winner and self._current_moves[row][col].label == ""

    def process_move(self, move):
        row, col = move.row, move.col
        self._current_moves[row][col] = move
        for combo in self._winning_combos:
            results = {self._current_moves[n][m].label for n, m in combo}
            if len(results) == 1 and "" not in results:
                self._has_winner = True
                self.winner_combo = combo
                break

    def has_winner(self):
        return self._has_winner

    def is_tied(self):
        return not self._has_winner and all(move.label for row in self._current_moves for move in row)

    def toggle_player(self):
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def reset_game(self):
        self.current_player = self.players[0]
        self._current_moves = [[Move(row, col) for col in range(self.board_size)] for row in range(self.board_size)]
        self._has_winner = False
        self.winner_combo = []

    def ai_move(self):
        if self.current_player.label == "O":
            best_score = -float("inf")
            best_move = None

            for row in range(self.board_size):
                for col in range(self.board_size):
                    if self._current_moves[row][col].label == "":
                        self._current_moves[row][col] = Move(row, col, self.current_player.label)
                        score = self.minimax(self._current_moves, 0, False)
                        self._current_moves[row][col] = Move(row, col, "")

                        if score > best_score:
                            best_score = score
                            best_move = (row, col)

            return best_move

        return None

    def minimax(self, board, depth, is_maximizing):
        scores = {
            "X": -1,
            "O": 1,
            "": 0
        }

        result = self.check_winner(board)
        if result is not None:
            return scores[result]

        if is_maximizing:
            best_score = -float("inf")
            for row in range(self.board_size):
                for col in range(self.board_size):
                    if board[row][col].label == "":
                        board[row][col] = Move(row, col, self.current_player.label)
                        score = self.minimax(board, depth + 1, False)
                        board[row][col] = Move(row, col, "")
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for row in range(self.board_size):
                for col in range(self.board_size):
                    if board[row][col].label == "":
                        board[row][col] = Move(row, col, self.get_opponent(self.current_player.label))
                        score = self.minimax(board, depth + 1, True)
                        board[row][col] = Move(row, col, "")
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, board):
        for combo in self._winning_combos:
            results = {board[row][col].label for row, col in combo}
            if len(results) == 1 and "" not in results:
                return results.pop()
        return None

    def get_opponent(self, player_label):
        return "X" if player_label == "O" else "O"


class TicTacToeBoard(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title("Tic Tac Toe Game")
        self._cells = {}
        self._game = game
        self.create_menu()
        self.create_board()

    def create_menu(self):
        menu_bar = tk.Menu(master=self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(master=menu_bar)
        file_menu.add_command(label="Play Again", command=self.reset_board)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def create_board(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold")
        )
        self.display.pack()

        board_grid = tk.Frame(master=self)
        board_grid.pack()
        for row in range(self._game.board_size):
            self.rowconfigure(row, minsize=50, weight=1)
            self.columnconfigure(row, minsize=75, weight=1)
            for col in range(self._game.board_size):
                button = tk.Button(
                    master=board_grid,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue"
                )
                self._cells[(row, col)] = button
                self._cells[button] = (row, col)
                button.bind("<ButtonPress-1>", self.play)
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def play(self, event):
        if self._game.has_winner() or self._game.is_tied():
            return

        clicked_btn = event.widget
        row, col = self._cells[clicked_btn]
        move = Move(row, col, self._game.current_player.label)
        if self._game.is_valid_move(move):
            self.update_button(clicked_btn)
            self._game.process_move(move)

            if self._game.has_winner():
                self.highlight_winning_combo()
                self.update_display(f"Player {self._game.current_player.label} wins!", self._game.current_player.color)
            elif self._game.is_tied():
                self.update_display("It's a tie!", "red")
            else:
                self._game.toggle_player()
                self.update_display(f"{self._game.current_player.label}'s turn")

                if self._game.current_player.label == "O":
                    self.ai_move()

    def ai_move(self):
        ai_move = self._game.ai_move()
        if ai_move:
            ai_row, ai_col = ai_move
            ai_button = self._cells[(ai_row, ai_col)]
            self.update_button(ai_button)
            self._game.process_move(Move(ai_row, ai_col, self._game.current_player.label))

            if self._game.has_winner():
                self.highlight_winning_combo()
                self.update_display(f"Player {self._game.current_player.label} wins!", self._game.current_player.color)
            elif self._game.is_tied():
                self.update_display("It's a tie!", "red")
            else:
                self._game.toggle_player()
                self.update_display(f"{self._game.current_player.label}'s turn")

    def update_button(self, clicked_btn):
        clicked_btn.config(text=self._game.current_player.label)
        clicked_btn.config(fg=self._game.current_player.color)
        clicked_btn.config(state="disabled")

    def highlight_winning_combo(self):
        for row, col in self._game.winner_combo:
            winning_button = self._cells[(row, col)]
            winning_button.config(highlightbackground="red")

    def update_display(self, msg, color="black"):
        self.display["text"] = msg
        self.display["fg"] = color

    def reset_board(self):
        for button in self._cells.values():
            button.config(state="active")
            button.config(text="")
            button.config(fg="black")
            button.config(highlightbackground="lightblue")
        self._game.reset_game()
        self.update_display("Ready?")


if __name__ == "__main__":
    game = Game()
    board = TicTacToeBoard(game)
    board.mainloop()
