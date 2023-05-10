from flask import request, jsonify
import json
from utils import *
import numpy as np
from datetime import date, timedelta

"""
Student.query.filter_by(firstname='Sammy').all()
Student.query.get(3)
@app.route('/<int:student_id>/')
def student(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template('student.html', student=student)
"""

id = 1


def markAttendance():
    img = np.array(json.loads(request.json), dtype=np.uint8)
    return jsonify(predictSpoofing(img))


def leaveRequest():
    requestjson = {
        "student_id": 1,
        "name": "dishti",
        "rollno": "b20286",
        "mobile": "8130091185",
        "email": "b20286.students.iitmandi.ac.in",
        "hostel": "B16",
        "roomno": 13,
        "home_town": 1,
        "start": date(2023, 5, 20),
        "end": date(2023, 5, 30),
        "location": "Delhi",
        "emergency_no": "813009",
        "status": 1,
    }
    student_id = requestjson["student_id"]
    start = requestjson["start"]
    end = requestjson["end"]
    location = requestjson["location"]
    emergency_no = requestjson["emergency_no"]
    home_town = requestjson["home_town"]
    status = requestjson["status"]
    addLeave(student_id, start, end, location, emergency_no, home_town, status)
    return "Approved"


def attendanceRecord():
    datejson = {"startdate": date(2023, 5, 10), "enddate": date(2023, 5, 15)}
    res = {}
    start = datejson["startdate"]
    end = datejson["enddate"]
    curr = start
    while curr <= end:
        dict = fetchUserAttendanceStatus(id, curr)
        res[dict["date"]] = dict["status"]
        curr += timedelta(days=1)
    return res


def leaveStatus():
    data = getUserLeaveStatus(id)
    print(data)
    return "Hola"
