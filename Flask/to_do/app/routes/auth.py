from flask import Blueprint , Flask , redirect , render_template , url_for , flash,request,session
from app import db
from app.models import User

auth_bp = Blueprint('auth', __name__)

# USER_CREDENTIALS={
#     'username':'yash123',
#     'email':'yash@gmail.com',
#     'password':'1234'
# }

@auth_bp.route("/", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        my_user = User.query.filter((User.user_name==username) & (User.user_email==email) & (User.user_password==password)).first()
        if my_user:
            session['user'] = username
            flash("Login Successful" , 'success')
            return redirect(url_for('task.view_task'))
        else:
            flash('Invalid username or passord','danger')
    return render_template('login.html')

@auth_bp.route("/register", methods=['GET' ,'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        existing_user = User.query.filter((User.user_name==username)|(User.user_email==email)).first()
        if existing_user:
            flash('username or email already register')
            return redirect(url_for('auth.register'))
        new_user = User(user_name=username , user_email =email , user_password = password)
        db.session.add(new_user)
        db.session.commit()
        flash("registration successfully")
        return redirect(url_for("auth.login"))
    return render_template("register.html")


@auth_bp.route('/logout')
def logout():
    session.pop('user' ,None)
    flash('Logged Out', 'info')
    return redirect(url_for('auth.login'))