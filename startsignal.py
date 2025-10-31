from microbit import *
import time
import utime
import random

def wait_for(wait_ms):
    wait_time = time.ticks_ms() + wait_ms
    while wait_time > time.ticks_ms():
        if button_a.is_pressed():
            return False
    return True

def start_sequence():
    # Light up first column
    display.set_pixel(0, 3, 9)
    display.set_pixel(0, 4, 9)

    # Light up the subsequent column
    for seq in range(1, 5):
        if not wait_for(1000):
            return False
        display.set_pixel(seq, 3, 9)
        display.set_pixel(seq, 4, 9)

    # Turn off all columns
    if not wait_for(random.randint(1000, 3000)):
        return False
    display.clear()

while True:
    if start_sequence() == False:
        # display.scroll("False Start")
        display.show(Image.NO)
        break

    start_time = time.ticks_ms()
    while not button_a.is_pressed():
        sleep(1)
    reaction_time = utime.ticks_diff(time.ticks_ms(), start_time)
    display.scroll(reaction_time / 1000)
    # display.scroll("RT: ()ms".format(reaction_time / 1000))
#    display.show()
