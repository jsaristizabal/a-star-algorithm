import time
import os
import random
import sys
import numpy as np
from queue import PriorityQueue

#np.random.seed(60)#60

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

    global start,goal

    start = generate_xy(init_grid)
    goal = generate_xy(init_grid)

    full_grid = init_grid.copy()

    #verificamos que sean diferentes
    while start == goal:
        start = start = generate_xy(init_grid)
    
    #start = (3,3)#####################
    #goal = (0,0)###################
    
    full_grid[start[0]][start[1]] = 2
    full_grid[goal[0]][goal[1]] = 3

    #grid[x-1,y-1] = 3
    return full_grid

def full_grid(m,n,prob):
    init_grid = create_initial_grid(m,n,prob) #matriz de 0 y 1
    full_grid = place_points(init_grid)     #matriz con modificaciones
    return full_grid



def manhattan_Dist(p1,p2):     #usando la distancia manhattan
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x2-x1) + abs(y2-y1))


def h(n):
    """
    h(n): Es la funcion heuristica que estima el camino mas corto desde n hasta el FINAL
    """

    return manhattan_Dist(n,goal)

def g(n):
    """
    g(n): es el costo del camino desde el INICIO hasta n
    """
    return manhattan_Dist(start,n)


def f(n):
    return (g(n) + h(n))

def update_neighbors(current,grid):
    # print(grid)
    # print(start)
    
    grid_map = [(i,j) for i in range(grid.shape[0]) for j in range(grid.shape[1])] #ubicamos las coordenadas
    #print(grid_map)
    neighbors = []
    
    x = current[0]
    y = current[1]

    max_X = grid.shape[0]-1
    max_Y = grid.shape[1]-1


    if x < max_X and not grid[x + 1 ][y] == 1:  #ABAJO
        neighbors.append((x + 1,y))

    if x > 0 and not grid[x - 1 ][y] == 1:  #ARRIBA
        neighbors.append((x - 1,y))

    if y < max_Y and not grid[x][y + 1] == 1:  #DERECHA
        neighbors.append((x,y + 1))

    if y > 0 and not grid[x][y - 1] == 1:  #IZQUIERDA
        neighbors.append((x,y - 1))
    #print(f"start: {start}")
    return neighbors # tenemos una lista de tuplas [ (row,col),(row,col)....] recordar que las coordenadas son desde grid[0][0]



def aStar(grid):
    
    
    open = PriorityQueue()
    #open.put((f(count_n),count_n,start))    #guarda el f_cost , count_n , posicion
    #open_list.append((0,count_n,start))    #guarda el f_cost , count_n , posicion
    open_set_hash = {start}
    a_Path = {}
    open.put( (f(start),h(start), start) )
    
    hashable = [(i,j) for i in range(grid.shape[0]) for j in range(grid.shape[1])]
    
    g_cost = {row:float('inf') for row in hashable}  # Costo g acumulado para cada nodo
    g_cost[start] = 0                                #start es una variable globar en forma de (x,y)

    f_cost = {row:float('inf') for row in hashable}  # Costo f acumulado para cada nodo
    f_cost[start] = h(start)                            #start es una variable globar en forma de (x,y)


    while not open.empty():

        actualPos = open.get()[2]
        #open_set_hash.remove(actualPos) #to prevent duplicates

        if actualPos == goal:   #si se llegó al objetivo: romper el ciclo
            break

        neighbors = update_neighbors(actualPos,grid)
        #print(f"vecinos {neighbors}")

        
        for index,neighbor in enumerate(neighbors):
            

            temp_g = g(neighbor) +1
            temp_f = temp_g + h(neighbor)

            if temp_g < g_cost[neighbor]:
                g_cost[neighbor] = temp_g
                f_cost[neighbor] = temp_f
                open.put( (temp_f , h(neighbor) , neighbor) )
                a_Path[neighbor] = actualPos                #reverse path
    #print(a_Path)

    fwdPath = {}
    aux_goal = goal
    while aux_goal != start:
         #print(f"auxgoal{aux_goal}")
         fwdPath[a_Path[aux_goal]] = aux_goal
         aux_goal = a_Path[aux_goal]

    return a_Path, fwdPath
        
                



    

    #return g_cost






def print_grid(grid):
    
    rows, cols = grid.shape
    out_str = ""
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                out_str += "\u00B7 "    #punto medio usando unicode
            
            elif grid[i][j] == 1:
                out_str += "x "
            
            elif grid[i][j] == 2:
                out_str += "S "

            elif grid[i][j] == 3:
                out_str += "G "



        out_str += "\n\r"
    print(out_str)

    
def update_grid(path):
    pos = start

    print(f"camino:{path} de longitud {len(path)}\n")
    

    for i in range(len(path)):

        

        step_i = path[pos]
        print(step_i)
        pos = step_i

    

def run(m,n,prob=5):
    clear_console()
    grid = full_grid(m,n,prob)
    print(f"Start point : {start}")
    print(f"End point : {goal}\n")
    
    print_grid(grid)

    aPath,fwdPath = aStar(grid)

    update_grid(fwdPath)

    #print(aPath)
    # print(fwdPath)

    #update_neighbors(start,grid)



if __name__ == '__main__':
    run(4,4)