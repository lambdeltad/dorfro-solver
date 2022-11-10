"""Main file."""
import logging.config
import os

from board import Board
from window import Window

logging.config.fileConfig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "logging.conf"))


def main():
    """Main function."""
    board = Board()
    Window(board)


if __name__ == '__main__':
    main()

# For 5/6 matches, consider exclusive edge matches
