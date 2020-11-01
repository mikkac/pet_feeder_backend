import argparse

from feeder import Feeder
from flask import Flask, jsonify
from status import Status

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
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
    return jsonify({
        'portions_left': feeder.get_portions_left(),
        'portions_limit': feeder.get_portions_limit(),
        f'{status[0].get_who()}': status[0].as_dict(),
        f'{status[1].get_who()}': status[1].as_dict()
    }
    )


@app.route('/refill')
def refill():
    status = feeder.refill()
    return jsonify({
        'portions_left': feeder.get_portions_left(),
        'portions_limit': feeder.get_portions_limit(),
        f'{status[0].get_who()}': status[0].as_dict(),
        f'{status[1].get_who()}': status[1].as_dict()
    }
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
