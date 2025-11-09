from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import Task

task_bp = Blueprint('tasks', __name__)

# Route to view tasks
@task_bp.route('/')
@login_required  # Flask-Login decorator - automatically redirects if not logged in
def view_tasks():
    # Get only the current user's tasks
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks=tasks)

# Route to add tasks
@task_bp.route('/add', methods=['POST'])
@login_required  # Protect this route
def add_tasks():
    title = request.form.get('title')
    if title:
        # Create task and link it to current user
        new_task = Task(
            title=title, 
            status='To-Do',
            user_id=current_user.id  # Link to logged-in user
        )
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
    return redirect(url_for('tasks.view_tasks'))

# Route to toggle task status
@task_bp.route('/toggle/<int:task_id>', methods=["POST"])
@login_required
def toggle_status(task_id):
    # Get only the current user's task (security!)
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first()
    
    if task:
        if task.status == 'To-Do':
            task.status = 'In Progress'
        elif task.status == 'In Progress':
            task.status = 'Done'
        else:
            task.status = 'To-Do'
        db.session.commit()
        flash('Task status updated!', 'success')
    else:
        flash('Task not found or unauthorized!', 'danger')
    
    return redirect(url_for('tasks.view_tasks'))

# Route to clear all tasks
@task_bp.route('/clear', methods=["POST"])
@login_required
def clear_tasks():
    # Delete only current user's tasks
    Task.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    flash("All your tasks cleared!", 'info')
    return redirect(url_for('tasks.view_tasks'))