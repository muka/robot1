from machine import Pin, reset, PWM

class DCMotor:
    def __init__(self, pwm_pin, direction_pin1, direction_pin2):
        """
        pwm_pin: PWM capable pin id. This pin should be connected to ENA/B.
        direction_pin1 and direction_pin1: Direction pins to be connected to
                                           N1/2 or N3/4.
        """
        self.dir_pin1 = Pin(direction_pin1, mode=Pin.OUT)
        self.dir_pin2 = Pin(direction_pin2, mode=Pin.OUT)
        self.pwm_pin = Pin(pwm_pin, mode=Pin.OUT)
        self.pwm = PWM(self.pwm_pin, freq=100, duty=0)

    def forward(self):
        self.dir_pin1.on()
        self.dir_pin2.off()

    def backward(self):
        self.dir_pin1.off()
        self.dir_pin2.on()

    def stop(self):
        self.dir_pin1.off()
        self.dir_pin2.off()

    def set_speed(self, ratio):
        """
        sets speed by pwm duty cycle value.
        ratio: The speed ratio ranging from 0 to 1.
               Anything above 1 will be taken as 1 and negative
               as 0.
        """
        if ratio < 0:
            self.pwm.duty(0)
        elif ratio <= 1.0:
            self.pwm.duty(int(1024*ratio))
        else:
            self.pwm.duty(1024)
