from flask import Flask
app = Flask(__name__)
app.secret_key = 'selem'
DB = 'ninjas_dojos'