from aluLib import *

# Screen width and height
window_width = 1500
window_height = 400

def cards():
    global loaded, inserted
    # Load cards from assets/ directory.
    if loaded == False:
        inserted = raw_input("Please select cards from A,2,3,4,5,6,7,8,9,10,J,K or Q: ")
        inserted = inserted.split(',')

        x = 20
        draw_text("You have selected the cards below, Press s to sort and r to randomize selection", window_width/3, 40)
        for i in inserted:
            draw_image("assets/"+ i+'.png', x, 150)
            x+=110
        loaded = True

def sort():
    global sorted, status, final
    if is_key_pressed('s'):
        sorted = []
        deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q']
        for x in deck:
            for i in inserted:
                if str(x) == i:
                    sorted.append(i)
                else:
                    pass
        status = True
        final = sorted


def draw():
    global status, loaded_sort
    if status == True:
        clear()
        draw_text("Your sorted card deck is below", window_width / 4,
                  40)
        x = 20
        for i in sorted:
            draw_image("assets/" + i + '.png', x, 150)
            x += 110
        loaded_sort = True


def main():
    cards()
    sort()
    draw()

loaded = False
loaded_sort = False
inserted = []
final = []
status = None
start_graphics(main, width=window_width, height=window_height)