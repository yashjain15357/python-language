from flask import Blueprint , Flask , redirect , render_template , url_for , flash,request,session
from app import db
from app.models import Task

tasks_bp = Blueprint('task', __name__)
@tasks_bp.before_request
def require_login():
    if 'user' not in session:
        flash("Please login first!", "warning")
        return redirect(url_for('auth.login'))

@tasks_bp.route('/tasks')
def view_task():

    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    tasks = Task.query.all()
    return render_template('task.html' , tasks=tasks)

@tasks_bp.route('/add', methods=['POST'])
def add_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    title = request.form.get('title')
    if title:
        new_task = Task(title=title , status='Pending')
        db.session.add(new_task)
        db.session.commit()
        flash("Task added successfully",'success')
    return redirect(url_for('task.view_task'))


@tasks_bp.route('/toggle/<int:task_id>', methods=['POST'])
# logic of change the task status
def toggle_status(task_id):
    task = Task.query.get(task_id)
    if task:
        if task.status =='Pending':
            task.status = 'Working'
        elif task.status == 'Working':
            task.status = 'Done'
        else:
            task.status = 'Pending'
        db.session.commit()
    return redirect(url_for('task.view_task'))

@tasks_bp.route("/clear_all")
def clear_all(): 
    Task.query.delete()
    db.session.commit()
    flash("All the task deleted",'info')
    return redirect(url_for('task.view_task'))

@tasks_bp.route('/clear_tk/<int:task_id>')
def clear_tk(task_id):

    task = Task.query.get(task_id)
    if task:
        db.session.delete(task) #use for delete the particular task
        db.session.commit()
        flash("Task is clear",'info')
    else:
        flash("Task not found",'warning')
    return redirect(url_for('task.view_task'))
