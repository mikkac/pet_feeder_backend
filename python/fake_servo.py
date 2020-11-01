import time
from status import Status


class FakeServo():
    def __init__(self, gpio_pin):
        self.gpio_pin = gpio_pin
        self.running = False
        self.last_status = Status('servo')

    def get_status(self):
        return self.last_status

    def setup(self):
        if not self.running:
            print('Setting up FakeServo')
            self.running = True
            self.last_status.set_status(Status.SERVO_SETUP_SUCCESS)
        else:
            self.last_status.set_status(Status.SERVO_SETUP_ALREADY_RUNNING)
        return self.last_status

    def set_angle(self, angle_deg):
        print(f'Rotating FakeServo by {angle_deg} degrees')
        self.last_status.set_status(Status.SERVO_ROTATE_SUCCESS)
        return self.last_status

    def tear_down(self):
        if self.running:
            print('Tearing down FakeServo')
            self.running = False
            self.last_status.set_status(Status.SERVO_TEAR_DOWN_SUCCESS)
        else:
            self.last_status.set_status(Status.SERVO_TEAR_DOWN_NOT_RUNNING)
        return self.last_status
