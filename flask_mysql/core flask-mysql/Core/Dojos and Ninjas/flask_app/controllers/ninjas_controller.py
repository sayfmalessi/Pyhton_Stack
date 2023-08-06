from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninjas_model import Ninja

# RENDER ROUTE - READ ALL


@app.route("/Ninja")
def display_Ninja():
    all_Ninja = Ninja.get_l()
    # print(all_Ninja)
    return render_template("Ninja.html", all_Ninja=all_Ninja)

# RENDER ROUTE - Display FORM


@app.route("/form")
def display_form():

    return render_template("form.html")


# ACTION ROUTE - Create Hero
@app.route("/processForm", methods=["POST"])
def create_hero():

    Ninja.create(request.form)
    return redirect("/Ninja")

# RENDER ROUTE - READ ONE
# ? tablename/id/action


@app.route("/Ninja/<id>/show")
def show_hero(id):

    data = {
        "id": id
    }

    one_hero = Ninja.show_one(data)
    print(one_hero)

    return render_template("show.html", hero=one_hero)

# RENDER ROUTE - EDIT


@app.route("/Ninja/<id>/edit")
def show_update_form(id):
    this_hero = Ninja.show_one({'id': id})
    return render_template("edit_hero.html", hero=this_hero)


# ACTION ROUTE - UPDATE HERO
@app.route("/editHero/<id>/update", methods=["POST"])
def edit_hero(id):

    data = {
        "name": request.form["hero_name"],
        "health_level": request.form["health"],
        "power": request.form["power"],
        'id': id
    }
    Ninja.update_hero(data)

    return redirect("/Ninja")

@app.route('/deleteHero/<id>', methods=["POST"])
def delete_hero(id):
    data = {
            "id": id
    }
    Ninja.delete_hero(data)
    return redirect("/Ninja")
