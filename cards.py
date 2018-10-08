from aluLib import *
import os

# Screen width and height
window_width = 1500
window_height = 900


def cards():
    # Load cards from assets/ directory.
    card_list = os.listdir('assets/')
    x = 20
    for i in card_list:
        draw_image("assets/"+ i, x, 150)
        x+=110

def sort(cards):
    if is_key_pressed('s'):
        pass

def main():
    cards()

start_graphics(main, width=window_width, height=window_height, framerate=60)