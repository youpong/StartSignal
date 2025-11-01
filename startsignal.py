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

def wait_until(target):
    while target > time.ticks_ms():
        if button_a.is_pressed():
            raise FalseStartError()
        utime.sleep_ms(1)

def light_up(column):
    display.set_pixel(column, 3, LED_BRIGHTNESS)
    display.set_pixel(column, 4, LED_BRIGHTNESS)
    
def start_sequence():
    display.clear()
    
    # Light up first column
    start_time = time.ticks_ms()
    light_up(0)
    music.pitch(150, 150)

    # Light up the subsequent column
    for seq in range(1, 5):
        wait_until(start_time + LIGHT_INTERVAL)
        start_time = time.ticks_ms()
        light_up(seq)
        music.pitch(150, 150)

    # Lights out
    wait_until(time.ticks_ms() + GO_WAIT())
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
        utime.sleep_ms(1)
    reaction_time = utime.ticks_diff(time.ticks_ms(), start_time)
    display.scroll("{:.3f}".format(reaction_time / 1000))
