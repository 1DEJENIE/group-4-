import random

def create_crossword(words):
                # Determine the size of the grid based on the longest word
    max_len = max(len(word) for word in words)
    grid_size = max_len + 2  # Add padding for borders

    # Initialize an empty grid
    
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

    # Place words horizontally or vertically randomly
for word in words: 
        if random.choice([True, False]):  # Place horizontally 
            placed = False 
            while not placed: 
                row = random.randint(1, grid_size - 2)  # Random row (excluding borders) 
                col = random.randint(1, grid_size - len(word) - 1)  # Random starting column 
                if all(grid[row][col+i] == ' ' for i in range(len(word))): 
                    for i, letter in enumerate(word): 
                        grid[row][col + i] = letter 
                    placed = True
                    
        else:  # Place vertically
            placed = False
            while not placed:
                row = random.randint(1, grid_size - len(word) - 1)  # Random starting row
                col = random.randint(1, grid_size - 2)  # Random column (excluding borders)
                if all(grid[row+i][col] == ' ' for i in range(len(word))):
                    for i, letter in enumerate(word):
                        grid[row + i][col] = letter
                    placed = True
                  
