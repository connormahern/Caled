from flask_login import UserMixin
from main import db
import datetime


# class User(UserMixin, db.Model):

#     __tablename__ = 'User'

#     id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
#     email = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))
#     name = db.Column(db.String(1000))

#     #students = db.relationship('student', backref='user', lazy=True) 
#     #instructors = db.relationship('instructor', backref='user', lazy=True)
#     #admins = db.relationship('admin', backref='user', lazy=True)

#     userType = db.Column(db.String(100)) #holds user selection for desired role (Admin/Student/Instructor)
#     hasAccess = db.Column(db.Boolean) #indicates if a user has access to the service t/f
    
    
#     def __repr__(self):
#         return f"User('{self.name}','{self.email}', '{self.hasAccess}')"


class User(UserMixin, db.Model):

    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    sentMessages = db.relationship('Message', back_populates='sender', foreign_keys='Message.senderId')
    recievedMessages = db.relationship('Message', back_populates='recipient', foreign_keys='Message.recipientId')
    
    #organizations = db.relationship('Organization', backref='User', lazy=True)

    userType = db.Column(db.String(100)) #holds user selection for desired role (Admin/Student/Instructor)
    hasAccess = db.Column(db.Boolean) #indicates if a user has access to the service t/f

    __mapper_args__ = { 
        "polymorphic_identity": "User",
        "polymorphic_on": userType
    }
    
    def set_password(self, password):
        self.password = password
    
    def __repr__(self):
        return f"User('{self.name}','{self.email}', '{self.hasAccess}')"

class Instructor(User):

    __tablename__ = 'Instructor'

    #id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    id = db.Column(db.ForeignKey('User.id'), primary_key=True) # primary keys are required by SQLAlchemy
    #email = db.Column(db.String(100), nullable=False, unique=True)
    #password = db.Column(db.String(100), nullable=False)
    #instructor_name = db.Column(db.String(1000))
    inststructorCourses = db.relationship('Course', backref='Instructor', lazy=True)
    # messages = db.relationship('Message', backref='Instruct', lazy=True) #specifies 1:M relationship between user and message tables
    # organizations = db.relationship('Organization', backref='Instructor', lazy=True)
    #instructorCourses = db.relationship('Course', back_populates='instructor', foreign_keys='Course.instructorId')

    # def set_password(self, password):
    #     self.password = generate_password_hash(password)

    __mapper_args__ = {"polymorphic_identity": "Instructor"}
    
    
	#def __repr__(self):
	#	return f"Instructor('{self.name}','{self.email}')"
    
class Student(User):

    __tablename__ = 'Student'

    id = db.Column(db.ForeignKey('User.id'), primary_key=True) # primary keys are required by SQLAlchemy
    #email = db.Column(db.String(100), unique=True)
    #password = db.Column(db.String(100))
    #student_name = db.Column(db.String(1000))
    #studentCourses = db.relationship('StudentCourses', backref='Student', lazy=True) #all courses that a student belongs to
    #messages = db.relationship('Message', backref='Student', lazy=True) #specifies 1:M relationship between user and message tables
    #organizations = db.relationship('Organization', backref='Student', lazy=True)
    studentCourses = db.relationship('StudentCourses', back_populates='student', foreign_keys='StudentCourses.studentId')
    # def set_password(self, password):
    #     self.password = generate_password_hash(password)

    __mapper_args__ = {"polymorphic_identity": "Student"}

    def __repr__(self):
        return f"Student('{self.name}','{self.email}')"      
        
class Admin(User):

    __tablename__ = 'Admin'

    #id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    id = db.Column(db.ForeignKey('User.id'), primary_key=True) # primary keys are required by SQLAlchemy
    #email = db.Column(db.String(100), unique=True)
    #password = db.Column(db.String(100))
    #admin_name = db.Column(db.String(1000))
    
    __mapper_args__ = {"polymorphic_identity": "Admin"}

    # def set_password(self, password):
    #     self.password = generate_password_hash(password)
          
    
