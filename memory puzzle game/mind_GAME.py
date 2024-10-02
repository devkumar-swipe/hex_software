import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QLabel, QMessageBox
)
from PyQt5.QtCore import QTimer, Qt


class MemoryPuzzle(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the game window
        self.setWindowTitle("Memory Puzzle Game")
        self.setGeometry(100, 100, 300, 300)
        
        # Central widget and grid layout
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.grid = QGridLayout(self.centralWidget)

        # Game variables
        self.cards = list(range(3)) * 2  # 3 pairs of cards
        random.shuffle(self.cards)  # Shuffle the cards

        self.buttons = []  # Store the buttons (cards)
        self.first_card = None  # Track the first revealed card
        self.second_card = None  # Track the second revealed card
        self.matched_pairs = 0  # Track matched pairs
        self.time_left = 20  # Set a 20-second timer for simplicity

        # Timer label
        self.timer_label = QLabel(f"Time Left: {self.time_left}", self)
        self.grid.addWidget(self.timer_label, 0, 0, 1, 3, Qt.AlignCenter)

        # Set up the game timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Update timer every second

        # Create the card grid (2x3 grid for 6 cards)
        self.create_grid()

    def create_grid(self):
        """Create a 2x3 grid of buttons representing the cards."""
        for i in range(2):
            for j in range(3):
                button = QPushButton("?", self)
                button.setFixedSize(100, 100)
                button.clicked.connect(lambda _, btn=button: self.reveal_card(btn))
                self.grid.addWidget(button, i + 1, j)
                self.buttons.append(button)

    def reveal_card(self, button):
        """Reveal the card when clicked."""
        index = self.buttons.index(button)

        # Ensure we only reveal cards that are still hidden
        if button.text() == "?" and self.second_card is None:
            button.setText(str(self.cards[index]))  # Reveal card value
            button.setEnabled(False)

            if self.first_card is None:
                self.first_card = button  # Store first card
            else:
                self.second_card = button  # Store second card
                self.check_match()  # Check if they match

    def check_match(self):
        """Check if the two revealed cards match."""
        if self.first_card.text() == self.second_card.text():
            # Cards match
            self.matched_pairs += 1
            self.first_card = None
            self.second_card = None

            # Check if all pairs are matched
            if self.matched_pairs == 3:
                self.show_message("You Win!", "You matched all pairs!")
        else:
            # Cards don't match, hide them after a brief pause
            QTimer.singleShot(1000, self.hide_cards)

    def hide_cards(self):
        """Hide the cards if they don't match."""
        self.first_card.setText("?")
        self.first_card.setEnabled(True)
        self.second_card.setText("?")
        self.second_card.setEnabled(True)
        self.first_card = None
        self.second_card = None

    def update_timer(self):
        """Update the countdown timer."""
        self.time_left -= 1
        self.timer_label.setText(f"Time Left: {self.time_left}")
        if self.time_left == 0:
            self.timer.stop()
            self.show_message("Time's Up!", "You ran out of time!")

    def show_message(self, title, message):
        """Display a message and restart the game."""
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()
        self.restart_game()

    def restart_game(self):
        """Restart the game by reshuffling cards and resetting variables."""
        random.shuffle(self.cards)
        self.matched_pairs = 0
        self.first_card = None
        self.second_card = None
        self.time_left = 20
        self.timer.start(1000)

        # Reset buttons to their initial state
        for button in self.buttons:
            button.setText("?")
            button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MemoryPuzzle()
    window.show()
    sys.exit(app.exec_())
