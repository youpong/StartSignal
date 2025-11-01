import microbit


def pitch(frequency: int,
          duration: int = -1,
          pin: microbit.MicroBitAnalogDigitalPin = microbit.pin0,
          wait: bool = True) -> None: ...
