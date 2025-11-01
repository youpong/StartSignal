from microbit import *  # noqa: F401, F403
import time
import random
import music

LED_BRIGHTNESS = 5
LIGHT_INTERVAL = 1000


class FalseStartError(Exception):
    """A exception for a false start"""
    pass


def go_wait() -> None:
    return random.randint(2000, 3000)


def wait_for(duration) -> None:
    wait_time = time.ticks_ms() + duration
    while wait_time > time.ticks_ms():
        if button_a.is_pressed():
            raise FalseStartError()
        time.sleep_ms(1)


def light_up(column) -> None:
    display.set_pixel(column, 3, LED_BRIGHTNESS)
    display.set_pixel(column, 4, LED_BRIGHTNESS)
    music.pitch(150, 150, wait=False)


def start_sequence() -> None:
    display.clear()

    # Light up first column
    light_up(0)

    # Light up the subsequent column
    for seq in range(1, 5):
        wait_for(LIGHT_INTERVAL)
        light_up(seq)

    # Lights out
    wait_for(go_wait())
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
