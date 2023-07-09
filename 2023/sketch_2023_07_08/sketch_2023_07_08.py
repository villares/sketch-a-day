# based on https://www.jpytr.com/post/game_of_life/

import py5
import numpy as np
from scipy.signal import convolve2d

board_img = count_img = None

color_map = np.array([
    [0, 0, 0],
    [250, 250, 0],      
    [0, 0, 250],    
    ])

def setup():
    global status
    py5.size(1200, 600)
    py5.no_smooth()
    status = get_init_status((py5.height // 4, py5.width // 4))
    py5.frame_rate(20)

def draw():
    global status, board_img, count_img
    py5.scale(4)
    status = apply_conways_game_of_life_rules(status)
    colored_status = status.copy()
    colored_status[1::2,::2] *= 2
    colored_status[::2,1::2] *= 2
    board_img = py5.create_image_from_numpy(color_map[colored_status], 'RGB', dst=board_img)
    py5.image(board_img, 0, 0)
    # count_img = py5.create_image_from_numpy(live_neighbors * 32, 'L', dst=count_img)
    # py5.image(count_img, 0, 0) 

def get_init_status(size, initial_prob_life=0.5):
    status = np.random.uniform(0, 1, size=size) <= initial_prob_life
    return status

def apply_conways_game_of_life_rules(status):
    global live_neighbors
    """Applies Conway's Game of Life rules given the current status of the game"""
    live_neighbors = count_live_neighbors(status)
    survive_underpopulation = live_neighbors >= 2
    survive_overpopulation = live_neighbors <= 3
    survive = status * survive_underpopulation * survive_overpopulation
    new_status = np.where(live_neighbors==3, 1, survive)  # Born
    return new_status 

def count_live_neighbors(status):
    """Counts the number of neighboring live cells"""
    kernel = np.array(
        [
         [0, 0, 1, 0, 0],
         [0, 1, 0, 1, 0],
         [1, 0, 0, 0, 1],
         [0, 1, 0, 1, 0],
         [0, 0, 1, 0, 0],
         ])
    return convolve2d(status, kernel, mode='same', boundary="wrap")

py5.run_sketch()
