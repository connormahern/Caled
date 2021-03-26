
from flask import Blueprint, render_template, redirect, url_for, request, flash, session, jsonify, Flask
from flask_login import login_required, current_user
from .models import User
from flask_sqlalchemy import SQLAlchemy 
from main import db

#engine = create_engine('sqlite:///db.sqlite')
views = Blueprint('views', __name__)


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
# Adding Course Events to DB

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/profile')
@login_required
def profile():

    currentUser  = { 'id' : '10001', 'name' : current_user.name, 'email' : session['email'], 'password' : '********', 'userType' : 'Student'}

    return render_template('profile.html', current=currentUser)

rerouteName = None
@views.route('/courses')
@login_required
def courses():
    """ if request.method == 'POST' :
        rerouteName = request.form.get('courseReroute')
    else : """
    
    return render_template('courses.html', course=course)

@views.route('/coursePage')
@login_required
def coursePage():
    


    return render_template('coursePage.html', rerouteName=rerouteName)

@views.route('/index')
@login_required
def MainP():
    #This is our main page for calander and general organization
    return render_template('index.html', name=current_user.name)

@views.route('/messages')
@login_required
def messages():
    message = [ 
            {
                'id' : 20000,
                'name' : "Connor Mahern",
                'sender' : 'cjmahern@iu.edu',
                'recipient' : ['ctaddeuc@iu.edu'],
                'messageText' : 'Group Project! Soon! lets work',
                'date' : "03-23-2021 11:51 pm",
                'isRead' : False

            },
            {
                'id' : 20001,
                'name' : "Chris Taddeucci",
                'sender' : 'ctaddeuc@iu.edu',
                'recipient' : ['cjmahern@iu.edu'],
                'messageText' : 'for sure man',
                'date' : "03-23-2021 11:51 pm",
                'isRead' : True

            },
           {
                'id' : 20002,
                'name' : "Chris Taddeucci",
                'sender' : 'teacher@iu.edu',
                'recipient' : ['ctaddeuc@iu.edu'],
                'messageText' : "YOU HAVE BAD GRADE",
                'date' : "03-23-2021 11:51 pm",
                'isRead' : True
            },
            {
                'id' : 20003,
                'name' : "Connor Mahern",
                'sender' : 'cjmahern@iu.edu',
                'recipient' : ['ctaddeuc@iu.edu', 'teacher@iu.edu'],
                'messageText' : "The Instructor changed the deadline",
                'date' : "03-23-2021 11:51 pm",
                'isRead' : False
            },
            {

                'id' : 20004,
                'name' : "Teacher 1",
                'sender' : 'teacher@iu.edu',
                'recipient' : ['ctaddeuc@iu.edu', 'cjmahern@iu.edu'],
                'messageText' : "Thank you!",
                'date' : "03-23-2021 11:51 pm",
                'isRead' : True

            },
            {

                'id' : 20005,
                'name' : "Teacher 1",
                'sender' : 'teacher@iu.edu',
                'recipient' : ['ctaddeuc@iu.edu', 'cjmahern@iu.edu'],
                'messageText' : "Thanks for letting me know",
                'date' : "03-23-2021 11:51 pm",
                'isRead' : False

            }
        ]
    email = session['email']


    return render_template('messages.html', message=message, email=email)

@views.route('/calendar-events')
@login_required
def calendar_events():
    #This is a temporary page
    # conn = None
    # cursor = None
    # try :
    #     conn = engine.connect()
    #     cursor = conn.cursor()
    #     cursor.execute("SELECT id, title, url FROM event")
    #     rows = cursor.fetchall()
    #     resp = jsonify({'success' : 1, 'result' : rows})
    #     resp.status_code = 200
    #     return resp

    # except Exception as e :
    #     print(e)
    
    # finally :
    #     cursor.close()
    #     conn.close()


    
    return render_template('calendar.html')


#def assignment

#def calender

#def courses

#def messgaes

#Find ways to verify that this person is admin
#def admin_add_to_organzation
    #search function for admins to find sutdents and add them to a specific organization
    #only searching for student on the entire platform
    








