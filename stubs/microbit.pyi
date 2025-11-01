class Display:
    def show(self,
             image: Image,
             delay: int = 400,
             wait: bool = True,
             loop: bool = False,
             clear: bool = False) -> None: ...

    def scroll(self,
               text: str,
               delay: int = 150,
               wait: bool = True,
               loop: bool = False,
               monospace: bool = False) -> None: ...


class Button:
    def is_pressed(self) -> bool: ...


class Image:
    NO: Image


class MicroBitAnalogDigitalPin:
    pass


class MicroBitTouchPin:
    def is_touched(self) -> bool: ...


display: Display
button_a: Button
button_b: Button
pin_logo: MicroBitTouchPin
pin0: MicroBitAnalogDigitalPin
