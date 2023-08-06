from flask_app import app
from flask import request ,render_template, session, redirect, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


@app.route('/recipes/new')
def new_recipe():
    if not 'user_id' in session:
        return redirect('/')
    return render_template('new_recip.html')
@app.route('/recipes/create', methods=['POST'])
def create_recip():
    if (Recipe.validate(request.form)):
        
        data ={
            **request.form,
            'user_id':session['user_id']
        }
        print(data)
        Recipe.create_recip(data)
        return redirect('/dashboard')
    return redirect('/recipes/new')

@app.route('/recipes/<int:user_id>')
def show(user_id):
    recipe = Recipe.get_by_id({'id':user_id})
    user = User.get_by_id({'id':session['user_id']})
    print(recipe)
    return render_template('show.html',recipe=recipe,user=user)

@app.route('/recipes/<int:recip_id>/edit')
def edit(recip_id):
    if not 'user_id' in session:
        return redirect('/')
    
    recip=Recipe.get_by_id({'id':recip_id})
    return render_template('edit.html',recip=recip)

@app.route('/recipes/<int:recip_id>/update', methods=['POST'])
def update(recip_id):
    if(Recipe.validate(request.form)):
        Recipe.edit_recip(request.form)
        return redirect('/dashboard')
    return redirect('/recipes/'+str(recip_id)+'/edit')
@app.route('/recipes/<int:recip_id>/destroy')
def destroy(recip_id):
    
    Recipe.remove({'id':recip_id})
    return redirect('/dashboard')
