from flask import render_template, request, redirect, url_for
from models.data import Data, db
from app import app


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users-list')
def users_list():
    users = Data.query.order_by(Data.name).all()

    return render_template('users_list.html', users=users)

@app.route('/users-list/<int:id>')
def users_info(id):
    user = Data.query.get(id)

    return render_template('user_info.html', user=user)

@app.route('/users-list/<int:id>/delete')
def users_delete(id):
    user = Data.query.get_or_404(id)

    try:
        db.session.delete(user)
        db.session.commit()
        return redirect('/users-list')
    except:
        return 'Fault user delete'

@app.route('/users-list/<int:id>/update', methods=['POST', 'GET'])
def user_update(id):
    user = Data.query.get_or_404(id)

    if request.method == 'POST':
        user.name = request.form['user-name']
        user.phone = request.form['phone-number']
        try:
            db.session.commit()
            return redirect('/users-list')
        except:
            return 'Fault update user'
    else:
        return render_template('edit_user.html', user=user)


@app.route('/create-user', methods=['POST', 'GET'])
def user_create():
    if request.method == 'POST':
        name = request.form['user-name']
        phone = request.form['phone-number']
        
        try:
            data = Data(name=name, phone=phone)
            db.session.add(data)
            db.session.commit()
            return redirect('/users-list')
        except:
            return '<h2>DB create error</h2>'

    else:
        return render_template('create_user.html')

@app.route('/create')
def create():
    db.create_all()
    return render_template('create_db.html')