class Course(UserMixin, db.Model):

    __tablename__ = 'Course'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    instructorId = db.Column(db.Integer, db.ForeignKey('Instructor.id'), nullable=False) #foreign key from user to link to message table
    # userId = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    #instructorId = db.Column(db.Integer, db.ForeignKey('Instructor.id', ondelete='cascade'))
    #instructor = db.relationship('Instructor', foreign_keys=instructorId)
    # studentId = db.Column(db.Integer, db.ForeignKey('Student.id', ondelete='set null'))
    students =  db.relationship('StudentCourses', back_populates='course')
    description = db.Column(db.String(10000))
    semester = db.Column(db.String(100))
    organization = db.Column(db.String(100))
    #modules = db.relationship('Module', backref='Course', lazy=True)
    

    def __repr__(self):
        return f"Course('{self.name}')"


class StudentCourses(UserMixin, db.Model):

    __tablename__ = 'StudentCourses'

    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(1000))
    # instructorId = db.Column(db.Integer, db.ForeignKey('Instructor.id'), nullable=False) #foreign key from user to link to message table
    # userId = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    #instructorId = db.Column(db.Integer, db.ForeignKey('Instructor.id', ondelete='cascade'))
    #instructor = db.relationship('Instructor', foreign_keys=instructorId)
    courseId =  db.Column(db.Integer, db.ForeignKey('Course.id', ondelete='cascade'), primary_key=True)
    course = db.relationship('Course', foreign_keys=courseId)
    studentId = db.Column(db.Integer, db.ForeignKey('Student.id', ondelete='set null'), primary_key=True)
    student =  db.relationship('Student', foreign_keys=studentId)


    def __repr__(self):
        return f"StudentCourses('{self.name}')"

class Message(UserMixin, db.Model):

    __tablename__ = 'Message'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String(100), nullable=False) #actual message
    #sender = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #foreign key from user to link to message table
    senderId = db.Column(db.Integer, db.ForeignKey('User.id', ondelete='cascade'))
    sender = db.relationship('User', foreign_keys=senderId)
    recipientId = db.Column(db.Integer, db.ForeignKey('User.id', ondelete='set null'))
    recipient =  db.relationship('User', foreign_keys=recipientId)
    dateTime = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow) #time message was received 
    isRead = db.Column(db.Boolean, default=False) #indicates if a message has been read

    def __repr__(self):
        return f"Message('{self.message}', '{self.dateTime}', '{self.isRead}')"


#def access(): #method for admin to grant access to user (i.e. move a user row to a instructor/student table)
    #needs to gain access to all users (not instructor/admins/students) in user table
    
    #user.query.all() #returns all data (as a list) in user table that is allowed to be shown (__rep__ method dictates what is shown when this query is called)



    #insert user to instructor/student table and delete user row from user table or deny access
    


    #add a user to instructor table

    #newInstructor = Instructor(user.email, user.password, user.name)
    #db.session.add(newInstructor) #adds instructor to instructor table in db
    #db.session.commit() #commits changes to db


    #add a user to student table

    #newStudent = Student(user.email, user.password, user.name)
    #db.session.add(newStudent) #adds student to student table in db
    #db.session.commit() #commits changes to db


    #add a user to admin table

    #newAdmin = Admin(user.email, user.password, user.name)
    #db.session.add(newAdmin) #adds admin to admin table in db
    #db.session.commit() #commits changes to db



##### SQLALCHEMY COMMAND LIST #####
#db.create_all() # creates db
#var = desiredTable(attribute1, attribute2, etc) #create a variable for a specific table 
#var.id #returns unique id for variable
#var.id.get(1) #returns a var with the unique id of 1
#db.session.add(var) #creates new row in desired table with variable
#db.session.commit() #commit changes to db
#Table.query.all() #displays all data in the specified 'Table'
#Table.query.filter_by(username='ctaddeuc').first() #returns all data that has the username 'ctaddeuc'