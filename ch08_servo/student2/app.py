from flask import Flask, render_template, request, jsonify     # request, jsonify 추가
import RPi.GPIO as GPIO                                        # 추가
from time import sleep                                         # 추가
import config

app = Flask(__name__)
SERVO = config.SERVO_PIN                                       # 추가

# ───── 서보모터 준비 (servo_test.py 와 같음) ─────
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO, GPIO.OUT)
servo = GPIO.PWM(SERVO, 50)
servo.start(0)


def set_angle(angle):
    duty = 2.5 + 10 * angle / 180
    servo.ChangeDutyCycle(duty)
    sleep(0.5)
    servo.ChangeDutyCycle(0)


@app.route("/")
def home():
    return render_template("index.html")


# ───── 아래 라우트 추가 ─────
@app.route("/api/angle", methods=["POST"])
def api_angle():
    data = request.get_json()               # 브라우저가 보낸 JSON 을 딕셔너리로 받음
    angle = int(float(data["angle"]))       # "90.5" 처럼 소수가 와도 정수로 바꿈
    if (angle < 0 or angle > 180):
            return {"message": "0 ~ 180 사이만 가능"},400# ✏️ 1. angle 이 0 보다 작거나 180 보다 크면 {"message": "0 ~ 180 사이만 가능"} 과 400 을 돌려줌
    else:
        set_angle(angle)
        return {"message": f"{angle}도로 움직임"}# ✏️ 2. 아니면 set_angle(angle) 로 움직이고 {"message": "90도로 움직임"} 을 돌려줌
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT)
