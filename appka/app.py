from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hlavna_stranka():
    return render_template("index.html", pocitac = "51")

@app.route("/tajna-sprava")
def sprava():
    return "abc"

app.run(host="0.0.0.0")