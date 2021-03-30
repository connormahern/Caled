
from flask import Blueprint, render_template, redirect, url_for, request, flash, session, jsonify, Flask, current_app, g
from flask_login import login_required, current_user
from flask_login.utils import login_fresh
from .models import User, Message
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.sql import text
from .__init__ import app, db

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

@views.route('/database')
def userData():

    query = User.query.filter(User.email == session['email']).first()
    data = { 'id' : query.id, 'name' : query.name, 'email' : query.email}
    
    return render_template('database.html', data=data)



@views.route('/profile')
@login_required
def profile():

    query = User.query.filter(User.email == session['email']).first()
    currentUser = { 'id' : query.id, 'name' : query.name, 'email' : query.email, 'userType' : query.userType}

    return render_template('profile.html', current=currentUser)

@views.route('/courses')
@login_required
def courses(): 
    return render_template('courses.html', course=course)


rerouteName = None
@views.route('/courses', methods=['GET', 'POST'])
@login_required
def courses_post():
    
    rerouteName = request.form.get('courseReroute')
    return redirect(url_for('views.coursePage'))

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
    
    email = session['email']
    currentQuery = User.query.filter(User.email == session['email']).first()
    currentName = currentQuery.name
    currentId = currentQuery.id
    currentEmail = currentQuery.email
    messageQuery = Message.query.filter(Message.recipientId == currentId).all()
    sentQuery = Message.query.filter(Message.senderId == currentId).all()


    if messageQuery is not None : 
        messageList = []
        for i in messageQuery :
            newMessage = {'id' : i.id, 'messageText' : i.message ,'senderId'  : i.senderId, 'recipientId': i.recipientId, 'date' : " ", 'isRead': i.isRead }
            
            senderQuery = User.query.filter(User.id == i.senderId).first()
            senderName = senderQuery.name
            senderEmail = senderQuery.email
            newMessage['name'] = senderName
            newMessage['recipient'] = currentEmail
            newMessage['sender'] = senderEmail
            messageList.append(newMessage)
        
        sentList = []
        for i in sentQuery :
            newMessage = {'id' : i.id, 'messageText' : i.message ,'senderId'  : i.senderId, 'recipientId': i.recipientId, 'date' : "  ", 'isRead': i.isRead }
            
            recipientQuery = User.query.filter(User.id == i.recipientId).first()
            recipientName = recipientQuery.name
            recipientEmail = recipientQuery.email
            newMessage['name'] = recipientName
            newMessage['recipient'] = recipientEmail
            newMessage['sender'] = currentEmail
            sentList.append(newMessage)
    


        return render_template('messages.html', message=messageList, sent=sentList, email=email, currentName=currentName)
    else :
        return render_template('messagesNone.html')

@views.route('/sendMessage')
@login_required
def sendMessage() :
    return render_template("sendMessage.html")

@views.route('/sendMessage', methods=['POST'])
def message_post():

    query = User.query.filter(User.email == session['email']).first()
    currentUser = { 'id' : query.id, 'name' : query.name, 'email' : query.email, 'userType' : query.userType}

    newMessage = request.form.get('message')
    senderId = query.id

    recipientEmail = request.form.get('email')
    try :
        recipientQuery = User.query.filter(User.email == recipientEmail).first()
        recipientId = recipientQuery.id
    
        new_message = Message(message=newMessage, senderId=senderId, recipientId=recipientId)
        db.session.add(new_message)
        db.session.commit()
    except :
        flash('No User in Organization with this Email Adress! Please try again!')
        return redirect(url_for('views.sendMessage'))


    return redirect(url_for('views.messages'))

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
    








