import tkinter as tk
from tkinter import font


class TicTacToe:
    def __init__(self, master):
        self.game_result = None
        self.reset_button = None
        self.labels = None
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.geometry("300x400")
        self.master.resizable(False, False)
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.create_widgets()

    def create_widgets(self):
        title_font = font.Font(family='Helvetica', size=24, weight='bold')
        label_font = font.Font(family='Helvetica', size=16, weight='bold')
        button_font = font.Font(family='Helvetica', size=14, weight='bold')

        title_label = tk.Label(self.master, text="Tic Tac Toe", font=title_font)
        title_label.pack(pady=10)

        board_frame = tk.Frame(self.master)
        board_frame.pack()

        self.labels = [[tk.Label(board_frame, text=' ', width=4, height=2, font=label_font,
                                 bg='#f2f2f2', relief="groove", borderwidth=2)
                        for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.labels[i][j].grid(row=i, column=j, padx=5, pady=5)
                self.labels[i][j].bind("<Button-1>", lambda event, row=i, col=j: self.player_move(row, col))

        self.reset_button = tk.Button(self.master, text="Reset Game", font=button_font,
                                      command=self.reset_game, state='disabled',
                                      bg='#f2f2f2', relief="groove", borderwidth=2)
        self.reset_button.pack(pady=10)

        self.game_result = tk.Label(self.master, text="", font=label_font)
        self.game_result.pack(pady=10)

    def player_move(self, row, col):
        if not self.game_over and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.labels[row][col].config(text=self.current_player, state='disabled')
            winner = self.check_win(self.current_player)
            if winner:
                self.game_result.config(text=f"Player {self.current_player} wins! Congratulations!", fg='#4CAF50')
                self.disable_all_labels()
                self.game_over = True
                self.reset_button.config(text="Play Again", state='normal')
            elif self.check_draw():
                self.game_result.config(text="It's a draw!", fg='#f44336')
                self.disable_all_labels()
                self.game_over = True
                self.reset_button.config(text="Play Again", state='normal')
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.computer_move()
                self.print_board()

    def computer_move(self):
        best_score = float('-inf')
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ' '

                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            row, col = best_move
            self.board[row][col] = 'O'
            self.labels[row][col].config(text='O', state='disabled')

            winner = self.check_win('O')
            if winner:
                self.game_result.config(text="Computer wins! Better luck next time!", fg='#f44336')
                self.disable_all_labels()
                self.game_over = True
                self.reset_button.config(text="Play Again", state='normal')
            elif self.check_draw():
                self.game_result.config(text="It's a draw!", fg='#f44336')
                self.disable_all_labels()
                self.game_over = True
                self.reset_button.config(text="Play Again", state='normal')
            else:
                self.current_player = 'X'
                self.print_board()

    def minimax(self, board, depth, is_maximizing):
        if self.check_win('O'):
            return 1
        if self.check_win('X'):
            return -1
        if self.check_draw():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = ' '
                        best_score = min(score, best_score)
            return best_score

    def check_win(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def disable_all_labels(self):
        for i in range(3):
            for j in range(3):
                self.labels[i][j].config(state='disabled')

    def reset_game(self):
        self.game_over = False
        self.game_result.config(text="")
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.labels[i][j].config(text=' ', state='normal')
        self.current_player = 'X'
        self.print_board()
        self.reset_button.config(text="Reset Game", state='disabled')

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end=' ')
            print()
        print()


root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
