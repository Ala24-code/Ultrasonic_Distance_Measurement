from machine import Pin, time_pulse_us
from time import sleep_us

class HCSR04:
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=30000):
        self.trigger = Pin(trigger_pin, mode=Pin.OUT)
        self.echo = Pin(echo_pin, mode=Pin.IN)
        self.echo_timeout_us = echo_timeout_us

    def _send_pulse_and_wait(self):
        self.trigger.off()
        sleep_us(5)
        self.trigger.on()
        sleep_us(10)
        self.trigger.off()
        try:
            pulse_time = time_pulse_us(self.echo, 1, self.echo_timeout_us)
            return pulse_time
        except OSError as ex:
            raise OSError('Out of range')

    def distance_mm(self):
        pulse_time = self._send_pulse_and_wait()
        mm = (pulse_time * 100) // 582
        return mm

    def distance_cm(self):
        pulse_time = self._send_pulse_and_wait()
        cm = (pulse_time / 2) / 29.1
        return cm

