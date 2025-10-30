from microbit import *
import time
import utime

def show_signal():
    display.show(Image('00000:'
                      '00000:'
                      '00000:'
                      '00000:'
                      '00000:'))
    sleep(1000)
    display.show(Image('00000:'
                      '00000:'
                      '00000:'
                      '90000:'
                      '90000:'))
    sleep(1000)
    display.show(Image('00000:'
                      '00000:'
                      '00000:'
                      '99000:'
                      '99000:'))
    sleep(1000)
    display.show(Image('00000:'
                      '00000:'
                      '00000:'
                      '99900:'
                      '99900:'))
    sleep(1000)
    display.show(Image('00000:'
                      '00000:'
                      '00000:'
                      '99990:'
                      '99990:'))
    sleep(1000)
    display.show(Image('00000:'
                      '00000:'
                      '00000:'
                      '99999:'
                      '99999:'))
    # TODO: randomize sleep time
    sleep(1000)
    display.show(Image('00000:'
                      '00000:'
                      '00000:'
                      '00000:'
                      '00000:'))    

while True:
    display.scroll('Touch Logo to start')
    while True:
        if pin_logo.is_touched():
            break
        
    show_signal()
    start_time = time.ticks_ms()
    while True:
        if button_a.is_pressed():
            reacted_time = time.ticks_ms()
            duration_time = utime.ticks_diff(reacted_time, start_time) / 1000
            display.scroll(duration_time)
            break
