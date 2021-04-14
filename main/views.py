
from flask import Blueprint, render_template, redirect, url_for, request, flash, session, jsonify, Flask, current_app, g
from flask_login import login_required, current_user
from flask_login.utils import login_fresh
from .models import Instructor, User, Message, Course, StudentCourses, Organization, UserOrganizations
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
    userO = UserOrganizations.query.filter(currentUser['id'] == UserOrganizations.userId)
    organizationList = []

    for o in userO :
        organizationList.append(o.organization)

    organizationNames = []
    for name in organizationList :
        organizationNames.append(name.name)
    

    return render_template('profile.html', current=currentUser, organizationNames=organizationNames)

@views.route('/courses')
@login_required
def courses():

    coursesDict = []
    current = User.query.filter(User.email == session['email']).first()
    if current.userType == 'Instructor' :
        intructorCourses = Course.query.filter(Course.instructorId == current.id)
        coursesDict = []

        for course in intructorCourses :
            currentCorse = {
                'id' : course.id,
                'name' : course.name,
                'teacherId' : course.instructorId,
            }
            enrolledStudents = []

            for s in course.students :
                enrolledStudents.append(s.studentId)
            currentCorse['enrolledId'] = enrolledStudents
            coursesDict.append(currentCorse)


    elif current.userType == 'Student' :
        studentCourses = StudentCourses.query.filter(StudentCourses.studentId == current.id)
        # TODO FINISH STUDENT COURSE LIST IMPLENTATION

        coursesDict = []

        for course in studentCourses :
            for s in course.course :
                currentCorse = {
                    'id' : course.id,
                    'name' : course.name,
                    'teacherId' : course.instructorId,
                }
                coursesDict.append(currentCorse)

    return render_template('courses.html', course=coursesDict)

@views.route('/courses', methods=['GET', 'POST'])
@login_required
def courses_post():

    if request.method == 'POST':
        rerouteName = request.form['courseReroute']
        return redirect(url_for('views.coursePage', rerouteName=rerouteName))
        

@views.route('/coursePage/<rerouteName>')
@login_required
def coursePage(rerouteName):

    current = User.query.filter(User.email == session['email']).first()
    courseQuery = Course.query.filter(Course.id == int(rerouteName)).first()
    teacherQuery = User.query.filter(User.id == courseQuery.instructorId).first()

    courseInfo = {'courseNumber' : courseQuery.name, 'instructorName' : teacherQuery.name, 'org' : courseQuery.organization, 
    'courseDescription' : courseQuery.description}

    if current.id == courseQuery.instructorId :
        return render_template('coursePageInstructor.html', courseInfo=courseInfo)
    else : 
        return render_template('coursePage.html', courseInfo=courseInfo)

@views.route('/courseAddition', methods=['POST'])
@login_required
def courses_addition_post():

    current = User.query.filter(User.email == session['email']).first()
    course = request.form.get('course')
    semester = request.form.get('semester')
    organizationName = request.form.get('organization')
    description = request.form.get('description')
    instructorId = current.id

    new_course = Course(name=course, instructorId=instructorId, description=description, semester=semester, organization=organizationName)
    db.session.add(new_course)
    db.session.commit()


    return redirect(url_for('views.courses'))

@views.route('/courseAddition')
def course_addition() :

    current = User.query.filter(User.email == session['email']).first()
    if current.userType == 'Admin' or current.userType == 'Instructor' :

        return render_template('courseAddition.html')
    else :
        return redirect(url_for('views.profile'))


@views.route('/courseStudentAddition', methods=['POST'])
@login_required
def courses_student_addition_post():

    try :
        courseName = request.form.get('courseName')
        course = Course.query.filter(Course.name == courseName).first()
        studentEmail = request.form.get('studentEmail')
        student = User.query.filter(User.email == studentEmail).first()

        new_student = StudentCourses(courseId=course.id, studentId=student.id)
        db.session.add(new_student)
        db.session.commit()

    except :
        flash('No User with this Email Adress! Please try again!')
        return redirect(url_for('views.course_student_addition'))
    
    return redirect(url_for('views.courses'))

@views.route('/courseStudentAddition')
def course_student_addition() :

    current = User.query.filter(User.email == session['email']).first()
    if current.userType == 'Admin' or current.userType == 'Instructor' :
        return render_template('courseStudentAddition.html')
    else :
        return redirect(url_for('views.profile'))

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


#organization back-end implementation
@views.route('/organizations', methods=['GET', 'POST']) #organizations page lists all organizations associated with the admin 
@login_required
def organizations(): 
    current = User.query.filter(User.email == session['email']).first() #get current user (admin)
    if current.userType == 'Admin':
        adminId = current.id
        organizations = Organization.query.filter(adminId=adminId).first() #locate all organizations associated with admin
        return render_template('organizations.html', organizations=organizations) #returns organizations list to organizations page
    else:
        return redirect(url_for('views.profile')) #if user is not an admin, they are redirected to the profile page 


@views.route('/organizationAddition', methods=['POST'])
@login_required
def organization_addition_post():



    current = User.query.filter(User.email == session['email']).first()
    organizationName = request.form.get('organization')
    adminId = current.id

    newOrganization = Organization(name=organizationName, adminId=adminId)
    db.session.add(newOrganization)
    db.session.commit()


    return redirect(url_for('views.profile'))


@views.route('/organizationAddition')
def organization_addition() :
    current = User.query.filter(User.email == session['email']).first()
    if current.userType == 'Admin':
        return render_template('organizationAddition.html')
    else :
        return redirect(url_for('views.profile'))

@views.route('/organizationPage')
def organization_page() :
    current = User.query.filter(User.email == session['email']).first()


    if current.userType == 'Admin':
        return render_template('organizationPage.html')
    else :
        return redirect(url_for('views.profile'))

@views.route('/organizationPage', methods=['POST'])
def organization_page_post() :
    current = User.query.filter(User.email == session['email']).first()

    

    
    
    return render_template('organizationPage.html')
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
    








