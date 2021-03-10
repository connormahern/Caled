
from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_required, current_user
from .models import Course, User


main = Blueprint('main', __name__)


#This can be a sample for of data that is in class course, we could query a table where user.id in enrolledID
course = [

    {
        'id' : 100,
        'name' : 'C100 - Intro to Computer Science',
        'teacherId' : 500,
        'enrolledId' : [1000, 1001, 1002, 1003, 1004, 1005]

    } , 
    {
        'id' : 101,
        'name' : 'C101 - Intro to Biology',
        'teacherId' : 501,
        'enrolledId' : [1006, 1007, 1008, 1009, 1010, 1011]

    } , 
    {
        'id' : 101,
        'name' : 'C101 - Intro to Biology',
        'teacherId' : 501,
        'enrolledId' : [1006, 1007, 1008, 1009, 1010, 1011]

    }, 
    {
        'id' : 101,
        'name' : 'C101 - Intro to Biology',
        'teacherId' : 501,
        'enrolledId' : [1006, 1007, 1008, 1009, 1010, 1011]

    }, 
    {
        'id' : 101,
        'name' : 'C101 - Intro to Biology',
        'teacherId' : 501,
        'enrolledId' : [1006, 1007, 1008, 1009, 1010, 1011]

    }

]

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():

    return render_template('profile.html', name=current_user.name)

@main.route('/courses')
@login_required
def courses():

    return render_template('courses.html', course=course)

@main.route('/index')
@login_required
def mainP():
    #This is our main page for calander and general organization
    return render_template('index.html', name=current_user.name)

@main.route('/messages')
@login_required
def messages():
    #This is our main page for messages
    return render_template('messages.html', name=current_user.name)

@main.route('/temp')
def temp():
    #This is a temporary page
    return render_template('temp.html')


#def assignment

#def calender

#def courses

#def messgaes

#Find ways to verify that this person is admin
#def admin_add_to_organzation
    #search function for admins to find sutdents and add them to a specific organization
    #only searching for student on the entire platform
    








