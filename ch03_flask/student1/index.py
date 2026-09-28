from flask import Flask, render_template
import config

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<num>")
def save_num_get(num):
    print("넘어온 숫자:", num)

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=True)
