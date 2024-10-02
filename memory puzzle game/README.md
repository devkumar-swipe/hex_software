# Memory Puzzle Game

### Developed by Dev Kumar | Internship Project at Hex Software

The **Memory Puzzle Game** is a simple memory game built using Python and PyQt5. The player is tasked with matching pairs of cards within a time limit of 20 seconds.

## Features

- **Card Matching**: Players click on cards to reveal their values and attempt to match pairs.
- **Time Limit**: Players have 20 seconds to match all pairs of cards.
- **Automatic Restart**: The game automatically reshuffles and restarts after a win or when the timer runs out.

## Requirements

- Python 3.x
- PyQt5 (`pip install pyqt5`)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/devkumar-swipe/hex_software/memory-puzzle-game.git
    cd memory-puzzle-game
    ```

2. **Install the required dependencies**:
    ```bash
    pip install pyqt5
    ```

## How to Play

1. Run the application:
    ```bash
    python memory_puzzle.py
    ```

2. The game window will display a 2x3 grid of cards. Each card is hidden by default and marked with a question mark (`?`).

3. Click on any two cards to reveal them. If the cards match, they will stay revealed. If they don't match, the cards will be hidden again after a short delay.

4. You win if you match all three pairs of cards before the 20-second timer runs out.

5. If you run out of time, the game will display a "Time's Up!" message and automatically restart.

6. If you win, the game will congratulate you with a "You Win!" message and restart with a reshuffled deck.


## info
feel free to ask  any doubts regarding this project 
devkumar@cyberswipe.in


