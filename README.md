# Chess Engine

## Overview

This project is a fully functional chess engine implemented in Python using the Pygame library.

## Features

- **Graphical User Interface (GUI)**: Built with Pygame for an interactive chess experience.
- **Game Logic**: Comprehensive rules implementation including castling, en passant, and promotion.
- **Move Validation**: Ensures all moves are legal and follows chess rules.
- **Undo/Reset Functionality**: Press 'z' -> allows players to undo a move | Press 'r' -> allows players to reset the game.
- Comming soon -> **AI Opponent**: Implements various algorithms for AI, from simple heuristics to more complex strategies.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/malayashekhar/Chess-Engine-Project.git
    ```
2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the application:
    ```sh
    python main.py
    ```

## Screenshots

### Board
![Screenshot 2024-06-28 at 1 57 06 AM](https://github.com/malayashekhar/Chess-Engine-Project/assets/119888573/36a8cfe5-d416-41ee-887b-6d829de8a2dc)


### Gameplay
![Screenshot 2024-06-28 at 1 57 15 AM](https://github.com/malayashekhar/Chess-Engine-Project/assets/119888573/53e3a287-5175-4e33-b8a3-83765ad9991d)


### Valid-Moves
![Screenshot 2024-06-28 at 1 57 51 AM](https://github.com/malayashekhar/Chess-Engine-Project/assets/119888573/e126aa12-4e0d-4fee-8c48-9cf026952d6f)


### Checkmate/stalemate
![Screenshot 2024-06-28 at 1 58 52 AM](https://github.com/malayashekhar/Chess-Engine-Project/assets/119888573/268f3f4e-21bd-44c6-8a8b-5cb305eb7d3b)



## Algorithms Used


### 1. The Naive Algorithm:
- Generating all the possible moves.
- Making the move.
- Generating all the opponent's move.
- For each of the opponent's move, see if they attack your king.
- If they do attack your king, it's not a valid move.


## Acknowledgements

- Pygame community for the amazing library.
- Chess programming resources and tutorials.

---


