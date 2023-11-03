import matplotlib.pyplot as plt
import numpy as np

selected_points = []
coords = []
moves = []

grid_size = 5
grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

# Waits for click on graph
def on_click(event):
    if event.button == 1:
        x = float("{:.2f}".format(event.xdata))
        y = float("{:.2f}".format(event.ydata))
        selected_points.append((x, y))        
        plt.plot(x, y, 'ro')
        plt.draw()

# Logic
def calculate_moves(selected_points):
    def slope_sign(move1, move2):
        x = float("{:.2f}".format(move1[0]))
        y = float("{:.2f}".format(move1[1]))
        x2 = float("{:.2f}".format(move2[0]))
        y2 = float("{:.2f}".format(move2[1]))

        print(f"x:{x}, x2:{x2}, y:{y}, y2:{y2}")

        sign = np.round((y2-y)/(x2-x))

        if sign >= 1:
            return 1
        elif sign < 0:
            return -1
        else:
            return 0
    
    i = 0

    for element in selected_points:
        # x = element[0] - int(element[0])
        # y = element[1] - int(element[1])
        x = element[0]
        y = element[1]
        coords.append([x,y])

    for i in range(0, len(coords)):
        if i == (len(coords) - 1):
            break
        else:
            if (i+1) < len(coords):
                n2 = i+1 # n+1 element
            moves.append(slope_sign(coords[i], coords[n2]))
            
        
# Creates grid
def plot_grid(grid):
    plt.imshow(grid, cmap='binary', origin='upper', extent=[-0.5, grid_size - 0.5, -0.5, grid_size - 0.5])
    plt.colorbar(ticks=[0, 1])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Select target points')
    plt.xticks(range(grid_size))
    plt.yticks(range(grid_size))
    
    plt.grid(True, which='both', color='black', linewidth=2)
    plt.show()

# Main thang
def plot():
    fig, ax = plt.subplots()
    ax.imshow(grid, cmap='binary', origin='upper', extent=[-0.5, grid_size - 0.5, -0.5, grid_size - 0.5])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Select target points')
    
    ax.set_xticks(range(grid_size))
    ax.set_yticks(range(grid_size))
    
    ax.grid(True, which='both', color='black', linewidth=2)
    fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()
    calculate_moves(selected_points)
    print(moves)
