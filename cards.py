from aluLib import *

# Screen width and height
window_width = 1500
window_height = 900


def cards():
    card_list = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'king', 'queen']
    for i in card_list:
        draw_image("assets/"+ str(i) + '.png', 100, 150)

def main():
    cards()

start_graphics(main, width=window_width, height=window_height, framerate=60)