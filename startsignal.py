from microbit import *
import time
import utime
import random
import music

LIGHT_INTERVAL = 1000
GO_WAIT = random.randint(2000, 3000)

class FalseStartError(Exception):
    """A exception for a false start"""
    pass

def wait_for(duration_ms):
    wait_time = time.ticks_ms() + duration_ms
    while wait_time > time.ticks_ms():
        if button_a.is_pressed():
            raise FalseStartError()

def start_sequence():
    # Light up first column
    display.set_pixel(0, 3, 9)
    display.set_pixel(0, 4, 9)
    music.pitch(150, 150)

    # Light up the subsequent column
    for seq in range(1, 5):
        wait_for(LIGHT_INTERVAL)
        display.set_pixel(seq, 3, 9)
        display.set_pixel(seq, 4, 9)
        music.pitch(150, 150)

    # Lights out
    wait_for(GO_WAIT)
    display.clear()

while True:
    try:
        start_sequence()
    except FalseStartError as e:
        # display.scroll("False Start")
        display.show(Image.NO)
        break

    start_time = time.ticks_ms()
    while not button_a.is_pressed():
        sleep(1)
    reaction_time = utime.ticks_diff(time.ticks_ms(), start_time)
    display.scroll("{:.3f}".format(reaction_time / 1000))
    break
