from flask_sqlalchemy import SQLAlchemy
import os
from app import app

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)

class StudentDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    rollno = db.Column(db.String(20))

class Leaves(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.Date)
    end = db.Column(db.Date)
    location = db.Column(db.String(255))
    emergency_no = db.Column(db.String(20))
    home_town = db.Column(db.Boolean)
    status = db.Column(db.Boolean)


"""
from app import db, Student
student_john = Student(firstname='john', lastname='doe',
                       email='jd@example.com', age=23,
                       bio='Biology student')
student_john.firstname
student_john.bio

db.session.add(student_john)
db.session.commit()

student_john.email = 'john_doe@example.com'
db.session.add(student_john)
db.session.commit()

Student.query.all()
"""