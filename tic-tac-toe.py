import tkinter as tk
from tkinter import messagebox
from ia import ia
from player import Player  # Import the Player class

class TicTacToeWithAI:
    def __init__(self, player_name="Player"):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe with AI")
        self.root.configure(bg='#F0F0F0')

        # Create a player with the provided name
        self.player = Player(player_name)

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.title_label = tk.Label(self.root, text="Tic Tac Toe", font=('Helvetica', 18), bg='#F0F0F0')
        self.title_label.grid(row=0, column=0, columnspan=3, pady=(10, 20))

        # Display player information
        self.player_info_label = tk.Label(self.root, text=str(self.player), font=('Helvetica', 12), bg='#F0F0F0')
        self.player_info_label.grid(row=1, column=0, columnspan=3, pady=(0, 10))

        self.turn_label = tk.Label(self.root, text=f"Turn: {self.current_player}", font=('Helvetica', 12), bg='#F0F0F0')
        self.turn_label.grid(row=2, column=0, columnspan=3, pady=(0, 10))

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.root, text="", width=15, height=6,
                    command=lambda row=i, col=j: self.on_button_click(row, col)
                )
                button.grid(row=i + 3, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

    def on_button_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner(row, col):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.player.update_score(1)  # Update player score
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.switch_player()
                if self.current_player == "O":
                    self.make_ai_move()

    def check_winner(self, row, col):
        # Check row
        if all(self.board[row][i] == self.current_player for i in range(3)):
            return True
        # Check column
        if all(self.board[i][col] == self.current_player for i in range(3)):
            return True
        # Check diagonals
        if all(self.board[i][i] == self.current_player for i in range(3)) or \
           all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.turn_label.config(text=f"Turn: {self.current_player}")

    def make_ai_move(self):
        move = ia(self.board, self.current_player)
        if move:
            row, col = move
            self.on_button_click(row, col)

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")

        # Update player information label
        self.player_info_label.config(text=str(self.player))

if __name__ == "__main__":
    # Ask for player's name
    player_name = input("Enter your name: ")

    # Create an instance of TicTacToeWithAI with the player's name
    game = TicTacToeWithAI(player_name)
    game.root.mainloop()
