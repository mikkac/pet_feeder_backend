import argparse

from feeder import Feeder
from flask import Flask, jsonify
from status import Status

app = Flask(__name__)
feeder = Feeder()


def setup(opt):
    servo = None
    if opt.fake_servo:
        from fake_servo import FakeServo
        servo = FakeServo(opt.gpio)
    else:
        from servo import Servo
        servo = Servo(opt.gpio)
    servo.setup()
    feeder.set_servo(servo)
    feeder.set_portions_limit(opt.portions_limit)


@app.route('/feed')
def feed():
    status = feeder.feed()
    status_as_dict = [s.as_dict() for s in status]
    return jsonify(
        status=status_as_dict,
        portions_limit=feeder.get_portions_limit(),
        portions_left=feeder.get_portions_left()
    )


@app.route('/refill')
def refill():
    status = feeder.refill()
    status_as_dict = [s.as_dict() for s in status]
    return jsonify(
        status=status_as_dict,
        portions_limit=feeder.get_portions_limit(),
        portions_left=feeder.get_portions_left()
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--portions_limit",
        type=int,
        default=8,
        help="Portions limit in the feeder",
    )
    parser.add_argument(
        "--gpio",
        type=int,
        default=11,
        help="Number of GPIO used by Servomechanism",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=5000,
        help="Serving port"
    )
    parser.add_argument(
        "--fake_servo",
        type=lambda x: (str(x).lower() in ['true', '1', 'yes']),
        default=False,
        help="Whether FakeServo shall be used ('true' if yes)"
    )
    opt = parser.parse_args()

    setup(opt)

    app.run(host='0.0.0.0', port=opt.port)
