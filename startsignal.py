from microbit import *
import time
import utime
import random
import music

LED_BRIGHTNESS = 5
LIGHT_INTERVAL = 1000
GO_WAIT = lambda: random.randint(2000, 3000)

class FalseStartError(Exception):
    """A exception for a false start"""
    pass

def wait_for(duration_ms):
    wait_time = time.ticks_ms() + duration_ms
    while wait_time > time.ticks_ms():
        if button_a.is_pressed():
            raise FalseStartError()

def light_up(column):
    display.set_pixel(column, 3, LED_BRIGHTNESS)
    display.set_pixel(column, 4, LED_BRIGHTNESS)
    
def start_sequence():
    display.clear()
    
    # Light up first column
    light_up(0)
    music.pitch(150, 150)

    # Light up the subsequent column
    for seq in range(1, 5):
        wait_for(LIGHT_INTERVAL)
        light_up(seq)
        music.pitch(150, 150)

    # Lights out
    wait_for(GO_WAIT())
    display.clear()

while True:
    while not pin_logo.is_touched():
        pass

    try:
        start_sequence()
    except FalseStartError as e:
        # display.scroll("False Start")
        display.show(Image.NO)
        continue

    start_time = time.ticks_ms()
    while not button_a.is_pressed():
        sleep(1)
    reaction_time = utime.ticks_diff(time.ticks_ms(), start_time)
    display.scroll("{:.3f}".format(reaction_time / 1000))
