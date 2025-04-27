import time
from math import inf
import numpy as np

class TicTacToe:
    def __init__(self, human_player=1):
        self.board = np.zeros((3, 3))  # 0=empty, 1=X, 2=O
        self.current_player = 1  # X starts
        self.human_player = human_player  # 1 for X, 2 for O
        self.ai_player = 3 - human_player
        self.nodes_visited_minimax = 0  # Minimax nodes visited
        self.nodes_visited_ab = 0  # Alpha-Beta Pruning nodes visited

    def print_board(self):
        symbols = {0: '.', 1: 'X', 2: 'O'}
        for row in self.board:
            print(' '.join(symbols[cell] for cell in row))
        print()

    def make_move(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            self.current_player = 3 - self.current_player  # Switch player (1<->2)
            return True
        return False

    def is_winner(self, player):
        for i in range(3):
            if all(self.board[i][:] == player) or all(self.board[:, i] == player):
                return True
        if (self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player) or \
           (self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player):
            return True
        return False

    def is_draw(self):
        return not any(0 in row for row in self.board)

    def game_over(self):
        return self.is_winner(1) or self.is_winner(2) or self.is_draw()

    def get_empty_cells(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == 0]

    def evaluate(self):
        if self.is_winner(1):
            return 1
        if self.is_winner(2):
            return -1
        return 0

    def minimax(self, depth, is_maximizing):
        self.nodes_visited_minimax += 1  # Increment Minimax node count
        if self.game_over():
            return self.evaluate()

        if is_maximizing:
            best_score = -inf
            for row, col in self.get_empty_cells():
                self.board[row][col] = 1
                score = self.minimax(depth + 1, False)
                self.board[row][col] = 0
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = inf
            for row, col in self.get_empty_cells():
                self.board[row][col] = 2
                score = self.minimax(depth + 1, True)
                self.board[row][col] = 0
                best_score = min(score, best_score)
            return best_score

    def minimax_ab(self, depth, is_maximizing, alpha=-inf, beta=inf):
        self.nodes_visited_ab += 1  # Increment Alpha-Beta node count
        if self.game_over():
            return self.evaluate()

        if is_maximizing:
            best_score = -inf
            for row, col in self.get_empty_cells():
                self.board[row][col] = 1
                score = self.minimax_ab(depth + 1, False, alpha, beta)
                self.board[row][col] = 0
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = inf
            for row, col in self.get_empty_cells():
                self.board[row][col] = 2
                score = self.minimax_ab(depth + 1, True, alpha, beta)
                self.board[row][col] = 0
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            return best_score

    def get_best_move_minimax(self):
        best_score = -inf if self.current_player == 1 else inf
        best_move = None
        for row, col in self.get_empty_cells():
            self.board[row][col] = self.current_player
            score = self.minimax(0, self.current_player == 2)
            self.board[row][col] = 0
            if (self.current_player == 1 and score > best_score) or (self.current_player == 2 and score < best_score):
                best_score = score
                best_move = (row, col)
        return best_move

    def get_best_move_minimax_ab(self):
        best_score = -inf if self.current_player == 1 else inf
        best_move = None
        alpha = -inf
        beta = inf
        for row, col in self.get_empty_cells():
            self.board[row][col] = self.current_player
            score = self.minimax_ab(0, self.current_player == 2, alpha, beta)
            self.board[row][col] = 0
            best_score = score if self.current_player == 1 else best_score
            if (self.current_player == 1 and score > best_score) or (self.current_player == 2 and score < best_score):
                best_score = score
                best_move = (row, col)
            if self.current_player == 1:
                alpha = max(alpha, best_score)
            else:
                beta = min(beta, best_score)
        return best_move

def play_game():
    while True:
        print("Welcome to Tic-Tac-Toe!")
        print("Menu:")
        print("1. Play game")
        print("2. Exit")
        choice = int(input("Enter choice (1 or 2): "))

        if choice == 2:
            print("Exiting the game.")
            break

        print("Choose your player:")
        print("1. X (first player)")
        print("2. O (second player)")
        human_player = int(input("Enter choice (1 or 2): "))

        print("\nSelect AI mode:")
        print("1. Human vs Minimax AI")
        print("2. Human vs Minimax with Alpha-Beta AI")
        mode = int(input("Choose game mode (1 or 2): "))

        game = TicTacToe(human_player)

        while not game.game_over():
            game.print_board()
            current = game.current_player
            symbol = 'X' if current == 1 else 'O'
            print(f"Player {symbol}'s turn")

            if current == game.human_player:
                try:
                    row, col = map(int, input("Enter row and column (0-2): ").split())
                except:
                    print("Invalid input. Try again.")
                    continue
            else:
                if mode == 1:
                    start_time = time.time()
                    game.nodes_visited_minimax = 0  # Reset node count
                    row, col = game.get_best_move_minimax()
                    minimax_time = time.time() - start_time
                    print(f"Minimax AI chooses: {row}, {col}")
                    print(f"Minimax time: {minimax_time:.6f} seconds")
                    print(f"Minimax visited {game.nodes_visited_minimax} nodes")
                elif mode == 2:
                    start_time = time.time()
                    game.nodes_visited_ab = 0  # Reset node count
                    row, col = game.get_best_move_minimax_ab()
                    ab_time = time.time() - start_time
                    print(f"Alpha-Beta AI chooses: {row}, {col}")
                    print(f"Alpha-Beta time: {ab_time:.6f} seconds")
                    print(f"Alpha-Beta visited {game.nodes_visited_ab} nodes")

            if not game.make_move(row, col):
                print("Invalid move. Try again.")

        game.print_board()
        if game.is_winner(1):
            print("X wins!")
        elif game.is_winner(2):
            print("O wins!")
        else:
            print("It's a draw!")

        # Comparison after the game
        if mode == 1 or mode == 2:
            print("\nPerformance Comparison:")
            if mode == 1:
                print(f"Minimax algorithm visited {game.nodes_visited_minimax} nodes.")
                print(f"Minimax time: {minimax_time:.6f} seconds")
            if mode == 2:
                print(f"Alpha-Beta Pruning algorithm visited {game.nodes_visited_ab} nodes.")
                print(f"Alpha-Beta time: {ab_time:.6f} seconds")

if __name__ == "__main__":
    play_game()
