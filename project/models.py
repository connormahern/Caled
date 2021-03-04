from flask_login import UserMixin
from . import db

class User(UserMixin , db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    
    

#class student


#class admin

#class teacher

#class assignments_Student(UserMixin, db.model) :
#     id = db.Column(db.Integer, primary_key=True)
#     list assignments = db.relationship(db.Column(db.Integer), backref='author',  lazy=True)



#class messages(user_id)

#class calender(user_id)




    

