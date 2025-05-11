import numpy as np
import os
import time

Rows, Cols = 20, 50

def initialize_grid():
    arr=[0,1]
    return np.random.choice(arr, size=(Rows, Cols), p=[0.5, 0.5])
def count_neighbors(grid):
    # Pad the grid with 0s on all sides for edge safety
    padded = np.pad(grid, pad_width=1, mode='constant', constant_values=0)
    neighbors = sum(np.roll(np.roll(padded, i, 0), j, 1)[1:-1, 1:-1]
                    for i in (-1, 0, 1) for j in (-1, 0, 1)
                    if not (i == 0 and j == 0))
    return neighbors
def update_grid(grid):
    neighbors = count_neighbors(grid)
    #core logic of the game
    return np.where((grid==1)&((neighbors==2)|(neighbors==3))|(grid==0) & (neighbors==3),1,0)

def display_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(' '.join(['■' if cell else ' ' for cell in row]))
   
def main():
    grid = initialize_grid()
    while True:
        display_grid(grid)
        grid=update_grid(grid)
        time.sleep(0.2)

if __name__ == "__main__":
    main()