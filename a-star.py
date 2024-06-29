import time
import os
import random
import sys
import numpy as np

# np.random.seed(1982)

def clear_console():
    """
    Clears the console using a system command based on the user's operating system.
    """

    if sys.platform.startswith('win'):
        os.system("cls")
    elif sys.platform.startswith('linux'):
        os.system("clear")
    elif sys.platform.startswith('darwin'):
        os.system("clear")
    else:
        print("Unable to clear terminal. Your operating system is not supported.\n\r")



def create_initial_grid(rows,cols,prob):
    grid = []
    for row in range(rows):
        grid_rows = []
        for col in range(cols):
            if np.random.randint(0,prob) == 0:
                grid_rows += [1]
            else:
                grid_rows += [0]
        grid += [grid_rows]
    return np.array(grid)


def generate_xy(grid):
    rows, cols = grid.shape
    x = np.random.randint(0,rows)
    y = np.random.randint(0,cols)
    return (x,y)

def place_points(init_grid):
    full_grid = init_grid.copy()

    start = generate_xy(init_grid)
    goal = generate_xy(init_grid)

    #verificamos que sean diferentes
    while start == goal:
        start = start = generate_xy(init_grid)

    full_grid[start[0] - 1][start[1] - 1] = 2
    full_grid[goal[0] - 1][goal[1] - 1] = 3

    #grid[x-1,y-1] = 3
    return full_grid

def full_grid(m,n,prob):
    init_grid = create_initial_grid(m,n,prob) #matriz de 0 y 1
    full_grid = place_points(init_grid)     #matriz con modificaciones
    return full_grid



def h(p1,p2):
    x1,y1 = p1
    y2,y2 = p2
    return abs(x2-x1) + abs(y2-y1)





def print_grid(m,n, prob):
    grid = full_grid(m,n,prob)
    rows, cols = grid.shape
    out_str = ""
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                out_str += "\u00B7 "    #punto medio usando unicode

            elif grid[i][j] ==1:
                out_str += "x "

            elif grid[i][j] ==2:
                out_str += "S "

            elif grid[i][j] ==3:
                out_str += "G "



        out_str += "\n\r"
    print(out_str)




def run(m,n,prob=5):
    clear_console()
    print_grid(m,n,prob)



if __name__ == '__main__':
    run(20,30)