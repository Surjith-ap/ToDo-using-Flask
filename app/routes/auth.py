from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User
from app.forms import RegistrationForm, LoginForm

# Create blueprint
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Registration route using WTForms"""
    
    # If user is already logged in, redirect to tasks
    if current_user.is_authenticated:
        return redirect(url_for('tasks.view_tasks'))
    
    form = RegistrationForm()
    
    # Validate form on submit
    if form.validate_on_submit():
        # Create new user
        new_user = User(
            username=form.username.data,
            email=form.email.data
        )
        new_user.set_password(form.password.data)  # Hash the password
        
        # Save to database
        db.session.add(new_user)
        db.session.commit()

        session.clear()

        flash(f'Account created for {form.username.data}! Please login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Login route using WTForms"""
    
    # If user is already logged in, redirect to tasks
    if current_user.is_authenticated:
        return redirect(url_for('tasks.view_tasks'))
    
    form = LoginForm()
    
    # Validate form on submit
    if form.validate_on_submit():
        # Find user in database
        user = User.query.filter_by(username=form.username.data).first()

        # Check if user exists and password is correct
        if user and user.check_password(form.password.data):
            login_user(user)  # Log the user in
            flash(f'Welcome back, {user.username}!', 'success')
            
            # Redirect to next page or tasks
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('tasks.view_tasks'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')

    return render_template('login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    """Logout route"""
    logout_user()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('auth.login'))