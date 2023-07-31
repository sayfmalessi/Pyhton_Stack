from flask import Flask ,render_template
app = Flask(__name__)


@app.route('/')         
def hello_world():
    return  render_template('index.html')

@app.route('/dojo')         
def hello_dojo():
    return 'dojo!'

@app.route('/say/<name>') 
def hello(name):
    print(name)
    return "hi, " + name

@app.route("/repeat/<x>/<word>")
def repeat_word(x,word):
    return (word+"<br>")*int(x)


if __name__=="__main__":    
    app.run(debug=True)