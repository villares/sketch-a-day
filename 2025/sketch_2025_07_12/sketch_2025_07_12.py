# Basedn on the QueasyCam "maze" example

# import py5_tools
# print(py5_tools.processing.download_library("QueasyCam"))  # run once to install

import py5
from queasycam import QueasyCam   # needs to be after py5 import

def setup():
    global player, maze
    py5.size(600, 600, py5.P3D)
    py5.stroke_weight(2)
    py5.color_mode(py5.HSB)
    
    this = py5.get_current_sketch()
    player = Player(this)
    maze = Maze(20)
    maze.set_player_at_start(player)

def draw():
    py5.background(51)
    maze.update()
    maze.display()
    player.update()

class Maze:
    def __init__(self, order):
        self.blocks = [[None for _ in range(order)] for _ in range(order)]
        
        for i in range(order):
            for j in range(order):
                x = i * 5
                y = 0
                z = j * 5
                self.blocks[i][j] = Block(x, y, z, 5, 5, 5)
        
        row = int(py5.random(1, order-1))
        col = int(py5.random(1, order-1))
        self.start = self.blocks[row][col]
        
        for _ in range(order * order * order // 10):
            if not self.blocks[row][col].visited:
                self.blocks[row][col].move_down()
            self.blocks[row][col].visited = True
            
            if py5.random(1) < 0.5:
                if py5.random(1) < 0.5 and row > 1:
                    row -= 1
                elif row < order-2:
                    row += 1
            else:
                if py5.random(1) < 0.5 and col > 1:
                    col -= 1
                elif col < order-2:
                    col += 1
    
    def update(self):
        for row in self.blocks:
            for block in row:
                block.update()
    
    def display(self):
        for row in self.blocks:
            for block in row:
                block.display()
    
    def set_player_at_start(self, player):
        player.cam.position = py5.Py5Vector3D(
            self.start.position.x, 
            self.start.position.y -15, 
            self.start.position.z,
        )
        
class Block:
    def __init__(self, x, y, z, w, h, d):
        self.position = py5.Py5Vector3D(x, y, z)  
        self.dimensions = py5.Py5Vector3D(w, h, d)  

        self.fill_color = py5.color(py5.random(255), 200, 200) # grays only on the original example
        self.visited = False
    
    def update(self):
        player_left = player.cam.position.x - player.dimensions.x/2
        player_right = player.cam.position.x + player.dimensions.x/2
        player_top = player.cam.position.y - player.dimensions.y/2
        player_bottom = player.cam.position.y + player.dimensions.y/2
        player_front = player.cam.position.z - player.dimensions.z/2
        player_back = player.cam.position.z + player.dimensions.z/2
        
        box_left = self.position.x - self.dimensions.x/2
        box_right = self.position.x + self.dimensions.x/2
        box_top = self.position.y - self.dimensions.y/2
        box_bottom = self.position.y + self.dimensions.y/2
        box_front = self.position.z - self.dimensions.z/2
        box_back = self.position.z + self.dimensions.z/2
        
        box_left_overlap = player_right - box_left
        box_right_overlap = box_right - player_left
        box_top_overlap = player_bottom - box_top
        box_bottom_overlap = box_bottom - player_top
        box_front_overlap = player_back - box_front
        box_back_overlap = box_back - player_front
        
        if (((box_left < player_left < box_right) or (box_left < player_right < box_right)) and 
            ((box_top < player_top < box_bottom) or (box_top < player_bottom < box_bottom)) and 
            ((box_front < player_front < box_back) or (box_front < player_back < box_back))):
            
            x_overlap = max(min(box_left_overlap, box_right_overlap), 0)
            y_overlap = max(min(box_top_overlap, box_bottom_overlap), 0)
            z_overlap = max(min(box_front_overlap, box_back_overlap), 0)
            
            if x_overlap < y_overlap and x_overlap < z_overlap:
                if box_left_overlap < box_right_overlap:
                    player.cam.position.x = box_left - player.dimensions.x/2
                else:
                    player.cam.position.x = box_right + player.dimensions.x/2
            
            elif y_overlap < x_overlap and y_overlap < z_overlap:
                if box_top_overlap < box_bottom_overlap:
                    player.cam.position.y = box_top - player.dimensions.y/2
                    player.velocity.y = 0
                    player.grounded = True
                else:
                    player.cam.position.y = box_bottom + player.dimensions.y/2
            
            elif z_overlap < x_overlap and z_overlap < y_overlap:
                if box_front_overlap < box_back_overlap:
                    player.cam.position.z = box_front - player.dimensions.x/2
                else:
                    player.cam.position.z = box_back + player.dimensions.x/2
    
    def display(self):
        py5.push_matrix()
        py5.translate(self.position.x, self.position.y, self.position.z)
        py5.fill(self.fill_color)   # translucent on the original example py5.fill(self.fill_color, 2000)  
        py5.box(self.dimensions.x, self.dimensions.y, self.dimensions.z)
        py5.pop_matrix()
    
    def move_down(self):
        self.position.y += 5


class Player():
    def __init__(self, this):
        self.cam = QueasyCam(this)
        self.cam.speed = 0.04
        self.dimensions = py5.Py5Vector3D(1, 3, 1)
        self.velocity = py5.Py5Vector3D(0, 0, 0)
        self.gravity = py5.Py5Vector3D(0, 0.01, 0)
        self.grounded = False
        #print(dir(self.cam))
    
    def update(self):
        self.velocity = self.velocity + self.gravity
        self.cam.position.y = self.cam.position.y + self.velocity.y        
        if self.grounded and py5.is_key_pressed and py5.key == ' ':
            self.grounded = False
            self.velocity.y = -0.5
            self.cam.position.y -= 0.1
       

py5.run_sketch(block=False)
