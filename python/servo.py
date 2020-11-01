import RPi.GPIO as GPIO
import time

from status import Status


class Servo():
    def __init__(self, gpio_pin):
        self.gpio_pin = gpio_pin
        self.running = False
        self.last_status = Status('servo')

    def get_status(self):
        return self.last_status

    def setup(self):
        if not self.running:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(self.gpio_pin, GPIO.OUT)
            self.servo = GPIO.PWM(self.gpio_pin, 50)
            self.servo.start(0)
            self.running = True
            self.last_status.set_status(Status.SERVO_SETUP_SUCCESS)
        else:
            self.last_status.set_status(Status.SERVO_SETUP_ALREADY_RUNNING)
        return self.last_status

    def set_angle(self, angle_deg):
        try:
            self.servo.ChangeDutyCycle(2 + (angle_deg/18))
            time.sleep(0.5)
            self.servo.ChangeDutyCycle(0)
            self.last_status.set_status(Status.SERVO_ROTATE_SUCCESS)
        except ValueError as err:
            print(f'Servo::set_angle-> {err}')
            self.last_status.set_status(Status.SERVO_ROTATE_ERROR)
        finally:
            return self.last_status

    def tear_down(self):
        if self.running:
            self.servo.stop()
            GPIO.cleanup()
            self.running = False
            self.last_status.set_status(Status.SERVO_TEAR_DOWN_SUCCESS)
        else:
            self.last_status.set_status(Status.SERVO_TEAR_DOWN_NOT_RUNNING)
        return self.last_status
