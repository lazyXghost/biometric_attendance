from flask_sqlalchemy import SQLAlchemy
from context import app

db = SQLAlchemy(app)


class StudentDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    rollno = db.Column(db.String(20))


class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student_detail.id"))
    date = db.Column(db.Date)
    status = db.Column(db.Boolean)


class Leave(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student_detail.id"))
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
