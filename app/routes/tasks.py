from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models import Task

task_bp = Blueprint('tasks', __name__)

#route to view tasks
@task_bp.route('/')
def view_tasks():
    # redirect to login if user not logged in
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

#route to add tasks
@task_bp.route('/add', methods=['POST'])
def add_tasks():
    # redirect to login if user not logged in
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    title = request.form.get('title')
    if title:
        new_task = Task(title=title, status = 'pending')
        db.session.add(new_task)
        db.session.commit()
        flash('Task Added successfully','success' )
    return redirect(url_for('tasks.view_tasks'))

@task_bp.route('/toggle/<int:task_id>', methods = ["POST"])
def toggle_status(task_id):
    task = Task.query.get(task_id)
    if task:
        if task.status == 'pending':
            task.status = 'working'
        elif task.status == 'working':
            task.status = 'done'
        else:
            task.status = 'pending'
        db.session.commit()
    return redirect(url_for('tasks.view_tasks'))

@task_bp.route('/clear', methods = ["POST"])
def clear_tasks():
    Task.query.delete()
    db.session.commit()
    flash("All Tasks Cleared", 'info')
    return redirect(url_for('tasks.view_tasks'))



    
