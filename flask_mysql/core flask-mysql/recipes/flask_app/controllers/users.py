from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)     





@app.route('/')
def index():
    return render_template('index.html')
@app.route('/users/create', methods=['POST'])
def create():
    if (User.validate(request.form)):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        data = {
                **request.form,'password': pw_hash
        }
        user_id = User.create(data)
        session['user_id']= user_id
    
        return redirect('/dashboard')
    return redirect('/')
@app.route('/dashboard')
def dashboard():
    if not 'user_id' in session:
        return redirect('/')
    user = User.get_by_id({'id':session['user_id']})
    recipes = Recipe.get_all()
    return render_template('dashboard.html',user=user,recipes=recipes)
@app.route('/users/login', methods=['POST'])
def login():
    user_in_db = User.get_by_email({'email':request.form['email']})
    print(user_in_db)
    if(user_in_db):
        # check password
        if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
            flash("Invalid Email/Password")
            return redirect('/')
        session['user_id']=user_in_db.id
        return redirect('/dashboard')
    flash("Invalid Email/Password")
    return redirect('/')
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')