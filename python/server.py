import argparse

from servo import Servo
from feeder import Feeder
from flask import Flask, jsonify

app = Flask(__name__)
feeder = Feeder()

def setup(opt):
    servo = Servo(opt.gpio)
    servo.setup()
    feeder.set_servo(servo)
    feeder.set_portions_limit(opt.portions_limit)

@app.route('/feed')
def feed():
    status = feeder.feed()
    #  msg = get_message_for_status(status)
    msg = "Feed"
    return jsonify(
            status=status, 
            message=msg, 
            portions_limit=feeder.get_portions_limit(), 
            portions_left=feeder.get_portions_left()
            )

@app.route('/fillUp')
def fill_up():
    status = feeder.fill_up()
    #  msg = get_message_for_status(status)
    msg = "Feed"
    return jsonify(
            status=status, 
            message=msg, 
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
    opt = parser.parse_args()

    setup(opt)

    app.run(host='0.0.0.0', port=opt.port)
