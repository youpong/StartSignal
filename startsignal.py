import microbit as mb
import time
import random
import music

LED_BRIGHTNESS: int = 5
LIGHT_INTERVAL: int = 1000


def go_wait() -> int:
    """
    Generate random wait time before light out.
    
    Returns:
        Random wait time between 2000-3000ms
    """
    return random.randint(2000, 3000)


def wait_for(duration: int) -> bool:
    """
    Wait for duration(ms) time.

    Args:
        duration: Wait time(ms)

    Returns:
        False if jump start detected, True otherwise
    """
    wait_time = time.ticks_ms() + duration  # type: ignore[attr-defined]
    while wait_time > time.ticks_ms():  # type: ignore[attr-defined]
        if mb.button_a.is_pressed():
            return False
        time.sleep_ms(1)  # type: ignore[attr-defined]
    return True


def light_up(column: int) -> None:
    """
    Light up LEDs in specified column.

    Args:
        column: Column index (0-4)
    """
    mb.display.set_pixel(column, 3, LED_BRIGHTNESS)
    mb.display.set_pixel(column, 4, LED_BRIGHTNESS)
    music.pitch(150, 150, wait=False)


def start_sequence() -> bool:
    """
    Execute the start light sequence.

    Returns:
        False if jump start detected, True otherwise
    """
    mb.display.clear()

    # Light up the subsequent column
    for seq in range(5):
        if seq != 0 and not wait_for(LIGHT_INTERVAL):
            return False
        light_up(seq)

    # Lights out
    if not wait_for(go_wait()):
        return False
    mb.display.clear()
    return True


def run_game():
    # type: () -> int | None
    """
    Run one game cycle.

    Returns:
        Reaction time in ms, or None if jump start
    """
    if not start_sequence():
        mb.display.show(mb.Image.NO)
        return None

    start_time = time.ticks_ms()  # type: ignore[attr-defined]
    while not mb.button_a.is_pressed():
        time.sleep_ms(1)  # type: ignore[attr-defined]
    return time.ticks_diff(time.ticks_ms(), start_time)  # type: ignore[attr-defined]


# Main routine
while True:
    while not mb.pin_logo.is_touched():
        time.sleep_ms(1)  # type: ignore[attr-defined]

    reaction_time = run_game()
    if reaction_time is not None:
        mb.display.scroll("{:.3f}".format(reaction_time / 1000.0))
