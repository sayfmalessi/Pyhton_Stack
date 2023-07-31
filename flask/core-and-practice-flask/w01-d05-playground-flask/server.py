from flask import Flask, render_template

app = Flask(__name__)

@app.route('/box/')
def box():
    return render_template("index.html", number=3, color="coral")

@app.route('/box/<url_color>/<int:number>')
def colored_box(url_color, number):
    return render_template("index.html", color = url_color, number = number)


if __name__ == '__main__':
    app.run(debug=True, port=5000)