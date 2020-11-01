from status import Status


class Feeder():
    def __init__(self, portions_limit=0, servo=None):
        self.portions_limit = portions_limit
        self.portions_left = portions_limit
        self.servo = servo
        if self.servo != None:
            self.servo.setup()
        self.last_status = Status('feeder')
        self.last_servo_status = Status('servo')

    def feed(self):
        if self.portions_left == 0:
            print('No portions left :( please fill up the feeder')
            self.last_status.set_status(Status.NO_PORTIONS)
            self.last_servo_status.set_status(Status.NOT_TRIGGERED)
            return [self.last_status, self.last_servo_status]

        self.portions_left -= 1
        print(
            f'Feeding... portions left: {self.portions_left}/{self.portions_limit}')

        servo_status = self.servo.set_angle(
            (180 / self.portions_limit) *
            (self.portions_limit - self.portions_left)
        )

        if servo_status.get_status() == Status.SERVO_ROTATE_SUCCESS:
            self.last_status.set_status(Status.FEED_SUCCESS)
        else:
            self.last_status.set_status(Status.FEED_ERROR)

        return [self.last_status, servo_status]

    def refill(self):
        if self.portions_left == self.portions_limit:
            print('Feeder already full! No need to refill')
            self.last_status.set_status(Status.FEEDER_FULL)
            self.last_servo_status.set_status(Status.NOT_TRIGGERED)
            return [self.last_status, self.last_servo_status]

        self.portions_left = self.portions_limit
        print(
            f'Refilling... portions left: {self.portions_left}/{self.portions_limit}')
        servo_status = self.servo.set_angle(0)

        if servo_status.get_status() == Status.SERVO_ROTATE_SUCCESS:
            self.last_status.set_status(Status.FEED_SUCCESS)
        else:
            self.last_status.set_status(Status.FEED_ERROR)

        return [self.last_status, servo_status]

    def set_portions_limit(self, portions_limit):
        self.portions_limit = portions_limit
        self.portions_left = portions_limit

    def set_servo(self, servo):
        if self.servo != None:
            self.servo.tear_down()
        self.servo = servo

    def get_portions_limit(self):
        return self.portions_limit

    def get_portions_left(self):
        return self.portions_left

    def get_state(self):
        return [self.last_status, self.last_servo_status]
