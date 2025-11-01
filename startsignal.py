from microbit import *  # noqa: F401, F403
import time
import random
import music

LED_BRIGHTNESS = 5
LIGHT_INTERVAL = 1000


class FalseStartError(Exception):
    """A exception for a false start"""
    pass


def go_wait():
    return random.randint(2000, 3000)


def wait_until(target):
    while target > time.ticks_ms():
        if button_a.is_pressed():
            raise FalseStartError()
        time.sleep_ms(1)


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
    wait_until(time.ticks_ms() + go_wait())
    display.clear()


while True:
    while not pin_logo.is_touched():
        pass

    try:
        start_sequence()
    except FalseStartError:
        display.show(Image.NO)
        continue

    start_time = time.ticks_ms()
    while not button_a.is_pressed():
        time.sleep_ms(1)
    reaction_time = time.ticks_diff(time.ticks_ms(), start_time)
    display.scroll("{:.3f}".format(reaction_time / 1000))
