from flask import Blueprint, render_template
from flask_login import login_required, current_user


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():

    return render_template('profile.html', name=current_user.name)

#def assignment

#def calender

#def courses

#def messgaes

#Find ways to verify that this person is admin
#def admin_add_to_organzation
    #search function for admins to find sutdents and add them to a specific organization
    #only searching for student on the entire platform
    








