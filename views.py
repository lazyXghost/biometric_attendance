# from flask import request, jsonify
# from utils import *
# import numpy as np
# import json

"""
Student.query.filter_by(firstname='Sammy').all()
Student.query.get(3)
@app.route('/<int:student_id>/')
def student(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template('student.html', student=student)
"""

# def markAttendance():
#     # POST REQUEST
#     img = np.array(json.loads(request.json), dtype=np.uint8)
#     return (jsonify(predictSpoofing(img)))

def leaveRequest():
    # POST REQUEST
    # requires user to logged in
    # you will get form data in post request just need to store it in database
    return "Approved"

def attendanceRecord():
    # POST REQUEST
    # requires user logged in 
    # you will get dates to check attendance between in post request and on the basis of them fetch from database
    return "Absent all time"

def leaveStatus():
    # GET REQUEST
    # requires user logged in
    # check all the leaves of the user logged in and return his all leaves
    return "Not approved"