class Feeder():
    def __init__(self, portions_limit = 0, servo = None):
        self.__portions_limit = portions_limit
        self.__portions_left = portions_limit
        self.__servo = servo
        if self.__servo != None:
            self.__servo.setup()

    def feed(self):
        if self.__portions_left == 0:
            print('No portions left :( please fill up the feeder')
            return -1
        
        self.__portions_left -= 1
        print(f'Feeding... portions left: {self.__portions_left}/{self.__portions_limit}')
        return self.__servo.set_angle(
            (180 / self.__portions_limit) /
            (self.__portions_limit - self.__portions_left)
            )
        #  return 0

    def fill_up(self):
        self.__portions_left = self.__portions_limit
        print(f'Filling up... portions left: {self.__portions_left}/{self.__portions_limit}')
        return self.__servo.set_angle(0)
        #  return 0

    def set_portions_limit(self, portions_limit):
        self.__portions_limit = portions_limit
        self.__portions_left = portions_limit
       
    def set_servo(self, servo):
        if self.__servo != None:
            self.__servo.tear_down()
        self.__servo = servo

    def get_portions_limit(self):
        return self.__portions_limit

    def get_portions_left(self):
        return self.__portions_left
