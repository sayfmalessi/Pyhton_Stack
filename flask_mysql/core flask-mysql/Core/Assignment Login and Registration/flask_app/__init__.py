from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhh this a secret key !!!"
DB_NAME = "log_reg"
