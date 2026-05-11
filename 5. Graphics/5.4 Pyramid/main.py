from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Loop through each row, starting from the base (row 0) up to the top
    for row in range(BRICKS_IN_BASE):
        
        # Calculate how many bricks are in the current row
        # Row 0 has BRICKS_IN_BASE, Row 1 has BRICKS_IN_BASE - 1, etc.
        bricks_in_row = BRICKS_IN_BASE - row
        
        # Calculate the starting Y coordinate for the current row
        # We start from the bottom of the canvas and move up
        y_start = CANVAS_HEIGHT - (BRICK_HEIGHT * (row + 1))
        
        # Calculate the starting X coordinate to center the row
        # Total width of the row is bricks_in_row * BRICK_WIDTH
        row_width = bricks_in_row * BRICK_WIDTH
        x_start = (CANVAS_WIDTH - row_width) / 2
        
        # Draw the bricks for the current row
        for i in range(bricks_in_row):
            # Calculate coordinates for the individual brick
            x1 = x_start + (i * BRICK_WIDTH)
            y1 = y_start
            x2 = x1 + BRICK_WIDTH
            y2 = y1 + BRICK_HEIGHT
            
            canvas.create_rectangle(x1, y1, x2, y2, "yellow", "black")

if __name__ == '__main__':
    main()