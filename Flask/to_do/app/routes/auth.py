from flask import Blueprint , Flask , redirect , render_template , url_for , flash,request,session

auth_bp = Blueprint('auth', __name__)

USER_CREDENTIALS={
    'username':'yash123',
    'email':'yash@gmail.com',
    'password':'1234'
}

@auth_bp.route("/", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        if username==USER_CREDENTIALS['username'] and email==USER_CREDENTIALS['email'] and password == USER_CREDENTIALS['password']:
            session['user'] = username
            flash("Login Successful" , 'success')
            return redirect(url_for('task.view_task'))
        else:
            flash('Invalid username or passord','danger')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user' ,None)
    flash('Logged Out', 'info')
    return redirect(url_for('auth.login'))