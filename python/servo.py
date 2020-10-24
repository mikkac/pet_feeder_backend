import RPi.GPIO as GPIO
import time

class Servo():
    def __init__(self, gpio_pin):
        self.gpio_pin = gpio_pin
        self.running = False

    def setup(self):
        if not self.running:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(self.gpio_pin, GPIO.OUT)
            self.servo = GPIO.PWM(self.gpio_pin, 50)
            self.servo.start(0)
            self.running = True

    def set_angle(self, angle_deg):
        try:
            self.servo.ChangeDutyCycle(2 + (angle_deg/18))
            time.sleep(0.5)
            self.servo.ChangeDutyCycle(0)
            return 0
        except ValueError as err:
            print(f'Servo::set_angle-> {err}')
            return -1

    def tear_down(self):
        if self.running:
            self.servo.stop()
            GPIO.cleanup()
            self.running = False
