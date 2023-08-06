from my_app import app
from flask import flask,render_template,redirect,request
from my_app.models.users_model import User

#RENDER ROUTE - READ ALL 
@app.route("/users")
def display_users():
    all_users = User.get_all() 
    # print(all_users)
    return render_template("users.html", all_users = all_users)

# RENDER ROUTE - Display FORM
@app.route("/form")
def display_form():

    return render_template("form.html")


# ACTION ROUTE - Create Hero
@app.route("/processForm", methods=["POST"])
def create_hero():
    #! REQUEST, REDIRECT
    # print(request.form)
    User.create(request.form)
    return redirect("/users")

# RENDER ROUTE - READ ONE
#? tablename/id/action
@app.route("/users/<id>/show")
def show_hero(id):

    data = {
        "id": id
    }

    one_hero = User.show_one(data)
    print(one_hero)

    return render_template("show.html", hero = one_hero)

# RENDER ROUTE - EDIT
@app.route("/users/<id>/edit")
def show_update_form(id):
    this_hero = User.show_one({'id': id})
    return render_template("edit_hero.html", hero = this_hero)



#ACTION ROUTE - UPDATE HERO
@app.route("/editHero/<id>/update", methods=["POST"])
def edit_hero(id):
    # print(request.form)
    data = {
        "name": request.form["hero_name"],
        "health_level": request.form["health"],
        "power": request.form["power"],
        'id': id
    }
    User.update_hero(data)

    return redirect("/users")