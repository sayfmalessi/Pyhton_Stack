from flask import Flask, render_template

app = Flask(__name__)

users = [
    {'first_name': 'Michael', 'last_name': 'Choi'},
    {'first_name': 'John', 'last_name': 'Supsupin'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

# Add the 'full_name' field to the users data
for user in users:
    user['full_name'] = user['first_name'] + ' ' + user['last_name']

@app.route('/')
def index():
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
