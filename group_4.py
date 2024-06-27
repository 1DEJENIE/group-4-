import random

def create_crossword(words):
                # Determine the size of the grid based on the longest word
    max_len = max(len(word) for word in words)
    grid_size = max_len + 2  # Add padding for borders

    # Initialize an empty grid
    
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

    # Place words horizontally or vertically randomly
