from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    """Registration form with validation"""
    
    username = StringField('Username', 
                          validators=[
                              DataRequired(message='Username is required'),
                              Length(min=3, max=80, message='Username must be between 3 and 80 characters')
                          ])
    
    email = EmailField('Email', 
                      validators=[
                          DataRequired(message='Email is required'),
                          Email(message='Invalid email address')
                      ])
    
    password = PasswordField('Password', 
                            validators=[
                                DataRequired(message='Password is required'),
                                Length(min=6, message='Password must be at least 6 characters long')
                            ])
    
    confirm_password = PasswordField('Confirm Password', 
                                    validators=[
                                        DataRequired(message='Please confirm your password'),
                                        EqualTo('password', message='Passwords must match')
                                    ])
    
    submit = SubmitField('Register')
    
    # Custom validators
    def validate_username(self, username):
        """Check if username already exists"""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different one.')
    
    def validate_email(self, email):
        """Check if email already exists"""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already registered. Please use a different one.')


class LoginForm(FlaskForm):
    """Login form with validation"""
    
    username = StringField('Username', 
                          validators=[
                              DataRequired(message='Username is required')
                          ])
    
    password = PasswordField('Password', 
                            validators=[
                                DataRequired(message='Password is required')
                            ])
    
    submit = SubmitField('Login')


class TaskForm(FlaskForm):
    """Task creation form"""
    
    title = StringField('Task Title', 
                       validators=[
                           DataRequired(message='Task title is required'),
                           Length(min=1, max=100, message='Task title must be between 1 and 100 characters')
                       ])
    
    submit = SubmitField('Add Task')