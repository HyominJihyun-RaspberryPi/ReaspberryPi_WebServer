from flask import Flask, render_template
import RPi.GPIO as GPIO
import config
from model.led_db import LedDB

app = Flask(__name__)
led_db = LedDB()
LED = config.LED_PIN

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/on", methods=["POST"])
def led_on():
    try:
        GPIO.output(LED, GPIO.HIGH)
        led_db.add(LED, 1)
        return "ok"
    except:
        return "fail"


@app.route("/off", methods=["POST"])
def led_off():
    try:
        GPIO.output(LED, GPIO.LOW)
        led_db.add(LED, 0)
        return "ok"
    except:
        return "fail"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT)
