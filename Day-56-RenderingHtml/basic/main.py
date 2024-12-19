from flask import Flask, render_template

app = Flask(__name__)  # name of current directory


@app.route("/")
def home():
    # return render_template("pss.html")
    # return render_template("indexx.html")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
