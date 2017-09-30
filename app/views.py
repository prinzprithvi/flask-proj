from app import myApp as app
from flask import Blueprint,request,render_template
from app.user_models import *
from flask_login import login_user,logout_user,login_required,current_user

user_apis = Blueprint('app_views', __name__,template_folder='templates')


@app.route('/')
def index():
    #user = User()
    #user.username = 'test'
    #user.save()
    #user = User.objects.get(username='test')
    #login_user(user)
    return render_template("login.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You are now logged out'


@app.route('/home')
@login_required
def home():
    return 'The current user is' + current_user.username