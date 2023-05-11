from flask import request, jsonify
import json
from utils import *
import numpy as np
from datetime import date, timedelta, datetime
from io import BytesIO
# from PIL import Image

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
    # image_data = request.json['image']
    # pil_image = Image.open(BytesIO(image_data))
    # pil_image.save('output.jpg')
    # res = "Hola"
    # img = np.array(json.loads(request.json), dtype=np.uint8)
    # real = (predictSpoofing(img) == "Real")
    # if real:
    detected_user_id = 1
    addattendance(detected_user_id, date.today(), True)
    res = "Marked Attendance"
    # else:
    #     res = "Spoofing detected"
    return jsonify(res)


def leaveRequest():
    id = 1
    body = request.json
    addLeave(id, datetime.strptime(body['start'],'%Y-%m-%d').date(), datetime.strptime(body['end'],'%Y-%m-%d').date(), body["location"], body["emergency_no"], body["home_town"], body["status"])
    return jsonify("Leave requested")


def attendanceRecord():
    body = request.json
    res = {}
    start = datetime.strptime(body['startdate'],'%Y-%m-%d').date()
    end = datetime.strptime(body['enddate'],'%Y-%m-%d').date()
    curr_date = start
    while curr_date <= end:
        leave_object = fetchUserAttendance(id, curr_date)
        if leave_object:
            curr_attendance = leave_object.status
        else:
            curr_attendance = False
        res[curr_date.strftime('%Y-%m-%d')] = curr_attendance
        curr_date += timedelta(days=1)
    print(res)
    return jsonify(res)


def leaveStatus():
    data = getUserLeaves(id)
    return jsonify(data)
