from flask import Flask, render_template
import config

app = Flask(__name__)


@app.route("/")
def home():
    is_on = GPIO.input(LED)         # 핀이 지금 켜져 있으면 1, 꺼져 있으면 0
    return render_template("index.html", is_on=is_on)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT)
