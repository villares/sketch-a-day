# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# inspired by a Processing implementation of Game of Life By Joan Soler-Adillon

SKETCH_NAME = "s121"  # 180501

add_library('gifAnimation')
from gif_exporter import *

# How likely for a cell to be alive at start (in percentage)
probabilityOfAliveAtStart = 15
cellSize = 16  # Size of cells
# Variables for timer
interval = 100
lastRecordedTime = 0
pause = False  # Pause
GIF_EXPORT = False

def setup():
    frameRate(10)
    global input
    global grid_w, grid_h
    global cells  # Array of cells
    global cellsBuffer  # Buffer while changing the others in the interations
    size(600, 600)
    colorMode(HSB)
    # Instantiate arrays
    grid_w, grid_h = int(width / cellSize), int(height / cellSize)
    cells = [[None] * grid_w for _ in range(grid_h)]
    cellsBuffer = [[None] * grid_w for _ in range(grid_h)]
    # This stroke will draw the background grid
    noFill()  # stroke(48)
    noSmooth()
    # Initialization of cells
    for x in range(grid_w):
        for y in range(grid_h):
            state = random(100)
            if state > probabilityOfAliveAtStart:
                state = 0
            else:
                state = 1
            cells[x][y] = state  # Save state of each cell
    background(0)  # Fill in black in case cells don't cover all the windows

def draw():
    background(0)
    global lastRecordedTime
    # Draw grid
    for x in range(grid_w):
        for y in range(grid_h):
            if cells[x][y] == 1:
                n = calc_neighbours(x, y)
                stroke((n*25 + frameCount) % 256, 255, 255)  # If alive
            else:
                noStroke()  # fill(dead)  # If dead
            pointy_hexagon(x * cellSize, y * cellSize, cellSize)
    # Iterate if timer ticks
    if millis() - lastRecordedTime > interval:
        if not pause:
            iteration()
            lastRecordedTime = millis()
    # Create new cells manually on pause
    if pause and mousePressed:
        # Map and adef out of bound errors
        xCellOver = int(map(mouseX, 0, width, 0, width / cellSize))
        xCellOver = constrain(xCellOver, 0, width / cellSize - 1)
        yCellOver = int(map(mouseY, 0, height, 0, height / cellSize))
        yCellOver = constrain(yCellOver, 0, height / cellSize - 1)
        # Check against cells in buffer
        if cellsBuffer[xCellOver][yCellOver] == 1:  # Cell is alive
            cells[xCellOver][yCellOver] = 0  # Kill
        else:  # Cell is dead
            cells[xCellOver][yCellOver] = 1  # Make alive
    # And then save to buffer once mouse goes up
    elif pause and not mousePressed:
        # Save cells to buffer
        # (so we opeate with one array keeping the other intact)
        for x in range(grid_w):
            for y in range(grid_h):
                cellsBuffer[x][y] = cells[x][y]
                
    global GIF_EXPORT
    if not frameCount % 20 and GIF_EXPORT:
        GIF_EXPORT = gif_export(GifMaker,
                                frames=1000,
                                delay=300,
                                filename=SKETCH_NAME)


def iteration():  # When the clock ticks
    # Save cells to buffer
    # (so we opeate with one array keeping the other intact)
    for x in range(grid_w):
        for y in range(grid_h):
            cellsBuffer[x][y] = cells[x][y]
    # Visit each cell:
    for x in range(grid_w):
        for y in range(grid_h):
            # And visit all the neighbours of each cell
            neighbours = calc_neighbours(x, y)
            if cellsBuffer[x][y] == 1:
                if neighbours < 2 or neighbours > 3:
                    cells[x][y] = 0  # Die unless it has 2 or 3 neighbours
            else:  # The cell is dead: make it live if necessary
                if neighbours == 3:
                    cells[x][y] = 1  # Only if it has 3 neighbours

def calc_neighbours(x, y):
    neighbours = 0  # We'll count the neighbours
    for xx in range(x - 1, x + 2):
        for yy in range(y - 1, y + 2):
                    # Make sure you are not out of bounds
            if 0 <= xx < grid_w and 0 <= yy < grid_w:
                # Make sure to check against self
                if not (xx == x and yy == y):
                    if cellsBuffer[xx][yy] == 1:
                        # Check alive neighbours and count them
                        neighbours = neighbours + 1
    return neighbours

def keyPressed():
    global pause
    if key == 'r' or key == 'R':
        # Restart: reinitialization of cells
        for x in range(grid_w):
            for y in range(grid_h):
                state = random(100)
                if state > probabilityOfAliveAtStart:
                    state = 0
                else:
                    state = 1
                cells[x][y] = state  # Save state of each cell
    if key == ' ':  # On/off of pause
        pause = not pause
    if (key == 'c' or key == 'C'):  # Clear all
        for x in range(grid_w):
            for y in range(grid_h):
                cells[x][y] = 0  # Save all to zero
    global GIF_EXPORT
    if key == 'p':  # save PNG
        saveFrame("####.png")
    if key == 'g':  # save GIF
        GIF_EXPORT = True

def pointy_hexagon(x, y, r):
    with pushMatrix():
        translate(x, y)
        rotate(radians(30))  # pointy, comment out for "flat_hexagon()"
        beginShape()
        for i in range(6):
            sx = cos(i * TWO_PI / 6) * r
            sy = sin(i * TWO_PI / 6) * r
            vertex(sx, sy)
        endShape(CLOSE)
