
from flask import Blueprint, render_template, redirect, url_for, request, flash, session, jsonify
from flask_login import login_required, current_user
from .models import Course, User
from Flask_SQLAlchemy import SQLAlchemy

main = Blueprint('main', __name__)
#engine = create_engine('sqlite:///db.sqlite')


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

    #Find Authincated Value for Student Teacher or Adimn
    #acess = sessions['access_var'] --> could 'Student' , 'Teacher', or 'Adim'
    #user_id = session['id']
    #user_email = session['email']
    #user_email = session['email']


    #if acess == student : 
        #Shouldnt have acess to list of other student/ all course grade

        #list_assignments = some sql query that returns a list of assignments
        #student_grades = 
        ##list_studentid = 


        #returning template = courses_student.html
    #elif teacher :
        #Shouldnt have acess to list of other student/ all course grade
        #List of assignments with grades

        #student_grades = [[id, assignment_num, grade], [id, assignment_num, grade]]



        #return render_template('courses_teacher.html', students_grades=students_grades)
    # elif admin :



        #return render_template('courses_admin.html', course=course)




    #sudentsEnrolled = course.enrroledID
    #Instructor[] = [course.instructorIN, teachers name, teachers email]
    #course_times = 
    #assignments = course[assigments]

    

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

@main.route('/calendar-events')
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
    








