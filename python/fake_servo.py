import time

class FakeServo():
    def __init__(self, gpio_pin):
        self.gpio_pin = gpio_pin
        self.running = False

    def setup(self):
        if not self.running:
            print('Setting up FakeServo')
            self.running = True

    def set_angle(self, angle_deg):
        print(f'Rotating FakeServo by {angle_deg} degrees')

    def tear_down(self):
        if self.running:
            print('Tearing down FakeServo')
            self.running = False
