# Tic-Tac-Toe AI: Minimax and Alpha-Beta Pruning

## About
This project implements a Tic-Tac-Toe game featuring two powerful AI strategies:

- **Minimax Algorithm**: Plays optimally by exploring all possible moves.
- **Minimax with Alpha-Beta Pruning**: An optimized version that cuts off unnecessary branches, improving speed.

## Features
- Playable Tic-Tac-Toe game (Human vs AI or AI vs AI).
- AI decision-making using either Minimax or Alpha-Beta Pruning.
- Choose to play as X (first player) or O (second player).
- Compare the performance between Minimax and Alpha-Beta Pruning after each game (number of nodes visited, time taken).
- Simple and clean console-based interface.

## How It Works

### Minimax Algorithm
The **Minimax** algorithm recursively evaluates all possible future moves to choose the optimal move, assuming both players play perfectly. It calculates the best move based on the evaluation function that assigns scores to terminal game states (win, loss, or draw).

### Alpha-Beta Pruning
**Alpha-Beta Pruning** is an optimization of the Minimax algorithm. It cuts off branches of the search tree that do not need to be explored because they cannot influence the final decision. This significantly reduces the number of nodes the algorithm needs to evaluate, improving performance without affecting the correctness of the result.

## Learning Outcomes
- Understand and implement the **Minimax algorithm** for optimal decision-making in games.
- Apply **Alpha-Beta pruning** to optimize the Minimax algorithm and reduce the number of nodes evaluated.
- Learn how AI can make decisions in simple turn-based games like Tic-Tac-Toe.

## Future Improvements
- Add difficulty levels (Easy, Medium, Hard).
- Create a GUI using **Pygame** or **Tkinter** for a more interactive experience.
- Expand the game to larger grids (e.g., 4x4, 5x5).
- Add online multiplayer functionality.
- Implement move recommendation hints for players to improve their gameplay.

## File Structure
```yaml
├── Tic-Tac-Toe AI: Minimax and Alpha-Beta Pruning.py  # Main game and AI logic
├── Video of Output.mp4                               # Demo gameplay video
├── README.md                                         # Project documentation
