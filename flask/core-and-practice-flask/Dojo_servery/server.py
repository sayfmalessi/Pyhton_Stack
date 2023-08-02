from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "mysecretkey"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    session["gender"] = request.form["gender"]
    session["hobbies"] = request.form.getlist("hobbies")
    return redirect("/result")

@app.route("/result")
def result():
    if session["hobbies"] == []:
        session["hobbies"] = 'no hobbies are selected'

    return render_template("result.html")









if __name__ == "__main__":
    app.run(debug=True)