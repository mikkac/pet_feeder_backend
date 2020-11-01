class Status():
    # Statuses related to general state of Feeder
    ALIVE = 0
    DEAD = -1

    # Statuses related to 'feed' operation
    FEED_SUCCESS = 10
    FEED_ERROR = -10
    NO_PORTIONS = -11

    # Statuses related to 'refill' operation
    REFILL_SUCCESS = 20
    REFILL_ERROR = -20
    FEEDER_FULL = -21

    # Statuses related to servomechanism
    SERVO_SETUP_SUCCESS = 30
    SERVO_SETUP_ERROR = -30
    SERVO_SETUP_ALREADY_RUNNING = -31
    SERVO_ROTATE_SUCCESS = 40
    SERVO_ROTATE_ERROR = -40
    SERVO_TEAR_DOWN_SUCCESS = 50
    SERVO_TEAR_DOWN_ERROR = -50
    SERVO_TEAR_DOWN_NOT_RUNNING = -51
    INVALID_GPIO_PIN = -60

    # Misc statuses
    NOT_INITIALIZED = -200
    NOT_TRIGGERED = -300

    messages = {
        ALIVE: 'Feeder alive',
        DEAD: 'Feeder dead',

        FEED_SUCCESS: 'Feed has ended with success',
        FEED_ERROR: 'Feed has ended with failure',
        NO_PORTIONS: 'No more portions available, please refill',

        REFILL_SUCCESS: 'Refill has ended with success',
        REFILL_ERROR: 'Refill has ended with failure',
        FEEDER_FULL: 'Feeder is full! No need to refill',

        SERVO_SETUP_SUCCESS: 'Servo setup properly',
        SERVO_SETUP_ERROR: 'Servo setup has ended with failure',
        SERVO_SETUP_ALREADY_RUNNING: 'Servo is already active',
        SERVO_ROTATE_SUCCESS: 'Servo rotated successfully',
        SERVO_ROTATE_ERROR: 'Error during servo rotation',
        SERVO_TEAR_DOWN_SUCCESS: 'Servo teared down properly',
        SERVO_TEAR_DOWN_ERROR: 'Servo tear down has ended with failure',
        SERVO_TEAR_DOWN_NOT_RUNNING: 'Servo is not running yet',
        INVALID_GPIO_PIN: 'Invalid GPIO pin',

        NOT_INITIALIZED: 'Not initialized',
        NOT_TRIGGERED: 'No need to trigger',
    }

    @staticmethod
    def get_desc(status):
        msg = 'Unknown status'

        try:
            msg = Status.messages[status]
        except KeyError:
            print('Unknown status :(')

        return msg

    def __init__(self, who='unknown'):
        self.who = who
        self.status = Status.NOT_INITIALIZED

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_who(self):
        return self.who

    def as_dict(self):
        return {
            'status': self.status,
            'message': Status.get_desc(self.status),
        }
