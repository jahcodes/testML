#created by Jah
import tkinter as tk

# Global variables
GRID_SIZE = 25  # Size of the grid (10x10 in this example)
grid_matrix = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]  # Matrix to store the drawn squares
is_drawing = False # Flag to indicate if user is currently drawing

# Function to handle mouse button press event
def handle_press(event):
    global is_drawing
    is_drawing = True
    handle_motion(event)

# Function to handle mouse button release event
def handle_release(event):
    global is_drawing
    is_drawing = False

# Function to handle mouse motion event
def handle_motion(event):
    if is_drawing:
        cell_size = 400 // GRID_SIZE
        col = event.x // cell_size
        row = event.y // cell_size
        if 0 <= col < GRID_SIZE and 0 <= row < GRID_SIZE:
            if grid_matrix[row][col] == 0:
                grid_matrix[row][col] = 1
                canvas.itemconfig(cells[row][col], fill='black')

# Function to reset all cells to white
def reset_cells():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            grid_matrix[row][col] = 0
            canvas.itemconfig(cells[row][col], fill='white')

def handle_icon_click(i):
    if icons[i]['relief'] == tk.SUNKEN:
        icons[i]['relief'] = tk.RAISED
    else:
        for icon in icons: icon['relief'] = tk.RAISED
        icons[i]['relief'] = tk.SUNKEN

# Create a new Tkinter window
window = tk.Tk()
window.title("Grid Drawing")

# Create a canvas widget
canvas = tk.Canvas(window, width=400, height=400, borderwidth=0, highlightthickness=0)
canvas.pack()

# Create icons using buttons
icon_frame = tk.Frame(window)
icon_frame.pack()

icons = []
for i in range(10):
    icon = tk.Button(icon_frame, text=str(i), relief=tk.RAISED, command=lambda i=i: handle_icon_click(i))
    icon.pack(side=tk.LEFT, padx=10)
    icons.append(icon)

# Create a two-dimensional list to store the cell objects
cells = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]

# Create the grid cells on the canvas
cell_size = 400 // GRID_SIZE
for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        x1 = col * cell_size
        y1 = row * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        cell = canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='gray')
        cells[row][col] = cell

reset_button = tk.Button(window, text="Reset", command=reset_cells)
reset_button.pack()

# Bind event handlers for mouse events
canvas.bind('<ButtonPress-1>', handle_press)
canvas.bind('<B1-Motion>', handle_motion)
canvas.bind('<ButtonRelease-1>', handle_release)


# Start the Tkinter event loop
window.mainloop()